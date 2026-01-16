import os
import sys
import ollama
import lancedb
from pypdf import PdfReader
from rich.console import Console
from rich.markdown import Markdown

console = Console()

# --- Configuration ---
MODEL = "llama3"  # Ensure you have run: `ollama pull llama3`
EMBEDDING_MODEL = "nomic-embed-text" # Ensure you have run: `ollama pull nomic-embed-text`
DB_PATH = "./lancedb_store"

def get_embeddings(text):
    response = ollama.embeddings(model=EMBEDDING_MODEL, prompt=text)
    return response["embedding"]

def ingest_file(file_path):
    console.print(f"[bold blue]📄 Ingesting {file_path}...[/bold blue]")
    
    # 1. Read PDF
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # 2. Chunk Text (Naive splitting by paragraph/length)
    chunks = [text[i:i+500] for i in range(0, len(text), 450)]
    console.print(f"[green]✅ Created {len(chunks)} chunks.[/green]")

    # 3. Connect/Create DB
    db = lancedb.connect(DB_PATH)
    
    # 4. Embed and Store
    data = []
    with console.status("[bold yellow]🧠 Embedding chunks...[/bold yellow]"):
        for i, chunk in enumerate(chunks):
            embedding = get_embeddings(chunk)
            data.append({"vector": embedding, "text": chunk, "id": i})
    
    tbl = db.create_table("documents", data, mode="overwrite")
    console.print(f"[bold green]🎉 Indexed {len(data)} fragments into LanceDB![/bold green]")

def chat_loop():
    db = lancedb.connect(DB_PATH)
    tbl = db.open_table("documents")
    
    console.print("\n[bold cyan]🤖 RAG System Ready. Ask me anything about your doc![/bold cyan]")
    console.print("[dim](Type 'exit' to quit)[/dim]\n")

    while True:
        query = console.input("[bold magenta]You > [/bold magenta]")
        if query.lower() in ["exit", "quit"]:
            break

        # 1. Search Vector DB
        query_vec = get_embeddings(query)
        results = tbl.search(query_vec).limit(3).to_list()
        
        context = "\n\n".join([r["text"] for r in results])
        
        # 2. Generate Answer
        prompt = f"Using this context:\n{context}\n\nAnswer this question: {query}"
        
        console.print("[bold cyan]AI > [/bold cyan]", end="")
        stream = ollama.chat(model=MODEL, messages=[{'role': 'user', 'content': prompt}], stream=True)
        
        for chunk in stream:
            print(chunk['message']['content'], end="", flush=True)
        print("\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ingest_file(sys.argv[1])
    
    if os.path.exists(DB_PATH):
        chat_loop()
    else:
        console.print("[red]❌ No database found. Run `python rag.py document.pdf` first![/red]")

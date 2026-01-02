# 🏴‍☠️ The AI Hacker's Guide

This file contains non-obvious, "grey hat" optimization techniques to get performance that standard users don't get.

## 1. The "Repo Stitching" Technique (Context Stuffing)
**Goal:** Make an LLM understand a massive codebase that exceeds its context window.
**Hack:** Use `repomix` or `gingko` to pack your repo into a single XML-tagged file, but *remove* lockfiles and images.
**Tool:** `npm install -g repomix`
**Command:** `repomix --ignore "**/*.lock,**/*.svg"`
**Benefit:** Compresses 50 files into one prompt. Paste into Gemini 1.5 Pro (2M context) for a "Project Wide Refactor" that smaller models can't see.

## 2. The "Pre-computation" Workflow
**Goal:** Save money/time on reasoning models (o1/Claude).
**Hack:** Don't ask the expensive model to *write* the code first. Ask a cheap model (Flash/Haiku) to write a *comprehensive spec* and unit tests.
**Flow:**
1. **Gemini Flash:** "Write detailed unit tests for feature X."
2. **Claude 3.5 Sonnet:** "Implement feature X to pass THESE tests."
**Benefit:** You pin the logic with cheap tokens, then use expensive tokens only for high-quality syntax generation.

## 3. Local "Knowledge Graph" RAG
**Goal:** Make your AI remember business logic forever.
**Hack:** Don't rely on embeddings. Keep a markdown file `docs/logic.md` that is purely hard-rules.
**Rule:** Add `[Always read docs/logic.md before answering]` to your custom instructions.
**Benefit:** Hard-codes your business constraints (e.g., "Never expose UserID in API responses") into every generic valid answer.

## 4. The "Pseudo-Agent" Loop
**Goal:** Turn a standard chat into an agent.
**Hack:** Tell the model it is a REPL.
**Prompt:** "You are not a chat bot. You are a shell. If I ask for a task, output the exact terminal command to run it. If it needs code, output `cat <<EOF > filename.js` blocks. Do not talk."
**Benefit:** Allows you to copy-paste entire blocks into your terminal to "execute" the AI's will without an API key.

# 🔌 Model Context Protocol (MCP) - The Frontier

> **Warning:** This is advanced territory. MCP is the new standard (by Anthropic) allowing AI models to interact with your local environment, databases, and APIs securely.

## What is it?
Instead of just "chatting", MCP allows tools like Claude Desktop or IDEs to:
- Read/Write to your database directly.
- Execute terminal commands safely.
- Browse the internet via specific proxies.

## ⚡ Essential MCP Servers for 10x Engineers

| Server | Function | Why it's a Superpower |
| :--- | :--- | :--- |
| **[Filesystem MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** | Give AI full access to specific folders. | Let Claude analyze your entire `~/Documents/Specs` folder without uploading files. |
| **[Postgres MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)** | Read schema & query data. | Ask: "Why is the user query slow?" and have AI analyze the *real live* EXPLAIN PLAN. |
| **[Git MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** | Search history & diffs. | "When did we break the login feature?" -> AI hunts through git blame/logs. |
| **[Brave Search MCP](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)** | Real-time web access. | Give your local agents ability to Google solutions autonomously. |

## 🛠️ How to Set Up (Claude Desktop)

1. **Install uv** (Fast Python package manager):
   ```bash
   pip install uv
   ```
2. **Edit Config**:
   Open `%APPDATA%\Claude\claude_desktop_config.json`
3. **Add Server**:
   ```json
   {
     "mcpServers": {
       "filesystem": {
         "command": "uvx",
         "args": ["mcp-server-filesystem", "C:/Projects"]
       }
     }
   }
   ```
4. **Restart Claude**: You now have a "Chat with Filesystem" tool available.

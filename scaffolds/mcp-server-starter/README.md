# 🔌 MCP Server Starter

A minimal boilerplate for building **Model Context Protocol (MCP)** servers in TypeScript.

## What is this?
MCP allows you to connect Claude (Desktop) to your own tools and data. This template provides a basic server with two example tools:
1. `calculate-sum`
2. `get-system-time`

## 🚀 Setup

1. **Install Deps:**
   ```bash
   npm install
   ```
2. **Build:**
   ```bash
   npm run build
   ```
3. **Test with Claude:**
   Add this to your `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "my-starter": {
         "command": "node",
         "args": ["/absolute/path/to/mcp-server-starter/build/index.js"]
       }
     }
   }
   ```

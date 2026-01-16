#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
    CallToolRequestSchema,
    ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { z } from "zod";

// 1. Define the Server
const server = new Server(
    {
        name: "example-server",
        version: "1.0.0",
    },
    {
        capabilities: {
            tools: {},
        },
    }
);

// 2. Define Tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
    return {
        tools: [
            {
                name: "calculate-sum",
                description: "Add two numbers together",
                inputSchema: {
                    type: "object",
                    properties: {
                        a: { type: "number" },
                        b: { type: "number" },
                    },
                    required: ["a", "b"],
                },
            },
            {
                name: "get-system-time",
                description: "Returns the current server time",
                inputSchema: { type: "object" },
            },
        ],
    };
});

// 3. Handle Tool Execution
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    switch (request.params.name) {
        case "calculate-sum": {
            const { a, b } = request.params.arguments as any;
            return {
                content: [
                    {
                        type: "text",
                        text: String(a + b),
                    },
                ],
            };
        }
        case "get-system-time": {
            return {
                content: [
                    {
                        type: "text",
                        text: new Date().toISOString(),
                    },
                ],
            };
        }
        default:
            throw new Error("Unknown tool");
    }
});

// 4. Start Server
async function main() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
    console.error("MCP Server running on stdio");
}

main().catch((error) => {
    console.error("Server error:", error);
    process.exit(1);
});

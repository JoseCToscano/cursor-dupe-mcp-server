# Pair Programming Agent MCP Server

This is a Model Context Protocol (MCP) server that exposes a set of tools for pair programming with an AI assistant. The server provides functions for code search, file operations, terminal commands, and more.

## Requirements

- Python 3.10 or higher
- MCP Python SDK

## Installation

1. Create a virtual environment:
   ```bash
   python3.10 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the server with default settings (stdio transport, current directory as codebase root):
```bash
python pair_programming_agent.py
```

### Command-line Arguments

The server supports the following command-line arguments:

- `--codebase-root`: Default root directory of the codebase (default: current directory)
- `--transport`: Transport method for MCP, either 'stdio' or 'sse' (default: stdio)
- `--port`: Port for SSE transport (default: 8000)

Examples:

```bash
# Run with a specific default codebase root
python pair_programming_agent.py --codebase-root /path/to/your/codebase

# Run with SSE transport on port 9000
python pair_programming_agent.py --transport sse --port 9000
```

### Setting Codebase Root from Client

The server supports setting the codebase root in two ways:

1. **Using the `set_codebase_root` tool**:
   The server exposes a tool that allows clients to change the codebase root at runtime:
   ```python
   set_codebase_root("/path/to/new/codebase")
   ```

2. **Using context in tool calls**:
   Clients can provide a `codebase_root` parameter in the context of each tool call:
   ```python
   search_codebase("function_name", context={"codebase_root": "/path/to/codebase"})
   ```

This allows different clients to work with different codebases without restarting the server.

## Available Tools

The server exposes the following tools:

- `search_codebase`: Search the codebase for relevant code snippets
- `read_file`: Read the contents of a file
- `run_command`: Run a terminal command
- `list_directory`: List the contents of a directory
- `grep_search`: Perform a text-based regex search for exact pattern matches
- `edit_file`: Edit an existing file
- `search_file`: Search for a file by its name using fuzzy matching
- `delete_file`: Delete a file at the specified path
- `reapply_edit`: Reapply the last edit to the specified file
- `web_search`: Search the web for real-time information
- `get_diff_history`: Retrieve the history of recent changes made to files in the workspace
- `set_codebase_root`: Set the codebase root directory

## Integration with Claude for Desktop

To use this server with Claude for Desktop, add the following to your Claude for Desktop configuration file:

```json
{
    "mcpServers": {
        "pair_programming_agent": {
            "command": "python",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/pair_programming_agent",
                "pair_programming_agent.py"
            ]
        }
    }
}
```

Replace `/ABSOLUTE/PATH/TO/PARENT/FOLDER` with the absolute path to the parent directory of this project.

## License

MIT 
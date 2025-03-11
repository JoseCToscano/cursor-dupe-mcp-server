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
   pip install git+https://github.com/modelcontextprotocol/python-sdk.git httpx
   ```

## Usage

Run the server:
```bash
python pair_programming_agent.py
```

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
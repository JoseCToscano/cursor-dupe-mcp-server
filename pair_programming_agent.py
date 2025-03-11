from typing import List, Dict, Any, Optional, Union
import argparse
import os
from mcp.server.fastmcp import FastMCP

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Pair Programming Agent MCP Server')
parser.add_argument('--codebase-root', type=str, default=os.getcwd(),
                    help='Root directory of the codebase (default: current directory)')
parser.add_argument('--transport', type=str, choices=['stdio', 'sse'], default='stdio',
                    help='Transport method for MCP (default: stdio)')
parser.add_argument('--port', type=int, default=8000,
                    help='Port for SSE transport (default: 8000)')
args = parser.parse_args()

# Initialize FastMCP server
mcp = FastMCP("PairProgrammingAgent")

# Global variable to store the current codebase root
current_codebase_root = args.codebase_root

# Function to get the codebase root from context or use the default
def get_codebase_root(context: Dict[str, Any] = None) -> str:
    if context and 'codebase_root' in context:
        return context['codebase_root']
    return current_codebase_root

class PairProgrammingAgent:
    def __init__(self, codebase_root: str):
        self.codebase_root = codebase_root

# Create an instance of the agent
agent = PairProgrammingAgent(args.codebase_root)

@mcp.tool()
def search_codebase(query: str, target_directories: List[str] = [], context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Search the codebase for relevant code snippets.
    
    Args:
        query: The search query to find relevant code
        target_directories: Glob patterns for directories to search over (optional)
        context: Additional context from the client (optional)
    """
    codebase_root = get_codebase_root(context)
    return {
        "name": "codebase_search",
        "parameters": {
            "query": query,
            "target_directories": target_directories,
            "explanation": "Searching for relevant code snippets in the codebase."
        }
    }

@mcp.tool()
def read_file(target_file: str, start_line: int, end_line: int, should_read_entire_file: bool = False, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Read the contents of a file.
    
    Args:
        target_file: The path of the file to read
        start_line: The one-indexed line number to start reading from (inclusive)
        end_line: The one-indexed line number to end reading at (inclusive)
        should_read_entire_file: Whether to read the entire file (defaults to False)
        context: Additional context from the client (optional)
    """
    codebase_root = get_codebase_root(context)
    return {
        "name": "read_file",
        "parameters": {
            "target_file": target_file,
            "start_line_one_indexed": start_line,
            "end_line_one_indexed_inclusive": end_line,
            "should_read_entire_file": should_read_entire_file,
            "explanation": "Reading specific lines from the file to gather necessary context."
        }
    }

@mcp.tool()
def run_command(command: str, is_background: bool = False, require_user_approval: bool = True, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Run a terminal command.
    
    Args:
        command: The terminal command to execute
        is_background: Whether the command should be run in the background
        require_user_approval: Whether the user must approve the command before it is executed
        context: Additional context from the client (optional)
    """
    codebase_root = get_codebase_root(context)
    return {
        "name": "run_terminal_cmd",
        "parameters": {
            "command": command,
            "is_background": is_background,
            "require_user_approval": require_user_approval,
            "explanation": "Executing a command relevant to the coding task."
        }
    }

@mcp.tool()
def list_directory(relative_path: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """List the contents of a directory.
    
    Args:
        relative_path: Path to list contents of, relative to the workspace root
        context: Additional context from the client (optional)
    """
    codebase_root = get_codebase_root(context)
    return {
        "name": "list_dir",
        "parameters": {
            "relative_workspace_path": relative_path,
            "explanation": "Listing contents of the directory for codebase exploration."
        }
    }

@mcp.tool()
def grep_search(query: str, include_pattern: str = "*.py", case_sensitive: bool = False, exclude_pattern: str = "", context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Perform a text-based regex search for exact pattern matches.
    
    Args:
        query: The regex pattern to search for
        include_pattern: Glob pattern for files to include (e.g. '*.py' for Python files)
        case_sensitive: Whether the search should be case sensitive
        exclude_pattern: Glob pattern for files to exclude
        context: Additional context from the client (optional)
    """
    codebase_root = get_codebase_root(context)
    return {
        "name": "grep_search",
        "parameters": {
            "query": query,
            "include_pattern": include_pattern,
            "case_sensitive": case_sensitive,
            "exclude_pattern": exclude_pattern,
            "explanation": "Performing a text-based search for exact matches in the codebase."
        }
    }

@mcp.tool()
def edit_file(target_file: str, instructions: str, code_edit: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Edit an existing file.
    
    Args:
        target_file: The target file to modify
        instructions: A single sentence instruction describing what you are going to do
        code_edit: The code edit to apply
        context: Additional context from the client (optional)
    """
    codebase_root = get_codebase_root(context)
    return {
        "name": "edit_file",
        "parameters": {
            "target_file": target_file,
            "instructions": instructions,
            "code_edit": code_edit
        }
    }

@mcp.tool()
def search_file(query: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Search for a file by its name using fuzzy matching.
    
    Args:
        query: Fuzzy filename to search for
        context: Additional context from the client (optional)
    """
    codebase_root = get_codebase_root(context)
    return {
        "name": "file_search",
        "parameters": {
            "query": query,
            "explanation": "Searching for a file by its name using fuzzy matching."
        }
    }

@mcp.tool()
def delete_file(target_file: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Delete a file at the specified path.
    
    Args:
        target_file: The path of the file to delete
        context: Additional context from the client (optional)
    """
    codebase_root = get_codebase_root(context)
    return {
        "name": "delete_file",
        "parameters": {
            "target_file": target_file,
            "explanation": "Deleting a file that is no longer needed."
        }
    }

@mcp.tool()
def reapply_edit(target_file: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Reapply the last edit to the specified file.
    
    Args:
        target_file: The relative path to the file to reapply the last edit to
        context: Additional context from the client (optional)
    """
    codebase_root = get_codebase_root(context)
    return {
        "name": "reapply",
        "parameters": {
            "target_file": target_file
        }
    }

@mcp.tool()
def web_search(search_term: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Search the web for real-time information.
    
    Args:
        search_term: The search term to look up on the web
        context: Additional context from the client (optional)
    """
    return {
        "name": "web_search",
        "parameters": {
            "search_term": search_term,
            "explanation": "Searching the web for real-time information on the topic."
        }
    }

@mcp.tool()
def get_diff_history(context: Dict[str, Any] = None) -> Dict[str, Any]:
    """Retrieve the history of recent changes made to files in the workspace.
    
    Args:
        context: Additional context from the client (optional)
    """
    codebase_root = get_codebase_root(context)
    return {
        "name": "diff_history",
        "parameters": {
            "explanation": "Retrieving recent changes made to files in the codebase."
        }
    }

@mcp.tool()
def set_codebase_root(new_codebase_root: str) -> Dict[str, Any]:
    """Set the codebase root directory.
    
    Args:
        new_codebase_root: The absolute path to the codebase root directory
    """
    global current_codebase_root
    if os.path.isdir(new_codebase_root):
        current_codebase_root = new_codebase_root
        return {
            "success": True,
            "message": f"Codebase root set to: {new_codebase_root}"
        }
    else:
        return {
            "success": False,
            "message": f"Directory does not exist: {new_codebase_root}"
        }

if __name__ == "__main__":
    print(f"Starting Pair Programming Agent MCP Server")
    print(f"Default codebase root: {current_codebase_root}")
    print(f"Transport: {args.transport}")
    
    if args.transport == 'stdio':
        # Initialize and run the server with stdio transport
        mcp.run(transport='stdio')
    else:
        # Initialize and run the server with SSE transport
        mcp.run(transport='sse', port=args.port) 
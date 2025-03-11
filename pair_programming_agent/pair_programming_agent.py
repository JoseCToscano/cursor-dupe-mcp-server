from typing import List, Dict, Any, Optional, Union
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("PairProgrammingAgent")

class PairProgrammingAgent:
    def __init__(self, codebase_root: str):
        self.codebase_root = codebase_root

@mcp.tool()
def search_codebase(query: str, target_directories: List[str] = []) -> Dict[str, Any]:
    """Search the codebase for relevant code snippets.
    
    Args:
        query: The search query to find relevant code
        target_directories: Glob patterns for directories to search over (optional)
    """
    return {
        "name": "codebase_search",
        "parameters": {
            "query": query,
            "target_directories": target_directories,
            "explanation": "Searching for relevant code snippets in the codebase."
        }
    }

@mcp.tool()
def read_file(target_file: str, start_line: int, end_line: int, should_read_entire_file: bool = False) -> Dict[str, Any]:
    """Read the contents of a file.
    
    Args:
        target_file: The path of the file to read
        start_line: The one-indexed line number to start reading from (inclusive)
        end_line: The one-indexed line number to end reading at (inclusive)
        should_read_entire_file: Whether to read the entire file (defaults to False)
    """
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
def run_command(command: str, is_background: bool = False, require_user_approval: bool = True) -> Dict[str, Any]:
    """Run a terminal command.
    
    Args:
        command: The terminal command to execute
        is_background: Whether the command should be run in the background
        require_user_approval: Whether the user must approve the command before it is executed
    """
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
def list_directory(relative_path: str) -> Dict[str, Any]:
    """List the contents of a directory.
    
    Args:
        relative_path: Path to list contents of, relative to the workspace root
    """
    return {
        "name": "list_dir",
        "parameters": {
            "relative_workspace_path": relative_path,
            "explanation": "Listing contents of the directory for codebase exploration."
        }
    }

@mcp.tool()
def grep_search(query: str, include_pattern: str = "*.py", case_sensitive: bool = False, exclude_pattern: str = "") -> Dict[str, Any]:
    """Perform a text-based regex search for exact pattern matches.
    
    Args:
        query: The regex pattern to search for
        include_pattern: Glob pattern for files to include (e.g. '*.py' for Python files)
        case_sensitive: Whether the search should be case sensitive
        exclude_pattern: Glob pattern for files to exclude
    """
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
def edit_file(target_file: str, instructions: str, code_edit: str) -> Dict[str, Any]:
    """Edit an existing file.
    
    Args:
        target_file: The target file to modify
        instructions: A single sentence instruction describing what you are going to do
        code_edit: The code edit to apply
    """
    return {
        "name": "edit_file",
        "parameters": {
            "target_file": target_file,
            "instructions": instructions,
            "code_edit": code_edit
        }
    }

@mcp.tool()
def search_file(query: str) -> Dict[str, Any]:
    """Search for a file by its name using fuzzy matching.
    
    Args:
        query: Fuzzy filename to search for
    """
    return {
        "name": "file_search",
        "parameters": {
            "query": query,
            "explanation": "Searching for a file by its name using fuzzy matching."
        }
    }

@mcp.tool()
def delete_file(target_file: str) -> Dict[str, Any]:
    """Delete a file at the specified path.
    
    Args:
        target_file: The path of the file to delete
    """
    return {
        "name": "delete_file",
        "parameters": {
            "target_file": target_file,
            "explanation": "Deleting a file that is no longer needed."
        }
    }

@mcp.tool()
def reapply_edit(target_file: str) -> Dict[str, Any]:
    """Reapply the last edit to the specified file.
    
    Args:
        target_file: The relative path to the file to reapply the last edit to
    """
    return {
        "name": "reapply",
        "parameters": {
            "target_file": target_file
        }
    }

@mcp.tool()
def web_search(search_term: str) -> Dict[str, Any]:
    """Search the web for real-time information.
    
    Args:
        search_term: The search term to look up on the web
    """
    return {
        "name": "web_search",
        "parameters": {
            "search_term": search_term,
            "explanation": "Searching the web for real-time information on the topic."
        }
    }

@mcp.tool()
def get_diff_history() -> Dict[str, Any]:
    """Retrieve the history of recent changes made to files in the workspace.
    """
    return {
        "name": "diff_history",
        "parameters": {
            "explanation": "Retrieving recent changes made to files in the codebase."
        }
    }

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio') 
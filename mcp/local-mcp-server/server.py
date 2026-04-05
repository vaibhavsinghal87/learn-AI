# Example of updating local files using MCP.
# writing to local files can be used to share memory between LLMs

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LocalMCPServer")


@mcp.tool()
def write_to_file(content: str) -> str:
    """Write content to a file."""

    filename = "notes.txt"
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(content + "\n")
            return f"Content written to {filename}"
    except Exception as e:
        return f"Error writing to file: {str(e)}"


if __name__ == "__main__":
    mcp.run()

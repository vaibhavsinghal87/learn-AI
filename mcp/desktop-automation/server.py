# Example of a simple desktop automation tool for MCP.

import io

import pyautogui
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image

mcp = FastMCP("ScreenshotTool")


@mcp.tool()
def capture_screenshot() -> Image:
    """
    Capture a screenshot of the current desktop and return it as an image.
    """

    buffer = io.BytesIO()

    screenshot = pyautogui.screenshot()
    screenshot.convert("RGB").save(buffer, format="PNG")
    return Image(data=buffer.read(), format="PNG")


if __name__ == "__main__":
    mcp.run()

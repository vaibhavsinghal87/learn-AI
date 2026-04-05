# Example of calling API using MCP.

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CryptoAPI")


@mcp.tool()
def get_cryptocurrencyprice(crypto: str) -> str:
    """
    Get the current price of a cryptocurrency.
    Args:
    crypto (str): The name of the cryptocurrency (e.g., "Bitcoin", "Ethereum
    """

    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto.lower()}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        price = data.get(crypto.lower(), {}).get("usd")
        return f"The current price of {crypto} is ${price} USD."
    except Exception as e:
        return f"Error fetching price for {crypto}: {str(e)}"


if __name__ == "__main__":
    mcp.run()

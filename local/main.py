from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def count_letters_in_word(word: str, letter: str) -> int:
    return word.lower().count(letter.lower())

if __name__ == "__main__":
    mcp.run()
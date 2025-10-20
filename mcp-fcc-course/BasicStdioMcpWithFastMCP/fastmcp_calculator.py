from fastmcp import FastMCP

mcp = FastMCP(name = "Calculator")

@mcp.tool()
def multiply(a: float, b: float) -> float:
  """Multiplies two numbers.

  args: a (float): The first number.
        b (float): The second number.

  returns: float: The product of the two numbers.
  """
  return a * b

@mcp.tool(
  name = "add",
  description = "Add two numbers.",
  tags = ["arithmetic", "addition", "math"]
)
def add_numbers(x: float, y: float) -> float:
  """Adds two numbers.

  args: x (float): The first number.
        y (float): The second number.

  returns: float: The sum of the two numbers.
  """
  return x + y

@mcp.tool()
def subtract(a: float, b: float) -> float:
  """Subtracts the second number from the first.

  args: a (float): The first number.
        b (float): The second number.

  returns: float: The result of the subtraction.
  """
  return a - b

@mcp.tool()
def divide(a: float, b: float) -> float:
  """Divides the first number by the second.

  args: a (float): The numerator.
        b (float): The denominator.

  returns: float: The result of the division.
  """
  if b == 0:
    raise ValueError("Denominator cannot be zero.")

  return a / b

if __name__ == "__main__":
  mcp.run() # STDIO by default


# Run Calculator MCP with: python fastmcp_calculator.py
# MCP Inspector: npx @modelcontextprotocol/inspector python fastmcp_calculator.py [from inside BasicStdioMcpWithFastMCP folder]

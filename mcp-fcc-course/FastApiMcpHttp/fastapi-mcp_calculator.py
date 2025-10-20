# HTTP
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

#1. Let's make a FastAPI app (that means API) first

app = FastAPI(title = "Calculator API")

@app.post("/multiply")
def multiply(a: float, b: float):
  """
  Multiplies two numbers and returns the result.

  args: a (float): The first number.
        b (float): The second number.

  returns: float: The product of the two numbers.
  """
  result = a * b
  return {"result": result}

@app.post("/add")
def add_numbers(a: float, b: float):
  """
  Adds two numbers and returns the result.

  args: a (float): The first number.
        b (float): The second number.

  returns: float: The sum of the two numbers.
  """
  result = a + b
  return {"result": result}

@app.post("/subtract")
def subtract(a: float, b: float):
  """
  Subtracts the second number from the first and returns the result.

  args: a (float): The first number.
        b (float): The second number.

  returns: float: The result of the subtraction.
  """
  result = a - b
  return {"result": result}

@app.post("/divide")
def divide(a: float, b: float):
  """
  Divides the first number by the second and returns the result.

  args: a (float): The numerator.
        b (float): The denominator.

  returns: float: The result of the division.
  """
  if b == 0:
    raise ValueError("Denominator cannot be zero.")

  result = a / b
  return {"result": result}

#2. Converting it to MCP
mcp = FastApiMCP(app, name = "Calculator MCP")
mcp.mount_http()

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="localhost", port=8002)

# Run Calculator API with: python fastapi-mcp_calculator.py [from within FastApiMcpHttp folder]
# Access API docs at: http://localhost:8002/docs
# MCP Inspector: npx @modelcontextprotocol/inspector http://localhost:8002/mcp
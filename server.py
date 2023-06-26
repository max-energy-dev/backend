from jsonrpcserver import method, serve

# Define the RPC methods
@method
def add(a, b):
    return a + b

@method
def subtract(a, b):
    return a - b

@method
def multiply(a, b):
    return a * b

@method
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

# Start the RPC server
serve(methods=[add, subtract, multiply, divide])

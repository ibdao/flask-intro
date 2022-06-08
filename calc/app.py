from flask import Flask, request
import operations
app = Flask(__name__)

OPERATIONS = {
    "add" : operations.add,
    "sub" : operations.sub,
    "mult" : operations.mult,
    "div" : operations.div,
}

@app.get("/<operation>")
def math_operation(operation):
    """ Handle GET requests for various math operations
        Query string arguments include:
            a = first number
            b = second number
    """
    a = int(request.args["a"])
    b = int(request.args["b"])
    func = OPERATIONS[operation]
    result = func(a,b)
    return (f"<html><body>{result}</body></html>")

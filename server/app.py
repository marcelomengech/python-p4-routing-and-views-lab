from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    # Print to console
    print(input_string)
    # Return to browser
    return input_string

@app.route('/count/<int:num>')
def count(num):
    # Create a string of numbers from 0 to num-1, each on a new line
    # Add an extra newline at the end to match the test expectation
    return '\n'.join(str(i) for i in range(num)) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    # Perform mathematical operations based on the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        # Handle division by zero
        if num2 == 0:
            return 'Error: Division by zero'
        result = num1 / num2
    elif operation == '%':
        # Handle modulo with zero
        if num2 == 0:
            return 'Error: Modulo by zero'
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    # Convert result to string for display
    return str(result)

if __name__ == '__main__':
    app.run(port=5555)
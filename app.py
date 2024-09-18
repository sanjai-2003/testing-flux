from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask app!"

# Dynamic route with path parameter
@app.route('/user/<username>')
def user_profile(username):
    return f"Hello, {username}! This is your profile."

# Route with query parameters
@app.route('/search')
def search():
    query = request.args.get('q', '')
    return f"Search results for: {query}"

# POST route with form data
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.form['data']
    return f"Form submitted with data: {data}"

# POST route for JSON data
@app.route('/json', methods=['POST'])
def json_data():
    data = request.get_json()
    response = {
        "message": "JSON received!",
        "received_data": data
    }
    return jsonify(response)

# Route for summing two numbers (path parameters)
@app.route('/add/<int:num1>/<int:num2>')
def add_numbers(num1, num2):
    result = num1 + num2
    return f"The sum of {num1} and {num2} is {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

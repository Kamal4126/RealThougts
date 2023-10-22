from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route and a function to handle it
@app.route('/home')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)


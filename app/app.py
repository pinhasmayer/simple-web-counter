from flask import Flask, request

app = Flask(__name__)

# Initialize the counter
counter = 0

@app.route('/', methods=['POST'])
def increment_counter():
    global counter
    counter += 1
    return {"message": "Counter incremented successfully"}, 200

@app.route('/', methods=['GET'])
def get_counter():
    global counter
    return {"counter": counter}, 200

if __name__ == "__main__":
    # Run the Flask app on port 80
    app.run(host='0.0.0.0', port=80)


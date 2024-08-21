from flask import Flask, request, jsonify
import json 

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page"

@app.route('/api/data', methods=['POST'])
def receive_data():
    try:
        # Get the JSON data from the request
        json_data = request.get_json()
        
        # Save the JSON data to a file
        with open('received_data.json', 'w') as file:
            json.dump(json_data, file, indent=4)
        
        return jsonify({"message": "Data received and saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
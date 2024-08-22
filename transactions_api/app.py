from flask import Flask, request, jsonify
from jsonschema import validate, ValidationError
import json 

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page"


@app.route('/api/data', methods=['POST'])
def receive_data():
    # Get the JSON data from the request
    json_data = request.get_json()
    # input validation 
    validate_data(json_data)
    # Save the JSON data to a file
    with open('received_data.json', 'w') as file:
        json.dump(json_data, file, indent=4)
    return jsonify({"message": "Transaction data received and saved successfully"}), 200


def validate_data(data):
    try: 
        # Define the schema for the JSON data
        schema = {
            "type": "object",
            "properties": {
                "accountNumber": {"type": "string"},
                "amount": {"type": "float"},
                "vendor": {"type": "string"},
                "timestamp": {"type": "string"}
            },
            "required": ["transaction_id", "user_id", "amount", "currency", "timestamp"]
        }
        # Validate the JSON data against the schema
        validate(instance=data, schema=schema)
    except ValidationError as e:
        raise Exception(f"Invalid JSON data: {e.message}")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)
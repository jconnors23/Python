from flask import Flask, request, jsonify
from schema import Schema, And, Use, Optional, SchemaError
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
    # validate_data(json_data)
    validate_transactions(json_data)
    # Save the JSON data to a file
    with open('received_data.json', 'w') as file:
        json.dump(json_data, file, indent=4)
    return jsonify({"message": "Transaction data received and saved successfully"}), 200


# Define the schema for a single transaction
transaction_schema = Schema({
    'accountNumber': And(int, lambda n: n > 0),
    'amount': And(float, lambda f: f >= 0),
    'vendor': str,
    'timestamp': And(str, Use(lambda s: s.endswith('Z')))
})
# Define the schema for multiple transactions
transactions_schema = Schema([transaction_schema])


def validate_transactions(transactions):
    try:
        transactions_schema.validate(transactions)
        print("Validation successful.")
    except SchemaError as e:
        error_message = f"Validation error occured for transaction schema: {e}"
        print(error_message)
        raise ValueError(error_message)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)



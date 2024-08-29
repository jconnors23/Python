# past validation 

# def validate_data(data):
#     try: 
#         # Define the schema for the JSON data
#         schema = {
#             "type": "object",
#             "properties": {
#                 "accountNumber": {
#                     "type": "number",
#                     "description": "The user's account number"
#                 },
#                 "amount": {
#                     "type": "number",
#                     "description": "monetary value of transaction"
#                 },
#                 "vendor": {
#                     "type": "string",
#                     "description": "merchant"
#                 },
#                 # "timestamp": {"type": "string",
#                 #               "format": "date-time",
#                 #               "description": "time of transaction"
#                 # }
#             },
#             "required": ["accountNumber", "amount", "vendor"]
#         }
#         # Validate the JSON data against the schema
#         validate(instance=data, schema=schema)
#     except ValidationError as e:
#         raise Exception(f"Invalid JSON data: {e.message}")
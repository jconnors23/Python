# POST Request
# Simulates saving a group of transactions, data comes from client
# Payload is transaction JSON Array 
# input validation 

# Account Number: Integer
# Timestamp: ISO 8601 timestamp
# Vendor: String
# Amount: Float, two decimal places

# [
#     {
#         "accountNumber": 123456,
#         "amount": 250.75,
#         "vendor": "Example Vendor 1",
#         "timestamp": "2023-10-01T12:34:56Z"
#     },
#     {
#         "accountNumber": 789012,
#         "amount": 100.00,
#         "vendor": "Example Vendor 2",
#         "timestamp": "2023-10-02T14:20:00Z"
#     }
# ]
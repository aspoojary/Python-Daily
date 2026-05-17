# api_response = {
#     "status": "success",
#     "user": {
#         "name": "John"
#     }
# }

# username = api_response.get("user", {}).get("name")

# print(username)

person = {
    "name": "Anna",
    "age": 25,
    "city": "Ingolstadt"
}

# print(person["name"])  # Anna

person = person.get("name", "not found")

print(person)
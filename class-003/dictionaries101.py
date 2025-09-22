import json

with open("person.json") as infile:
    data = json.load(infile)

print(data)

# person = {
#     "name": "Sam",
#     "age": "won't tell",
#     "city": "Brooklyn",
#     "favorite_authors": ["kafka", "lispector", "tolstoy"],
# }

# with open("person.json", "w") as outfile:
#     json.dump(person, outfile)

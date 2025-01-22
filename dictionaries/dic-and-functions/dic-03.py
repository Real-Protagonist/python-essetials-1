dictionary = {
        "cat": "chat",
        "dog": "chien",
        "horse": "cheval"
}

dictionary['cat'] = "minou"
print(dictionary)

for key in sorted(dictionary.keys()):
    print(key)

print()

for french in dictionary.values():
    print(french)

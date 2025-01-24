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

# ADDING A NEW KEY
print()
print("ADDING A NEW KEY")
dictionary['swan'] = 'cygne'
print(dictionary)

# ADDING A NEW KEY BY UPDATE THE DIC
print()
print("ADDING A NEW KEY BY UPDATE")
dictionary.update({"duck": "canard"})
print(dictionary)

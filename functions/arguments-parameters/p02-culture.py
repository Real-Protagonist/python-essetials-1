def introduction(culture, first_name, last_name):
    if culture != "HNG":
        print("Hello, my name is: ", first_name, last_name)
    else:
        print("Hello, my name is: ", last_name, first_name)

first_name = input("First Name: ")
last_name = input("Last Name: ")
nacionality = input("Nacionality (ex. AO): ")

introduction(nacionality, first_name, last_name)

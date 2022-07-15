import json 

#this is question for ask to person
detail = [
    "Full Name",
    "Nick Name",
    "Age",
    "Phone No",
    "Address",
    "Work",
    "ID",
    "Password",
    "About",
]

#this is save a data

data = {}

for d in detail:
    
    user = input(f"{d} >> ")
    new = {f"{d}":f"{user}"}
    data.update(new)

print(data)

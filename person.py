import json 

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

data = '{}'

# json_data = str(data)

new_data = json.loads(data)

for d in detail:
    
    user = input(f"{d} >> ")
    new = {f"{d}":f"{user}"}
    new_data.update(new)

print(new_data)


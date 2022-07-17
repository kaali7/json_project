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
json_file = open("infro.json", "a")

data = '{}'

json_data = json.loads(data)

for d in detail:
    
    user = input(f"{d} >> ")
    new = {f"{d}":f"{user}"}
    json_data.update(new)

ID = json_data["ID"]

person = {
    f"{ID}": json_data
}

json_file.write(json.dumps(person))

json_file.close()


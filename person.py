import json 

#this is question for ask to person
detail = [
    "ID",
    "Full Name",
    "Nick Name",
    "Age",
    "Phone No",
    "Address",
    "Work",
    "Insta I'd",
    "Insta Password",
    "About",
]

#what u want write a new person detail and search old person detail
print("What u want ? write a new person detail and read old person detail\n")

print("write for \'w\' or read for \'r\' \n")
user = input(">> ")

if user=="w":

    json_file_R = open("infro.json", "r")
    json_data = json.load(json_file_R)         

    json_file_W = open("infro.json", "w")

    data = {}                              

    ID = ""

    for d in detail:
        if d=="ID":
            print("Next person don't get your detail\n")
            print("Frist create our ID\n")
            ID = input(f"{d} >> ")

        else:
            user = input(f"{d} >> ")
            new = {f"{d}":f"{user}"}
            data.update(new)


    person = {f"{ID}": data}       

    json_data.update(person)

    json.dump(json_data, json_file_W, indent=4)
    
    json_file_W.close()
    json_file_R.close()
    

elif user=="r":
    print("reading data.......")

else:
    print("plz! enter proporly again.")



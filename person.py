import json
from operator import truediv 

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

print("write for \'w\' or read for \'r\'")
user = input(">> ")

if user=="w":

    json_file_R = open("infro.json", "r")
    json_data = json.load(json_file_R)         

    json_file_W = open("infro.json", "w")

    data = {}                              

    ID = ""
    
    while True:
        for d in detail:
            if d=="ID":
                print("\n")
                print("Next person don't get your detail")
                print("Frist create our ID\n")
                ID = input(f"{d} >> ")

            else:
                user_data = input(f"{d} >> ")
                new = {f"{d}":f"{user_data}"}
                data.update(new)
        
        print("\n")
        print("IF u want to change anything type \'y\' and press enter")
        ans = input(">> ")
        if ans == "y":
            continue
        else:
            break
        

    person = {f"{ID}": data}       

    json_data.update(person)

    json.dump(json_data, json_file_W, indent=4)
    
    json_file_W.close()
    json_file_R.close()
    

elif user=="r":
    
    json_file = open("infro.json", "r")
    
    json_data = json.load(json_file)
    
    print("\n")
    print("Enter the I'd of person, who person detail u want")

    for i in range(3):

        ans = input(" ID >> ")
    
        if ans in json_data.keys():

            user_data = json_data[ans]

            print("Choice : ", end="")
            for d in detail:print(d, end=", ")
            print(", ALL ")

            print("\n")
            print("What type data you want? :\" ")
            
            user_need = input("Quik for q >> ")

            while True:
                if user_need in detail:

                    print("\n")
                    print(f"{user_need} :-> {user_data[user_need]}")
                    break

                elif user_need == "ALL":

                    print("\n")
                    for data in user_data:
                        print(f"{data} :-> {user_data[data]}")
                    break
            
                else:
                    print("Enter plz!, rightly")
                    continue


            break
        
        elif ans not in json_data.keys():
            print(f"you have {3-i+1} die")

        elif ans not in json_data.keys() and i>=3:
            print(" YOU ARE! BLOCK :}")


else:
    print("plz! enter proporly again.")



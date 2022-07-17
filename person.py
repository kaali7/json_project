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

print("write for \'w\' or read for \'r\'")
#user input
user = input(">> ")

#if user type w
if user=="w":

    #read to json file
    json_file_R = open("infro.json", "r")
    json_data = json.load(json_file_R)         

    #write to json file
    json_file_W = open("infro.json", "w")

    data = {}                              

    ID = ""
    
    while True:
        for d in detail:
            if d=="ID":
                print("\n")
                print("Next person don't get your detail")
                print("Frist create our ID\n")
                ID = input(f"{d} >> ")   #user give ID

            else:
                user_data = input(f"{d} >> ")
                new = {f"{d}":f"{user_data}"}
                data.update(new)         #add user data in data variable
        
        # if user want any changes in data
        print("\n")
        print("IF u want to change anything type \'y\' and press enter")
        ans = input(">> ")
        if ans == "y":
            continue
        else:
            break
        
    #user data
    person = {f"{ID}": data}       

    json_data.update(person)

    # add the user data in json file
    json.dump(json_data, json_file_W, indent=4)
    
    #close the write or read json file
    json_file_W.close()
    json_file_R.close()
    
#elif user type r
elif user=="r":
    
    #read to json file
    json_file = open("infro.json", "r")
    
    json_data = json.load(json_file)
    
    print("\n")
    print("Enter the I'd of person, who person detail u want")

    for i in range(3):  #user have tree die to enter correct I'd

        ans = input(" ID >> ") #user id

        # if id is correct
        if ans in json_data.keys():

            #person data , whom person data user want
            user_data = json_data[ans]

            #choice print 
            print("Choice : ", end="")
            for d in detail:print(d, end=", ")
            print(", ALL ")

            print("\n")
            print("What type data you want? :\" ")
            
            #user input
            user_need = input("Quik for q >> ")

            while True: #user have mutiples die

                #if user input is correct
                if user_need in detail:

                    print("\n")
                    print(f"{user_need} :-> {user_data[user_need]}")
                    break
                
                #elif user input is all
                elif user_need == "ALL":

                    print("\n")
                    for data in user_data:
                        print(f"{data} :-> {user_data[data]}")
                    break

                #elif user input is q
                elif user_need == "q":
                    print("YOU! Quick :> ")
                    break
            
                #else user input is incorrect
                else:
                    print("Enter plz!, rightly")
                    continue


            break
        
        #elif id isn't correct and user have die
        elif ans not in json_data.keys():
            print(f"you have {3-i+1} die")

        # elif id isn't correct and user didn't die
        elif ans not in json_data.keys() and i>=3:
            print(" YOU ARE! BLOCK :}")

#else type another thing
else:
    print("plz! enter proporly again.")



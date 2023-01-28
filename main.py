#       ____      ____      ___                 
#     //    ) ) //    ) ) //   ) ) 
#    //    / / //    / / //___/ /  
#   //    / / //    / / / __  (    
#  //    / / //    / / //    ) )   
# //____/ / //____/ / //____/ /    
# DictionaryDB
# A fun experiment by me to make a db using a dictionary
# imports
import random
import os
import functools
# consts/vars
db = {"":""}
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
logo = open("logo.txt","r").read()
# functions
def read_db(root_dir):
    # read database from folder structure
    dact = {}
    root_dir = root_dir.rstrip(os.sep)
    start = root_dir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(root_dir):
        folders = path[start:].split(os.sep)
        subdir = dact.fromkeys(files)
        parent = functools.reduce(dict.get, folders[:-1], dact)
        parent[folders[-1]] = subdir
    dact = dact["db"]
    for folder in dact:
        for file in dact[folder]:
            if dact[folder][file] == None:
                ffile = open("./db/"+folder+"/"+file)
                dact[folder][file] = ffile.read()
                ffile.close()
    return dact
def makeid():
    # generates the id to be used for database entries
    id = ""
    while id in db:
        for i in range(5):
            id += random.choice(letters)
    return id
def dbadd(id,attr={}):
    # easier to remember
    db[id] = attr
def dbaddui():
    # user interface for adding to the db
    dbtoadd = {}
    temp = input("enter name (blank for nothing): ")
    if temp != "":
        dbtoadd["name"] = temp
    temp = input("enter dn (blank for nothing): ")
    if temp != "":
        dbtoadd["dn"]=temp
    temp1 = input("Do you want to add any more fields? [y/n]: ")
    while True:
        if temp1.lower() == "y":
            temp2 = input("What is the name of the field to enter? [q to quit]: ")
            if temp2.lower() == "q":
                break
            temp = input("What is the value of the field to enter? [q to quit]: ")
            if temp.lower() == "q":
                break
            else:
                dbtoadd[temp2]=temp
        else:
            break
    dbadd(makeid(),dbtoadd)
def dbremui():
    global db
    temp = "a"
    while not temp in db or not temp == "q":
        temp = input("Enter the ID of the entry you wish to delete. [q to quit]: ")
    if temp.lower() == "q":
        return
    del db[temp]
def savetostruct():
    global db
    os.system("bash -c \"rm -r ./db/*\"")
    for item in db:
        if item != "":
            os.mkdir("db/"+item)
            for itemnested in db[item]:
                itemdata = open("db/"+item+"/"+itemnested, "w")
                itemdata.write(db[item][itemnested])
                itemdata.close()
    print("Saved!")
def mainui():
    # main user interface
    global db
    print(logo)
    result = input("choices:\n1. add to db\n2. delete from db\n3. save to disk\n4. load from disk\n5. show db\n6. quit\nchoose option[1-6]: ")
    try:
        match int(result):
            case 1:
                dbaddui()
            case 2:
                dbremui()
            case 3:
                savetostruct()
            case 4:
                db.update(read_db("./db/"))
                print("Loaded database.")
            case 5:
                print(db)
            case 6:
                print("quitting")
                exit(0)
            case other:
                print("not an option")

    except ValueError:
        print("not an option")
#dbadd(makeid(),{"name":"quandale dingle","age":"69","whatever else":"bingus"})
#dbadd(makeid(),{"name":"quandavious pringleton","age":"28","thibgf5":"roigujsodijvosdjf"})
# print(db)
# start main loop
while True:
    mainui()
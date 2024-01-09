# array name[max] where max is the upper limit of the number of elements in the array
names = ["Zhandos", "Eshan", "Sami", "Vicente", "Loran", "Bob", "Bob"]
soughtName = input("Enter name: ").capitalize()
# check list name for soughtName
found = False
for i in range(len(names)):
    if names[i] == soughtName:
        found = True
        print("Record number:", i+1)

if found == False:
    print("ERR: Not found")
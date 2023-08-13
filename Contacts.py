Contacts={"khawla":"777777777",
            "atrab":"777777111",
            "safa":"777777222",
            "manar":"777777333",}

print(" 1-View numbers\n 2-Add a number\n 3-Update a number\n 4-Delete a number\n 5-Delete all numbers\n")

allitems=Contacts.items()

def ViewContacts():
    print(f"{'Name':10}     {'Number':10} ")
    for phone_key, phone_value in Contacts.items():
        print('{0:10} ==> {1:10}'.format(phone_key,phone_value))
##################################################################
def AddContact():
    
    name=input("Enter the name")
    if name not in Contacts:
      num=input("Enter the number")
      Contacts.update({name:num})
      print("The number is added")
      ViewContacts()
    else:
        print("this name is exist")
##################################################################

def Update_numbers():
    name=input("Enter the name you want to update")
    if name in Contacts:
       new_num=input(f"Enter the new number for{name}")
       Contacts[name]=new_num
       ViewContacts()
    else:
        print("not found!")

##################################################################

def DeleteContact():
    name=input("Enter the name you want to delete")
    #del phone_list[name]
    if name in Contacts:
      print(Contacts.pop(name))
      print(f"{name} was deleted")
      ViewContacts()
    else:
      print("is not found")
 ##################################################################
     
def DeleteContacts():
    Contacts.clear()
    print(f"{Contacts} \n the list is empty")
  
##################################################################
    
user_choice=input("Chose a number:")

if user_choice =="1":
    ViewContacts()
elif user_choice =="2":
    AddContact()
elif user_choice =="3":
    Update_numbers()
elif user_choice =="4":
    DeleteContact()
elif user_choice =="5":
    DeleteContacts()
else:
    print("wrong choice!")
    
    


    





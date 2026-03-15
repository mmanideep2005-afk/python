contacts = {'manideep':9123456,'rahul':98765}  #empty contacts dictionary
def create_contact(name:str,mobile:int):
    if name not in contacts:
        contacts['name']=mobile
        return "contact saved"
    return "contact name already exists"
def update_contact(name:str,mobile:int):
    if name in contacts:
        contacts[name] = mobile
        return "contact updated"
    return 'contact already exists'
def remove_contact(name:str):
    if name in contacts:
        print(contacts.pop('name'))
        return 'contact removed'
    print(contacts)
def mobile_number(name:str):
    if name in contacts:
        print(contacts.get('name'))
    return 'mobile number returned'
def all_contacts():
    return contacts
if __name__=='__main__':
    print("select options like option 1) create contact \n 2)update contact \n 3)remove contact \n 4)mobile number \n 5)allcontacts")
    while True:
        choice= int(input("Enter your choice"))
        if choice == 1:
            print("your selected choice is 1. create contact number")
            name = input().strip()
            mobile = int(input())
            res = create_contact(name,mobile)
        elif choice==2:
            print("your selected choice is 2.update contact number.Update contact")
            name = input().strip()
            mobile = int(input())
            res = update_contact(name,mobile)
            print(res)
        elif choice == 3:
            print("your selected choice is 3. remove contact number. delete contact")
            name = input().strip()
            res = remove_contact(name)
            print(res)
        elif choice == 4:
            print("your selected choice is 4.display mobile number")
            name = input().strip()
            res = mobile_number(name)
            print(res)
        elif choice == 5:
            print("your selected choice is 5. display all contacts in dictionary")
            res = all_contacts()
            for name,mobile in res.items():
                print(f"{name} : {mobile}")
        elif choice == 6:
            exit()
        else:
            print("invalid choice")
'''
Write a python script to create an application like Truecaller where names and
numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
number and 2nd to add a new entry).
'''

class TrueCaller:
    def __init__(self) -> None:
        self.contact = {}
    
    def add_entry(self, name, number) -> None:
        self.contact[number] = name
    
    def fetch_name(self, number) -> str:
        return self.contact[number]

if __name__ == '__main__':
    app = TrueCaller()
    while True:
        option = input("Enter 1 to add contact, 2 to fetch number and 3 to exit: ")
        match option:
            case '1':
                contact = input("Enter name and mobile number using comma(',') : ").split(',')
                app.add_entry(contact[0], contact[1])
                # if len(contact) == 2 and contact[1].isnumeric() and contact[0].isalpha():
                #     app.add_entry(contact[0], contact[1])
                # elif len(contact) == 2 and contact[1].isalpha() and contact[0].isnumeric():
                #     app.add_entry(contact[1], contact[0])
                # else:
                #     print("Invalid input")
            case '2':
                number = input('Enter number : ')
                if number in app.contact:
                    print(app.fetch_name(number))
                else:
                    print("Number isn't available")
            case '3':
                exit()
            case _:
                print("Invalid option")
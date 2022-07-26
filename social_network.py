#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. <- Go back ")
    return input("Please Choose a number: ")


#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            a, b = input("Account Name, User Age :  ").split()
            
            
            ai_social_network.create_account()
            

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "5":    
                    break
                elif inner_menu_choice == "1":
                    
                    print('Your name is currently ' + a)
                    print('Your age is currently ' + b)
                    a == input('Enter new name : \n')
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                elif inner_menu_choice == "2":
                    p1 = Person(input("Confirm add friend? : "),1)
                    p1.add_friend()
                    break
                elif inner_menu_choice == "3":
                    print(p1.friendlist)
                    break
                elif inner_menu_choice == "4":
                    
                    y = Person(input('Who would you like to message? : '),1)    
                    #print('To ' + y + '!')
                    y.send_message()
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                    

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        

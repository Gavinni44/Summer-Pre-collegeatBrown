# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
from audioop import add


class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        print("Creating ...")
        pass


class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.messages = []


    def add_friend(self):
        f = input('Enter friend name: \n')
        self.friendlist.append(f)
        print(f'Updated Friends List{self.friendlist}')
        #implement adding friend. Hint add to self.friendlist
        #pass

    def send_message(self):
        g = input('Enter message : ')
        self.messages.append(g)
        print(self.messages)
        #implement sending message to friend here
        #friend_object.messages.append(message)
        pass

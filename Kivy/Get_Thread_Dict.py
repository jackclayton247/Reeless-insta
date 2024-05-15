from instagrapi import Client
from pandas import DataFrame
from collections import OrderedDict

ACCOUNT_USERNAME = "insta_api_tester1"
ACCOUNT_PASSWORD = "PooPoo987654321"

cl = Client()

#_______________________login_______________________
try:
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, verification_code="")
except:
    print("username/password is incorrect or an error occured")
    exit()

#_______________________create dictionary_______________________
a_dictionary_of_threads = {}
#_______________________get thread data_______________________
thread_data = cl.direct_threads()
for i, direct_thread in enumerate(thread_data):
    ordered_dict = OrderedDict(direct_thread.__dict__)
    ordered_dict.move_to_end("users", False) #moves the user to the start of the dictionary
    current_key = []
    for x, attribute in enumerate(ordered_dict):
        if attribute == "users":
            current_key = tuple(ordered_dict[attribute])
            a_dictionary_of_threads[current_key] = []
        else:
            a_dictionary_of_threads[current_key].append(ordered_dict[attribute])
#_______________________test_______________________
for i, item in enumerate(a_dictionary_of_threads):
    if i == 0:
        print(type(item[0].__dict__))
        print(item[0])
                
        

cl.logout()
#-------------------------------------------insta api-------------------------------------------
from instagrapi import Client
# ACCOUNT_USERNAME = "insta_api_tester2"
# ACCOUNT_PASSWORD = "PooPoo123456789"

def logging_in():
    ACCOUNT_USERNAME = username
    ACCOUNT_PASSWORD = password
    cl = Client()
    #_______________________login_______________________
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, verification_code="")    
    #_______________________create dictionary_______________________
    global a_dictionary_of_threads
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
    cl.logout()
    #root.manager.current = "ThreadsPage"
    #root.manager.transition.direction = "left"
    #-------------------------------------------insta api-------------------------------------------
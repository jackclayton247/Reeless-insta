from instagrapi import Client
from pandas import DataFrame

ACCOUNT_USERNAME = "insta_api_tester1"
ACCOUNT_PASSWORD = "PooPoo987654321"

#jack.clayton.15 thread_id=340282366841710301244276198747843586623
cl = Client()
#cl.set_proxy()
try:
    cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, verification_code="")
except:
    print("username/password is incorrect or an error occured")
    exit()
threads = cl.direct_threads() #list of threads' data
thread_dict = {} #dictionary to hold thread data as it is currently just attributes
for thread in threads:
    temp = [] #temp list for profile data
    for info in thread.__dict__["users"][0].__dict__:
        temp += [thread.__dict__["users"][0].__dict__[info]] #adds each attribute to a list
    thread_dict[thread.__dict__["id"]] =  temp #forms the dictionary 
    print(thread_dict) 
'''
messages = cl.direct_messages(thread_id = 340282366841710301244276198747843586623)
message_details = []
for message in messages:
    #print(type(message))
    #print(message.__dict__)
    temp = []
    for item in message.__dict__:
        if item not in ["id", "user_id", "thread_id", "is_shh_mode", 'reel_share', 'story_share', 'animated_media','media_share','felix_share','xma_share','clip','placeholder']:
            if item == "type" and message.__dict__[item] not in ["text"]:
                pass
            else:
                temp.append(message.__dict__[item])
    if temp[1] == "text":
        message_details.append(temp)
for poo in message_details:
    print(type(poo[2]))
    print("-----------------------------")
'''           
                
print("------------------")
#cl.direct_send(text="i have sent this using python 2", thread_ids=[340282366841710301244259555778673739564], send_attribute="message_button")
#user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
#print(user_id)
print("logged in")
cl.logout()

#{'timestamp''item_type''is_sent_by_viewer''reactions''text''reply''link','media','visual_media'}
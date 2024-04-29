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

# messages = cl.direct_messages(thread_id = 340282366841710301244276198747843586623)
# for message in messages:
#     print(type(message))
#     print("------------------")
#cl.direct_send(text="i have sent this using python 2", thread_ids=[340282366841710301244259555778673739564], send_attribute="message_button")
#user_id = cl.user_id_from_username(ACCOUNT_USERNAME)
#print(user_id)
print("logged in")
cl.logout()

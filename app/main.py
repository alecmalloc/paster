# imports
from datetime import datetime
import pyperclip as ppc
import pymongo
import time
import os

# rename secrets_template to secrets on first boot and import mongo uri
if os.path.isfile("secrets_template.py"):
    os.rename("secrets_template.py", "secrets.py")
from secrets import mongo_uri

# mongo db inits
uri = mongo_uri
client = pymongo.MongoClient(uri, server_api = pymongo.server_api.ServerApi('1'))
mydb = client["Cluster0"]
mycol = mydb["clips"]

# global variables
sleep = 3 # set this to any value you like. less time means faster sync but more resource use. just monitor usage data and see whats best for you

# send contents of clipboard to database
def databasePaste():
    try:
        new_clip = {"date": f"{datetime.now()}", "contents": f"{ppc.paste()}"}
        x = mycol.insert_one(new_clip)
        print(x.inserted_id)
    except Exception as e:
        print(e)

# get contents of clipboard from database
def databaseCopy():
    try:
        x = mycol.find_one(sort=[("_id", pymongo.DESCENDING)])
        ppc.copy(x["contents"])
    except Exception as e:
        print(e)

# check if local clipboard is different from database clipboard
def isLocalSame():
    try:
        x = mycol.find_one(sort=[("_id", pymongo.DESCENDING)])
        database_contents = x["contents"]
        local_contents = ppc.paste()
        if (local_contents == database_contents):
            return True
        else:
            return False
    except Exception as e:
        print(e)

def isLocalinDatabase():
    try:
        x = mycol.find(sort=[("_id", pymongo.DESCENDING)])
        second_to_last_doc = x[1]
        database_contents = second_to_last_doc["contents"]
        local_contents = ppc.paste()
        if local_contents == database_contents:
            return True
        else:
            return False
    except Exception as e:
        print(e)


def main():
    print("initializing connection with database")
    while True:
        if isLocalSame() is False:
            if isLocalinDatabase() is True:
                databaseCopy()
                print("<----------- recieved database clipboard")
            else:
                databasePaste()
                print("-----------> sent local clipboard to database")
        else:
            print(f"checked -- no diff -- sleeping {sleep}")
            time.sleep(sleep)

if __name__ == "__main__":
    main()

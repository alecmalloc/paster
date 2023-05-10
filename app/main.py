# imports
from secrets import mongo_user, mongo_pass, mongo_addr
from datetime import datetime
import pyperclip as ppc
import pymongo
import time

# mongo db inits
uri = "mongodb+srv://" + mongo_user + ":" + mongo_pass + "@" + mongo_addr
client = pymongo.MongoClient(uri, server_api = pymongo.server_api.ServerApi('1'))
mydb = client["Cluster0"]
mycol = mydb["clips"]

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
        query = {"contents": ppc.paste()}
        count = mycol.count_documents(query)
        print(count)
        if (count > 0):
            return True
        else:
            return False
    except Exception as e:
        print(e)

def main():
    print("boot")
    while True:
        if isLocalSame() is False:
            if isLocalinDatabase() is True:
                databaseCopy()
                print("recieved database clipboard")
            else:
                databasePaste()
                print("sent local clipboard to database")
        time.sleep(6)
        print("slept 6")

if __name__ == "__main__":
    main()
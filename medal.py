import requests
import datetime
import os
import time
import sys

def post_request(s_id,p_id,api_key):
    url = "http://api.steampowered.com/ITFPromos_440/GrantItem/v0001/"
    parameters = {"steamID":s_id,"promoID":p_id,"key":api_key} 
    r = requests.post(url,data=parameters)
    return r.json()

def write_info(file,api,filename,promoid,time):
    time = now.strftime("%d/%m/%Y %H:%M:%S\n")
    file.write("Execution time: %s"%time)
    file.write("File: %s\n"%filename)
    file.write("API Key: %s\n"%api)
    file.write("Promo ID: %d\n\n"%promoid)
    return

###########MAIN###############

again = "yes"
skipped = []
while (again == "yes"):
    now = datetime.datetime.now()
    file_name = now.strftime("%d_%m_%Y_%H_%M_%S.txt")
    file_successful = open("success_"+file_name,"w")
    file_fail = open("fail_"+file_name,"w")

    correct = "no"
    while (correct == "no"):
        apikey = input("Put your API key: ")
        while True:
            try:
                file_name2 = input("File name: (e.g., medals.txt ): ")
                file_read = open(file_name2,"r")
                break
            except:
                print("Couldn't find such file")
            
        while True:
            try:
                promoid = int(input("PromodID: "))
                break
            except:
                print("PromoID does not accept characters. Are you sure you typed it right?")
            
        print("Double check your details before continuing:\n---------------")
        print("Api key: %s"%apikey)
        print("File name: %s"%file_name2)
        print("PromodID: %d"%promoid)
        print("---------------")
        while True:
            correct = input("Are your details correct? (yes/no): ")
            if (correct == "yes" or correct == "no"):
                break

    print("Check the content for file: %s"%file_name2)
    time.sleep(1)
    for line in file_read:
        line = line.strip()
        print(line)
    file_read.seek(0)
    final_decision = input("Are you sure you want to continue? (yes/no): ")
    if (final_decision == "no"):
        sys.exit()
        
    write_info(file_successful,apikey,file_name2,promoid,now)
    write_info(file_fail,apikey,file_name2,promoid,now)

    successful = 0
    fail = 0
    
    for steamid in file_read:
        steamid = steamid.strip()
        try:
            steamid = int(steamid)
            request = post_request(steamid,promoid,apikey)
            status = request["result"]["status"]
            if (status == 1):
                print("Success. SteamID: %d"%steamid)
                successful += 1
                file_successful.write(str(steamid)+"\n")
            else:
                print("Failed to deliver. SteamID: %d"%steamid)
                fail += 1
                file_fail.write(str(steamid)+"\n")
                file_failt.write("\n"+str(request)+"\n")
        except:
            fail += 1
            print("Fail. Skipped: %s. Not valid."%steamid)
            skipped.append(steamid)



    file_successful.write("Successful attempts: "+str(successful))
    file_fail.write("Failed attempts: "+str(fail)+"\n")
    if (skipped):
        file_fail.write("Skipped lines:\n")
        for el in skipped:
            file_fail.write(str(el)+"\n")

    file_fail.close()
    file_successful.close()
    file_read.close()
    if (fail == 0):
        os.remove("fail_"+file_name)
    while True:
        again = input("Send more? (yes/no)?: ")
        if (again == "yes" or again == "no"):
                break
    print("---------------")

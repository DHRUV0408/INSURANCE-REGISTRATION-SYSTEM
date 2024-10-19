import random
import pymongo 
l = 1
while l:
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["DHRUV_RATHEE"]
    collection = db["Insurance_Details"]
    
    num = int(input('ENTER 1 FOR INSURANCE OTHERWISE 0 : '))
    i = 0
    while i <= num-1:
        if num==0:
            break  
        name = (input("ENTER YOUR NAME  : "))
        print("WELCOME", name)
        phone = int(input("ENTER YOUR PHONE NUMBER. : "))
        if phone <= 9999999999 and phone >= 1000000000:
            print("Name : ",name)
            print("Phone No. : ",(phone))
        else:
            print("WRONGE PHONE NUMBER")
            continue
        age = int(input("ENTER YOUR AGE : "))
        if age >= 18 and age <= 60:
            print("------WELCOME",name,"------")
            print("------YOUR PROFILE------")
            print("Name : ",name)
            print("Phone No. : ",phone)
            print("Age : ",age)
            print("YOU ARE PERFECT FOR INSURANCE ")
        else:
            print("YOU ARE NOT PERFECT FOR INSURANCE")
            break
        
        print("OTP GENERATING SECTION")
        a = random.randint(1000,9999)
        print("YOUR OTP IS : ",a)
        otp = int(input("ENTER YOUR OTP : "))
        if a==otp:
            print("YOUR REQUEST WILL ACCEPT IN THREE DAYS")
        else:
            print("YOUR OTP IS WRONGE")
            
        list = [{
            'Name' : name,
            'Phone no.': phone,
            'Age' : age,
            'OTP' : otp
        }]
        i+=1
    
    collection.insert_many(list)
    nul = int(input("PRESS 1 FOR INSURANCE TO ANOTHER PERSON OTHERWISE PRESS 0 : "))
    if nul != 1:
        print("----THANK_YOU----")
        break
    l = l + nul
       
       
        
       
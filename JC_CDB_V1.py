import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import datetime 

while True:
    option = input ("Welcome to JC consulting customer database, please enter login: ")
    if (option.lower() == "josh" ):
        break
    elif (option.lower() == "dawson" ):
        break
    else:
        print ("Wrong Username")

print ("Welcome",option.upper())
print ("Database is now loading....")

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("JC_db").sheet1

while True:
    
    info = """
Here is a list of the functions I can help you with:
    -Add customer
    
    -Hosting renewal
    
    -Customer information
    
    -Quit"""
    print (info)

    
    request = input ("what can I do for you: ")
    
    if (request.lower() == "add customer"):
        print ("sorry this function is not available due to development but will be available soon")
        
    elif (request.lower() == "hosting renewal"):
       
        tday = datetime.date.today()
        print ("Today's date is:", tday)
        print ("Now checking the data base for upcoming renewals......")
        
        total_dates = 7 
        counter = 0 
        for i in range(2,total_dates+1):
            counter = i
            names = sheet.cell(counter,1).value
            sheet_dates = sheet.cell(counter,2).value
            dates = datetime.datetime.strptime(sheet_dates, "%Y/%m/%d")
            real_dates = dates.date()
            date_difference = real_dates - tday 
            if (date_difference.days <= 7):
                print (real_dates, names)      

    elif (request.lower() == "customer information"):
        customer_name = input ("Please enter a customer's name to see their contact information: ")
        
        total_customers = 7
        counter1 = 0
        for n in range (2, total_customers+1):
            counter1 = n
            sheet_name = sheet.cell(counter1,1).value
            if (customer_name.lower() == sheet_name.lower()):
                c_email = sheet.cell(counter1,3).value
                c_phone = sheet.cell(counter1,4).value
                print ("Customer name:",sheet_name.upper())
                print ("Customer email:", c_email)
                print ("Customer phonenumber:",c_phone)
        
        
        

    elif (request.lower() == "quit"):
        print ("Thank you for using JC consulting customer database")
        break
    
    else:
        print("Sorry but I do not understand your request please try again or enter Quit to stop the program.")
        
    



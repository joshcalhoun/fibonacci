import gspread, pprint, datetime
from oauth2client.service_account import ServiceAccountCredentials
from customer import Customer

users = ['josh','dawson']
abilities = ['add customer','hosting renewal','customer info','quit']
appname = "JCDB"
username = ''
customer_list = []

def list_options():
    print ('Here\'s your list of options.')
    for ability in abilities:
        print("-" + ability)
    request = input("What would you like to do?: ")
    
def apology(name):
    print(f'Sorry {username}'+' can\'t do that yet :(.')

def startUp():
    i = 1
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("JC_db").sheet1
    
    while (i < int(sheet.row_count)):
        i = i + 1
        if (sheet.row_values(i) ==  ''):
            break
        values_list = sheet.row_values(i)
        customer = Customer(values_list[0])
        customer.renewal_date = values_list[1]
        customer.email = values_list[2]
        customer.phone = values_list[3]
        if (customer.name == ""):
            break
        customer_list.append(customer)
    
print(f"Welcome to {appname}!\n")
while True:
    username = input ("Username please: ")
    if (username in users):
        break
    else:
        print ("Wrong Username")
print(f"Welcome {username}!")
print("Database is now loading....")

startUp()


    

while True:
    print('What would you like to do?')
    request = input('Type \'o\' for more options: ' )

        
    if (request.lower() == 'o'):
        list_options()
        
    elif (request.lower() == "add customer"):
        apology(username)

    elif (request.lower() == "hosting renewal"):

        tday = datetime.date.today()
        print ("Today's date is:", tday)
        print ("Now checking the data base for upcoming renewals......")

        total_dates = 7
        counter = 0
        #for i in range(1, sheet.row_count():
                       
        values_list = sheet.row_values(1)

        for i in range(2,total_dates+1):
            counter = i
            names = sheet.cell(counter,1).value
            sheet_dates = sheet.cell(counter,2).value
            dates = datetime.datetime.strptime(sheet_dates, "%Y/%m/%d")
            real_dates = dates.date()
            date_difference = real_dates - tday
            if (date_difference.days <= 7):
                print (real_dates, names)

    elif (request.lower() == "customer info"):
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
        print ("Thank you for using JC consulting customer database!")
        break

    else:
        apology(username)
        
    choice = input('Type Q to quit, and any other key to do something else: ' )
    if (choice.lower() == 'q'):
        break
        


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
        request =  input('What would you like to do?')

    elif (request.lower() == "add customer"):
        apology(username)

    elif ("host" in request.lower()):

        tday = datetime.date.today()

        for customer in customer_list:
            date = datetime.datetime.strptime(customer.renewal_date, "%m/%d/%Y")
            if (date < datetime.datetime.now()):
                print(str(date.strftime('%B, %d, %Y')) + " " + customer.name)


    elif (request.lower() == "customer info"):
        customer_name = input ("Please enter a customer's name to see their contact information: ")
        for customer in customer_list:
            if(customer_name.lower() == customer.name.lower()):
                print(f'''Name: {customer.name}
Email: {customer.email}
Phone: {customer.phone}
Renewal Date: {customer.renewal_date}''')

    elif (request.lower() == "quit"):
        print ("Thank you for using JC consulting customer database!")
        break

    else:
        apology(username)
        
    choice = input('Type Q to quit, and any other key to do something else: ' )
    if (choice.lower() == 'q'):
        break
        


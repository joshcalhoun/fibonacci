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
    print(f'Sorry {name}'+' can\'t do that yet.')

def confirmation(name):
    print('Completed!')

def addCell(value, sheet):
    if (value == ""):
        pass
    else:
        pass

def allWordsCheck(words, string):
    result = True
    for word in words:
        result = ((word in string)and result)
    return result

def startUp(sheet):
    i = 1
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

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("JC_db").sheet1
    
startUp(sheet)

while True:
    print('What would you like to do?')
    request = input('Type \'o\' for more options: ' )
    r = request.lower()
    if (r == 'o'):
        list_options()
        request =  input('What would you like to do?')

    elif (allWordsCheck(["add","customer"],r)):
        new_values = ["Name","Renewal Date(M/D/Y)","Email","Phone"]
        for x in range(len(new_values)):
            value = input(new_values[x] + ': ')
            new_values[x] = value
        customer = Customer(new_values[0])
        customer.email = new_values[2]
        customer.phone = new_values[3]
        customer.renewal_date = new_values[1]
        customer_list.append(customer)
        print('Hold this can take up to a minute to complete...')
        sheet.insert_row(new_values, len(customer_list) + 1)
        confirmation(username)



    elif (allWordsCheck(["host"],r)):

        tday = datetime.date.today()

        for customer in customer_list:
            date = datetime.datetime.strptime(customer.renewal_date, "%m/%d/%Y")
            if (date < datetime.datetime.now()):
                print(str(date.strftime('%B, %d, %Y')) + " " + customer.name)
        confirmation(username)


    elif (allWordsCheck(["info","customer"],r)):
        customer_name = input ("Please enter a customer's name to see their contact information: ")
        for customer in customer_list:
            if(customer_name.lower() in customer.name.lower()):
                print(f'''Name: {customer.name}
Email: {customer.email}
Phone: {customer.phone}
Renewal Date: {customer.renewal_date}''')

        confirmation(username)


    elif (allWordsCheck(["quit","stop"],r)):
        confirmation(username)
        break

    else:
        apology(username)
        
    choice = input('Enter to continue or Q to quit: ' )
    if (choice.lower() == 'q'):
        break
        


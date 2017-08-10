

contacts = {
	'Dawson':['610-716-7668','sturgilldawson@gmail.com'],
	'Chad':  ['561-329-9821','sturg6@comcast.net'],
	'Beth':  ['610-716-7668','sturg4@comcast.net']}
while True:
    
    request = input("Which contact do you want?")
    second_request = input("Phone or Email?")
    
    if (second_request.lower() == "phone"):
        print(contacts[str(request)][0])
        
    elif (second_request.lower() == "email"):
        print(contacts[str(request)][1])
        
    option = input("Quit or continue")
    if (option == "quit"):
        break
    

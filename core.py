import re, nltk

def greet():
    input = ("Hello, what would you like to do?")
    return input
    
def contains(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def grant(request):
    verb,noun = getRequest(request)
    print(verb)
    if verb.lower() == "turn":
        print("Yes I can turn on the %s" % noun)
    else:
        print('Don\'t know how to do that yet')
    
def processRequest(text):
    tokenizedText = nltk.word_tokenize(text)
    print(nltk.pos_tag(tokenizedText))
    return nltk.pos_tag(tokenizedText)

def getRequest(text):
    for items in processRequest(text):
        i = items[1]
        if (i == 'VB' or i == 'VBP'):
            verb = str(items[0]).lower()
        if (i == 'NN'):
            noun = str(items[0]).lower()
    return verb, noun

#password generator
import random
import string

def get_password(l):
    special = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789" 
    password = ""
    if l == "":    
        password = random.choices(special + string.ascii_letters, k=15)
        return "".join(password)
    for i in l:
        case = random.randint(0,1)
        if not case:
            password += i.upper()
        else:
            password += i.lower()
        password = password.replace(" ",random.choice(special),1)
    return password

if __name__ == "__main__":
    print("Welcome to random Password Generator")
    name = input("What's your name? ")
    response = None
    while response != "Y" and response != "N":
        response = input("Do you want to generate a personalised password?(Y/N) : ").upper()
        if response not in "Y" and response not in "N":
            print("Please enter correct response only (Y) or (N) : ")
    
    l = ""
    if response == "Y":
        while True:
            keyword = input("Please enter the keyword for recommendation or press ENTER to exit! ")
            if keyword == "":
                print("")
                break
            l+=keyword+" "
    
    password = get_password(l)
    print("\nPASSWORD = "+password+"\n")

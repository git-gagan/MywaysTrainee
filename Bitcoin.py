import requests
import datetime

def crypto_profit():
    print("\nPlease enter the latest date on which you invested in bitcoin : ")
    year, month, date = "","",""
    while len(year)!=4 or len(month)!=2 or len(date)!=2:
        print("\nPlease Enter the complete date in correct format only!")
        year, month, date = input("Year(20xx) : "), input("Month(xx) : "), input("Date(xx) : ")
    start = year+"-"+month+"-"+date
    print("\nYou invested on : ",start)
    current = datetime.datetime.now()
    today = str(current.year)+"-"+str(current.month)+"-"+str(current.day)
    print("And today its : ",today+"\n")
    data = requests.get("https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1459987200&period2=1617753600&interval=1d&events=history&includeAdjustedClose=true").text.splitlines()
    for i in data:
        if start in i:
            close_that_day = i.split(",")[4]
            return float(data[-1].split(",")[4]) - float(close_that_day)
    return "\nNot in records, so Profit : "+data[-1].split(",")[4]

if __name__ == "__main__":
    print("\n---Welcome to Crypto Stocks Checker---")
    name = input("What's your name? ")
    response = None
    while response != "Y" and response != "N":
        response = input(f"Have you invested in bitcoin {name}? (Y) or (N)? ").upper()
        if response != "Y" and response != "N":
            print("Please enter a valid response only!")
    if response == "N":
        print("Since you haven't invested in bitcoin, your current profit is 0$\n")
    else:
        result = crypto_profit()
        print("Total profit within the time frame : ",result)
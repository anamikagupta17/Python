class BalanceException(Exception):
    pass  # we can write some code  here 

def check_balance(): # minmum balance should be 200
    money=1000
    withdraw=int(input("Enter Amount :"))
    try: 
        balance=money-withdraw
        if(balance<=200):
            raise BalanceException('Insufficient Balance')
    except BalanceException as be:
        print(be)  

check_balance()

# Import Functions from function.py
from function import *

choose = 0
while(choose != 2):
    print("====================================")
    print("=====Jonathan's Vending Machine=====")
    print("====================================")
    print("1. Buy Drinks")
    print("2. Exit")
    print("3. Check Stock")
    print("4. Restock (admin only)")
    choose = int(input("your choice => "))
    if(choose == 1):
        buy()
    elif(choose ==3):
        CheckStock()
    elif(choose==4):
        password = input("Input Password : ")
        if(password == "Admin"):
            restock()
        else:
            print("password is incorrect , please try again")

print("=====THANK YOU=====")
    



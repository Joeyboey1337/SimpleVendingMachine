# Import Functions from function.py
from function import *

choose = "0"
while(choose != "2"):
    print("====================================")
    print("=====Jonathan's Vending Machine=====")
    print("====================================")
    print("1. Buy Drinks")
    print("2. Exit")
    print("3. Check Stock (admin only)")
    print("4. Restock (admin only)")
    choose = int(input("your choice => "))
    if(choose == 1):
        buy()
    



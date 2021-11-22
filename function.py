#global variable
drinks = ["COCA COLA","FANTA","SPRITE","POCARISWEAT","AQUA"]
quantities = [10,10,10,10,10]
price = [8000,7500,7000,9000,5000] #in IDR
orders =[]
order_qtc=[]
order_price=[]

def CheckStock():
    l= len(drinks)
    print("Today we have :")
    for x in range(l):
        print(x+1,".",drinks[x]," : @IDR",price[x]," => ",quantities[x], "bottles available")

def buy():
    cont = True
    x=0
    while(cont):
        CheckStock()
        print("Input your order number (number only): ")
        order = int(input("=> "))
        n = order-1
        product = orders.insert(x,drinks[n])
        print("How Much ? (number only) :")
        qtc = int(input("=> "))
        if(quantities[n]< 1):
            print("Sorry our stock is not enough for your order")
            product = drinks[n]
            orders.remove(product)
        else:
            order_price.insert(x,price[n])
            quantities[n]-=qtc
        order_qtc.insert(x,qtc)

        print("Any thing else?(yes/no):")
        YN = input("=> ")
        if(YN.casefold() == "yes"):
            cont = True
            x+=1
        elif(YN.casefold() == "no"):
            print("Your Orders: ")
            l = len(orders)
            total = 0
            for j in range(l):
                print(j+1,".",orders[j]," : @IDR",order_price[j]," x ",order_qtc[j], "= IDR",order_price[j]*order_qtc[j])
                total += order_price[j]*order_qtc[j]
            print("TOTAL = IDR", total)
            break
        else:
            print("your input isn't valid , restart your order")
            buy()
buy()

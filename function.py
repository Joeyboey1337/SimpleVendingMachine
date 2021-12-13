from Product import *;
#product list:
drink1 = Product('Coca Cola',8000,10)
drink2 = Product('Fanta',5000,10)
drink3 = Product('Sprite',6000,10)
drink4 = Product('Milo',9000,10)
drink5 = Product('Pocari Sweat',9500,10)
drink6 = Product('Aqua',7000,10)
drinks =[drink1,drink2,drink3,drink4,drink5,drink6]


def CheckStock():
    print("Today we have :")
    index = 1
    for drink in drinks:
            print(str(index),drink.info())
            index+=1

def buy():
    orders =[]
    order_qtc=[]
    cont = True
    x=0
    while(cont):
        CheckStock()
        order = int(input("Input your order number (number only): "))
        order-=1
        orders.insert(x,drinks[order])
        qtc = int(input("How Much ? (number only) : "))
        if(drinks[order].qtc< 1 or drinks[order].qtc< qtc):
            print("Sorry our stock is not enough for your order")
            product = drinks[order]
            orders.remove(product)
        else:
            drinks[order].qtc-=qtc
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
                format_drinks = f"{orders[j].name:<15}"
                format_price  = f"RP.{orders[j].price:,}"
                format_qtc    = f"x {order_qtc[j]:>3}"
                format_result = f"= Rp{orders[j].price*order_qtc[j]:,}"
                print("||",j+1,".",format_drinks,"\t",format_price,format_qtc,format_result,"||")
                total += orders[j].price*order_qtc[j]
                format_total = f"TOTAL = Rp.{total:,}"
            print(format_total)
            pay = int(input("Your Money:Rp"))
            change = pay-total
            format_change = f"CHANGE = Rp.{change:,}"
            print(format_change)
            break
        else:
            print("your input isn't valid , restart your order")
            buy()

def restock():
    print("1. Add new products")
    print("2. Restock existing products")
    choose = int(input("=> "))
    if(choose == 1):
        l = len(drinks)
        while(True):
            name = input("Input Product's Name : ")
            Idr = int(input("Input Product's Price (IDR) :"))
            qtc = int(input("Input Product's Quantity (number only):"))
            drink = Product(name,Idr,qtc)
            drinks.insert(l,drink)
            CheckStock()
            cont = input("Do you want add product again ?(yes or no) :")
            if(cont.casefold()=="yes"):
                l+=1
                continue
            elif(cont.casefold()=="no"):
                print("=====THANKYOU=====")
                break

    elif(choose == 2):
        cont = True
        while(cont):
            CheckStock()
            n = int(input("Product number you want to restock : "))
            qtc = int(input("How much ? (number only): "))
            drinks[n-1].qtc += qtc
            print("Processing.....")
            print("Done.....")
            CheckStock()
            x = input("restock again ? (yes or no) => ")
            if(x.casefold() == "yes"):
                continue
            elif(x.casefold()):
                print("======THANKYOU=====")
                break

    
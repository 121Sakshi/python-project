# Define the menu of restaurant

menu={
    'Pizza':40,
    'Pasat':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80
}
# Greet
print("Welcome to PYTHON Restaurant")
print("Pizza: Rs40 \nPasat: Rs50 \nBurger: Rs60 \nSalad: Rs70 \nCoffee: Rs80")

order_total=0
# 80+50=130

item_1=input("Enter the name of itme you want to order =")
if item_1 in menu:
    order_total += menu[item_1] # 0+50
    print(f" Your item{item_1} has been added to yor order")

else:
    print(f"Ordered item {item_1} is not avaialable yet!")

another_order = input("Do you to add another itme?(Yes/No)")
if another_order=="Yes":
    item_2 = input("Enter the name of second itme =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Itme {item_2} has been add to order")
    else:
        print(f"Ordered item {item_2} is not avaialable!")
print(f"The totle amount of items to pay is {order_total} ")
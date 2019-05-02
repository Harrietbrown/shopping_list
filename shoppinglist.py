def main():
    endprogram = False
    with open("shoppinglist.txt", mode="r") as my_file:
        shop=my_file.read().splitlines()

    while endprogram == False:
        print("Welcome to your shopping list")
        print("this program can add items to your shopping list, sort those items into alphabetical order, display the list, and delete items off of the list")
        print("")
        print("0. Exit program")
        print("1. Display shopping list")
        print("2. Add to shopping list")
        print("3. Delete an Item from your list")
        print("4. Sort the list in alphabetical order")
        print("")
        job=input("Please enter command: ")
        print("\n \n ---------------------------------------------------------------------------------------- \n \n")
        if job == "1":
            display(shop)
            input("Enter any key to return to main menu.")
        elif job == "2":
            shop = addto(shop)
        elif job == "3":
            shop = delete(shop)
        elif job == "4":
            shop.sort()
            display(shop)
        elif job == "0":
            endprogram = True
        else:
            print("Invalid input, please try again. \n \n \n")
    with open("shoppinglist.txt", mode="w") as my_file:
        for item in shop:
            my_file.write(item +"\n")


def display(shop):
    for i in range(len(shop)):
        print("{0}. {1:<3} {2:<10}".format(i+1,"",shop[i]))
    return

def addto(shop):
    backtomenu = False
    while backtomenu == False:
        print("State item to be added to shopping list. Enter 0 to return to main menu")
        newitem = input()
        if newitem == "0":
            backtomenu = True
        else:
            shop.append(newitem)
    return shop


def delete(shop):
    backtomenu = False
    while backtomenu == False:
        display(shop)
        job = input("What item should be deleted? Enter 0 to exit. ")
        if job == "0":
            exit = True
        else:
            for i in range(len(shop)):
                if str(i+1)==job:
                    print("%s removed from your shopping list" %shop[i])
                    shop.pop(i)
    return shop


main()

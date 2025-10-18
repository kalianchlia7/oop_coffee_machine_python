from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#1. Print report (see all resources)

is_on=True

money_machine = MoneyMachine()
#need to create an object from money machine class and store it in a variable first
coffee_maker = CoffeeMaker()
menu = Menu()

#2. Check resources sufficient

while is_on:
    options = menu.get_items()  #saves str of all optinos into variable options
    choice = input(f"Wjat woul dyou like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report() #will print otu resources
        money_machine.report()  #will print current amount of money in machine
    else:
        drink = menu.find_drink(choice) #takes input str
        #converting str 'choice' to item in menu
        if coffee_maker.is_resource_sufficient(drink):

#3. Process coins + #4. Check transaction successful

            if money_machine.make_payment(drink.cost): #boolean  
                    #passing in cost of drink customer ordered
                    #drink is a menu item with attribute cost
                    #LOOK inside money machine code, has method to process coins and total sum

#5. Make Coffee

                coffee_maker.make_coffee(drink)
                #expects menu item as input parameter

        

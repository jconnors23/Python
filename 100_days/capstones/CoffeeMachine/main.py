from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    ordering = True
    while ordering:
        want = input("Would you like to order? (y | n)\n")
        if want != 'y':
            ordering = False
            continue
        menu = Menu()
        coffee_maker = CoffeeMaker()
        money_machine = MoneyMachine()
        choice = input(f"What would you like {Menu.get_items(menu)}?\n")
        if choice == 'off':
            print("System exiting.\n")
            exit()
        elif choice == 'report':
            print(CoffeeMaker.report(coffee_maker))
            print(MoneyMachine.report(money_machine))
            continue
        else:
            drink_selection = Menu.find_drink(menu, choice)
            if drink_selection == "Sorry that item is not available.":
                print("Sorry that item is not available.")
                continue
            else:
                can_make = CoffeeMaker.is_resource_sufficient(coffee_maker, drink_selection)
                if not can_make:
                    continue
                else:
                    successful_payment = MoneyMachine.make_payment(money_machine, drink_selection.cost)
                    if successful_payment:
                        CoffeeMaker.make_coffee(coffee_maker, drink_selection)
                        continue
                    else:
                        continue
    print("Have a nice day.")
    exit()


main()

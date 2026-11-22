class CoffeeMachine:
    RECIPES = {
        "1": {"water": 250, "milk": 0, "beans": 16, "cost": 4},
        "2": {"water": 350, "milk": 75, "beans": 20, "cost": 7},
        "3": {"water": 200, "milk": 100, "beans": 12, "cost": 6},
    }

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "action"

    def print_state(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def prompt(self):
        prompts = {
            "action": "Write action (buy, fill, take, remaining, exit):",
            "buy": "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:",
            "fill_water": "Write how many ml of water you want to add:",
            "fill_milk": "Write how many ml of milk you want to add:",
            "fill_beans": "Write how many grams of coffee beans you want to add:",
            "fill_cups": "Write how many disposable cups of coffee you want to add:",
        }
        print(prompts[self.state])

    def make_coffee(self, recipe):
        if self.water < recipe["water"]:
            print("Sorry, not enough water!")
            return
        if self.milk < recipe["milk"]:
            print("Sorry, not enough milk!")
            return
        if self.beans < recipe["beans"]:
            print("Sorry, not enough coffee beans!")
            return
        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return

        print("I have enough resources, making you a coffee!")
        self.water -= recipe["water"]
        self.milk -= recipe["milk"]
        self.beans -= recipe["beans"]
        self.cups -= 1
        self.money += recipe["cost"]

    def handle_input(self, user_input):
        cmd = user_input.strip()
        if self.state == "action":
            if cmd == "buy":
                self.state = "buy"
            elif cmd == "fill":
                self.state = "fill_water"
            elif cmd == "take":
                print(f"I gave you {self.money}")
                self.money = 0
            elif cmd == "remaining":
                self.print_state()
            elif cmd == "exit":
                return False
        elif self.state == "buy":
            if cmd in self.RECIPES:
                self.make_coffee(self.RECIPES[cmd])
            self.state = "action"
        elif self.state == "fill_water":
            self.water += int(cmd)
            self.state = "fill_milk"
        elif self.state == "fill_milk":
            self.milk += int(cmd)
            self.state = "fill_beans"
        elif self.state == "fill_beans":
            self.beans += int(cmd)
            self.state = "fill_cups"
        elif self.state == "fill_cups":
            self.cups += int(cmd)
            self.state = "action"
        return True


def main():
    machine = CoffeeMachine()
    while True:
        machine.prompt()
        if not machine.handle_input(input()):
            break


if __name__ == "__main__":
    main()

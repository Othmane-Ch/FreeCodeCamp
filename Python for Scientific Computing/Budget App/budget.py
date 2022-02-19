from math import floor

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spent = 0
    def deposit(self, amount, description="") -> None:
        assert amount > 0
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description="") -> bool:
        if self.balance >= amount:
            self.ledger.append({"amount": -1 * amount, "description": description})
            self.balance -= amount
            self.spent += amount
            return True
        return False

    def get_balance(self) -> float:
        return self.balance

    def transfer(self, amount, budget_category) -> bool:
        if self.balance > 0:
            budget_category.deposit(amount, f"Transfer from {self.name}")
            return self.withdraw(amount, f"Transfer to {budget_category.name}")


    def check_funds(self,amount) -> bool:
        return self.get_balance() >= amount

    def __str__(self) -> str:
        outputStr = ''
        outputStr += self.name.center(30, '*')
        for item in self.ledger:
            desc = item["description"][:23]
            amt = '{:.2f}'.format(item["amount"])[-7:]
            outputStr += '\n{:<23}{:>7}'.format(desc, amt)
        # Add the total at the end
        outputStr += '\nTotal: {:.2f}'.format(self.balance)
        return outputStr




def create_spend_chart(categories)-> str:
    
  total = sum([category.spent for category in categories]) 
  categories_spent = []

  # Get the percentage that each category spent
  for category in categories:
    total_spent = sum([category.spent for category in categories])
    categories_spent = []

    # Get the percentage that each category spent
    for category in categories:
      categories_spent.append(floor(round((category.spent * 100) / total_spent) / 10.0) * 10 )

    
    bars = ""  # each "o"s and spaces
    lines = []  # whole second lines
    for number in range(100, -1, -10):
        match = lambda value: value >= number  # tests each percentage
        o_or_white = list(map(match, categories_spent))  # "True" and "False" list
        percentages = ["o" if digit else " " for digit in o_or_white]

        bars = "  ".join(percentages)

        lines.append(
            f"{str(number).rjust(3)}| {bars}  "
        )

    new_line = "\n"  # because backslashes can't be inside f-strings

    dashes = f"    -{'-' * len(bars)}--"
    names = []  # each category name displayed vertically

    individuals = [category.name for category in categories]
    largest_length = len(max(individuals, key=len))

    listed = []
    for name in individuals:
        if len(name) < largest_length:
            listed.append(name + (" " * (largest_length - len(name))))
        else:
            listed.append(name)
    
    separated = list(map(list, listed))
    zipped = zip(*separated)  # all lists being mapped
    tupled = list(zipped)

    for values in tupled:
        names.append(f"     {'  '.join(values)}  ")

    bar_chart = (
        "Percentage spent by category\n"
        f"{new_line.join(lines)}\n"
        f"{dashes}\n"
        f"{new_line.join(names)}"
    )

    return bar_chart

class Inventory:

    def __init__(self, coffee = 0, milk = 0, sugar = 0, chocolate = 0):
        self.coffee = coffee
        self.milk = milk
        self.sugar = sugar
        self.chocolate = chocolate
    
    def enoughIngredients(self, recipe):
        
        if self.coffee < recipe.amtCoffee:
            return False
        
        if self.milk < recipe.amtMilk:
            return False
        
        if self.sugar < recipe.amtSugar:
            return False
        
        if self.chocolate < recipe.amtChocolate:
            return False
        
        return True
    

    def useIngredients(self, recipe):
        if self.enoughIngredients(recipe):
            self.coffee -= recipe.amtCoffee
            self.milk -= recipe.amtMilk
            self.sugar -= recipe.amtSugar
            self.chocolate -= recipe.amtChocolate

            return True
        
        return False
    
    def addCoffee(self, quantity = 1):
        self.coffee += quantity
    
    def addChocolate(self, quantity = 1):
        self.chocolate += quantity

    def addMilk(self, quantity = 1):
        self.milk += quantity

    def addSugar(self, quantity = 1):
        self.sugar += quantity
    
    def __str__(self):
        return f"""
---------------------------
Coffee: {self.coffee}
Milk: {self.milk}
Sugar: {self.sugar}
Cbocolate: {self.chocolate}
---------------------------
"""
    
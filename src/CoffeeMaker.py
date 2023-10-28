from src.RecipeBook import RecipeBook
from src.Inventory import Inventory

class CoffeeMaker:

    def __init__(self):
        self.recipeBook = RecipeBook()
        self.inventory = Inventory()
        
    def addRecipe(self, recipe):
        return self.recipeBook.addRecipe(recipe)
    
    def deleteRecipe(self, recipeIndex):
        return self.recipeBook.removeRecipe(recipeIndex)

    def editRecipe(self, recipeIndex, recipe):
        return self.recipeBook.editRecipe(recipeIndex, recipe)
    
    def addInventory(self, chocolate, coffee, milk, sugar):
        self.inventory.addChocolate(chocolate)
        self.inventory.addCoffee(coffee)
        self.inventory.addMilk(milk)
        self.inventory.addSugar(sugar)

    def checkInventory(self):
        return self.inventory
    
    def getRecipes(self):
        return self.recipeBook.recipes
    
    def makeCoffee(self, recipeToPurchase, amountPaid):
        currentRecipe = self.getRecipes()[recipeToPurchase]

        if not currentRecipe:
            return amountPaid
        
        if currentRecipe.price <= amountPaid:
            if self.inventory.useIngredients(currentRecipe):
                return amountPaid - currentRecipe.price
            
            return amountPaid

        return amountPaid
    
    
    

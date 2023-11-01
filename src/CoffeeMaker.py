from src.RecipeBook import RecipeBook
from src.Inventory import Inventory

class CoffeeMaker:

    def __init__(self):
        self.recipeBook = RecipeBook()
        self.inventory = Inventory()
        
    def addRecipe(self, recipe):
        if type(recipe.price) == str or type(recipe.amtCoffee) == str or type(recipe.amtSugar) == str or type(recipe.amtChocolate) == str or type(recipe.amtMilk) == str:
            return False

        if recipe.price <= 0 or recipe.amtCoffee <= 0 or recipe.amtChocolate <= 0 or recipe.amtSugar <= 0 or recipe.amtMilk <= 0:
            return False
        
        return self.recipeBook.addRecipe(recipe)
    
    def deleteRecipe(self, recipeIndex):
        return self.recipeBook.removeRecipe(recipeIndex)

    def editRecipe(self, recipeIndex, recipe):
        if type(recipe.price) == str or type(recipe.amtCoffee) == str or type(recipe.amtSugar) == str or type(recipe.amtChocolate) == str or type(recipe.amtMilk) == str:
            return False

        if recipe.price <= 0 or recipe.amtCoffee <= 0 or recipe.amtChocolate <= 0 or recipe.amtSugar <= 0 or recipe.amtMilk <= 0:
            return False
        
        return self.recipeBook.editRecipe(recipeIndex, recipe)
    
    def addInventory(self, chocolate, coffee, milk, sugar):
        if type(chocolate) == str or type(coffee) == str or type(sugar) == str or type(milk) == str:
            return False

        if chocolate <= 0 or coffee <= 0 or milk <= 0 or sugar <= 0:
            return False
        
        self.inventory.addChocolate(chocolate)
        self.inventory.addCoffee(coffee)
        self.inventory.addMilk(milk)
        self.inventory.addSugar(sugar)

        return True

    def checkInventory(self):
        return self.inventory
    
    def getRecipes(self):
        return self.recipeBook.recipes
    
    def makeCoffee(self, recipeToPurchase, amountPaid):
        if recipeToPurchase > len(self.getRecipes()):
            return amountPaid
        
        currentRecipe = self.getRecipes()[recipeToPurchase]

        if not currentRecipe:
            return amountPaid
        
        if currentRecipe.price <= amountPaid:
            if self.inventory.useIngredients(currentRecipe):
                return amountPaid - currentRecipe.price
            
            return amountPaid

        return amountPaid
    
    
    

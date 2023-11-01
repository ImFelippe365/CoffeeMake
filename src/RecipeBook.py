from src.Recipe import Recipe

class RecipeBook:

    def __init__(self):
        self.maxRecipes = 4
        self.recipes = []
        
    def addRecipe(self, newRecipe):
        if len(self.recipes) == self.maxRecipes:
            return False

        if newRecipe in self.recipes:
            return False
        
        self.recipes.append(newRecipe)
        return True

    def removeRecipe(self, index):
        try: 
            if self.recipes[index]:
                recipeName = self.recipes[index].name
                del self.recipes[index]

                return recipeName
        except:
            return False
        
        return False
    
    def editRecipe(self, index, newRecipe):
        if not self.recipes[index]:
            return False
        
        recipeName = self.recipes[index].name
        self.recipes[index] = newRecipe

        return recipeName
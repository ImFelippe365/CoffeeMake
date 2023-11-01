from src.CoffeeMaker import CoffeeMaker
from src.Recipe import Recipe
from .base_test import BaseTest

class TestCoffeeMaker(BaseTest):

    def test_add_valid_recipe(self, setUp):
        recipe = Recipe("Coffee Test", 2, 1, 1, 1, 1)
        
        assert setUp.addRecipe(recipe)
    
    def test_add_invalid_recipe(self, setUp):
        recipe = Recipe("Coffee Test", 2, "1", "1", "1", "1")
        
        assert not setUp.addRecipe(recipe)
    
    def test_add_recipe_with_negative_values(self, setUp):
        recipe = Recipe("Coffee Test", -1, -3, -4, -2, -3)
        
        assert not setUp.addRecipe(recipe)

    def test_remove_recipe(self, setUp):
        recipe = Recipe("Coffee Test", 2, 1, 1, 1, 1)
        setUp.addRecipe(recipe)
        
        assert setUp.deleteRecipe(0)

    def test_remove_nonexistent_recipe(self, setUp):
        assert not setUp.deleteRecipe(9)

    def test_edit_recipe(self, setUp):
        recipe = Recipe("Coffee Test", 2, 1, 1, 1, 1)
        setUp.addRecipe(recipe)

        edited_recipe = Recipe("Edited Coffee Test", 200, 100, 100, 100, 100)
        
        assert setUp.editRecipe(0, edited_recipe)

    def test_edit_recipe_with_invalid_content(self, setUp):
        recipe = Recipe("Coffee Test", 2, 1, 1, 1, 1)
        setUp.addRecipe(recipe)

        edited_recipe = Recipe("Edited Coffee Test", -1, -3, -4, -2, -3)
        
        assert not setUp.editRecipe(0, edited_recipe)

    def test_add_inventory(self, setUp):
        assert setUp.addInventory(13, 13, 13, 13)
    
    def test_add_invalid_inventory(self, setUp):
        assert not setUp.addInventory("5", "5", "5", "5")
    
    def test_add_inventory_with_negative_values(self, setUp):
        assert not setUp.addInventory(-22, -22, -22, -22)

    def test_make_coffee(self, setUp):
        recipe = Recipe("Coffee Test", 2, 1, 1, 1, 1)
        setUp.addRecipe(recipe)
        
        assert setUp.makeCoffee(0, 1) == 1

    def test_make_coffee_insufficient_money(self, setUp):
        recipe = Recipe("Coffee Test", 5, 1, 1, 1, 1)
        setUp.addRecipe(recipe)
        
        assert setUp.makeCoffee(0, 4) == 4
    
    def test_make_coffee_invalid_recipe(self, setUp):
        recipe = Recipe("Coffee Test", 2, 1, 1, 1, 1)
        setUp.addRecipe(recipe)
        
        assert setUp.makeCoffee(5, 1)
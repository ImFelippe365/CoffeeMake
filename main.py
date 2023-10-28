from src.CoffeeMaker import CoffeeMaker
from src.Recipe import Recipe

class Main:
    

	def __init__(self, *args, **kwargs):
		self.coffeeMaker = CoffeeMaker()
		
	def menu(self):
		print(25*"-")
		print("1- Adicionar uma receita")
		print("2- Remover uma receita")
		print("3- Editar uma receita")
		print("4- Adicionar inventário")
		print("5- Checar inventário")
		print("6- Fazer café")
		print(25*"-")
		print("0- Sair")
		print(25*"-")
		
		userInput = int(input("Digite um número que corresponde o que você quer fazer: "))
        
		if userInput == 1:
			self.addRecipe()
		elif userInput == 2:
			self.deleteRecipe()
		elif userInput == 3:
			self.editRecipe()
		elif userInput == 4:
			self.addInventory()
		elif userInput == 5:
			self.checkInventory()
		elif userInput == 6:
			self.makeCoffee()
		elif userInput == 0:
			exit(1)
		else:
			print("Opção inválida")
			self.menu()

	def addRecipe(self):
		name = input("\nInsira o nome da receita: ")
		price= input("\nInsira o valor da receita: ")
		coffee= input("\nInsira a quantidade de café usada na receita: ")
		milk= input("\nInsira a quantidade de leite usada na receita: ")
		sugar= input("\nInsira a quantidade de açúcar usada na receita: ")
		chocolate= input("\nInsira a quantidade de chocolate usada na receita: ")

		recipe = Recipe(name, price, coffee, milk, sugar, chocolate)
		recipeAdded = self.coffeeMaker.addRecipe(recipe)

		if not recipeAdded:
			print("(!) Receita não adicionada, máximo de 4 receitas.")
		else:
			print("(✔) Receita adicionada com sucesso!")

		self.menu()

	def deleteRecipe(self):
		for index, recipe in enumerate(self.coffeeMaker.getRecipes()):
			print(f"{index}- {recipe.name}")

		recipeToDelete = self.recipeListSelection("\nDigite o número referente a receita que deseja remover: ")
	
		if not recipeToDelete or recipeToDelete < 0:
			return self.deleteRecipe()
		
		recipeDeleted = self.coffeeMaker.deleteRecipe(recipeToDelete)
        
		if recipeDeleted:
			print(f"(✔) {recipeDeleted} ")
		else:
			print("(!) A receita selecionada não pôde ser removida.");
        
		self.menu()
    
	def editRecipe(self):
		for index, recipe in enumerate(self.coffeeMaker.getRecipes()):
			print(f"{index}- {recipe.name}")
		
		recipeToEdit = self.recipeListSelection("\nDigite o número referente a receita que deseja editar: ")
        
		if not recipeToEdit or recipeToEdit < 0:
			self.editRecipe()

		name = input("\nInsira o nome da receita: ")
		price= input("\nInsira o valor da receita: ")
		coffee= input("\nInsira a quantidade de café usada na receita: ")
		milk= input("\nInsira a quantidade de leite usada na receita: ")
		sugar= input("\nInsira a quantidade de açúcar usada na receita: ")
		chocolate= input("\nInsira a quantidade de chocolate usada na receita: ")
		
		recipe = Recipe(name, price, coffee, milk, sugar, chocolate)
		recipeEdited = self.coffeeMaker.editRecipe(recipeToEdit, recipe)

		if not recipeEdited:
			print("(!) Receita não foi editada.")
		else:
			print("(✔) Receita editada com sucesso!")
		
		self.menu()
    
	def addInventory(self):
		coffee= int(input("\nInsira a quantidade de café para adicionar ao inventário: "))
		milk= int(input("\nInsira a quantidade de leite para adicionar ao inventário: "))
		sugar= int(input("\nInsira a quantidade de açúcar para adicionar ao inventário: "))
		chocolate= int(input("\nInsira a quantidade de chocolate para adicionar ao inventário: "))

		self.coffeeMaker.addInventory(chocolate, coffee, milk, sugar)
		print("(✔) Itens adicionados ao inventário")
        
		self.menu()
    
	def checkInventory(self):
		print(self.coffeeMaker.inventory)
		self.menu()
    
	def makeCoffee(self):
		if len(self.coffeeMaker.getRecipes()) == 0:
			print("(!) Sem receitas cadastradas. Adicione alguma primeiro.")
			self.menu()
		
		recipeToPurchase = self.recipeListSelection("\nDigite o número referente a receita que deseja comprar: ")
        
		amountPaid = int(input("Digite a quantidade que deseja pagar: "))
	
		if not amountPaid or amountPaid > 0:
			print("(!) Informe um valor válido.")
			return self.makeCoffee()
        
		change = self.coffeeMaker.makeCoffee(recipeToPurchase, amountPaid)
        # talvez se informar o dobro da compra, dê bug
		if change == amountPaid:
			print("(!) Valor fornecido é insuficiente para prosseguir com a compra")
		else:
			print(f"Obrigado pela compra! -> {self.coffeeMaker.getRecipes()[recipeToPurchase].name} ")
			
		if change != 0:
			print(f"Seu troco é de R$ {change}")
		
		self.menu()
    
	def recipeListSelection(self, message):
		for index, recipe in enumerate(self.coffeeMaker.getRecipes()):
			print(f"{index}- {recipe.name}")
		
		userSelection = int(input(message))
		recipe = userSelection - 1

		try:
			if not (recipe >= 0 and recipe <=2):
				recipe = -1
		except:
			print("Por favor, escolha uma opção no intervalo de 1-3.")
			recipe = -1
        
		return recipe
	
coffeeMaker = Main()
coffeeMaker.menu()
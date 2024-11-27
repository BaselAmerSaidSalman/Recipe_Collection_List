import time

class Recipe:
  def __init__ (self, name, ingredients, time, instuctions):
    self.name = name
    self.ingredients = ingredients
    self.time = time
    self.instuctions = instuctions

  def print_recipe(self):
    print("\n\n Displaying recipe...")
    print(f"Recipe Name: {self.name}")
    print(f"Recipe Ingredients: {self.ingredients}")
    print(f"Recipe Time: {self.time}")
    print(f"Recipe Instuctions: {self.instuctions}")

def create_recipe():
  name = input("\n\nEnter the receipe name: ")
  ingredients = input("Enter the receipe ingredients: ")
  time = input("Enter the receipe time: ")
  instuctions = input("Enter the receipe instuctions: ")

  return Recipe(name, ingredients, time, instuctions)
recipe1 = create_recipe()
recipe1.print_recipe()
number = input("Enter 1 to create another recipe or 2 to exit: ")
if number == "1":
  create_recipe().print_recipe()
else:
  print("Exiting...")
  time.sleep(2)
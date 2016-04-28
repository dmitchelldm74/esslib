from esslib import ess as e

ess = e.ESS1(open("test1.ess", "r").read()) # input as string
ess.parse() # parses string
# __help__ for help
print ess.get("__comments__") # gets the comments of the ess
print ess.get("__tree__") # gets complete tree
print ess.get("__vars__") # gets the variables of the ess
print ess.getItem("body") # gets an item with the name 
print ess.toCSS() # turns ess to css
# ess.getIds() gets all ids
# ess.getClasses gets all classes
# ess.getAllStartWith(<startswith>) gets all items that start with <startswith>

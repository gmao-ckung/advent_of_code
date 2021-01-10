import os
import math
import numpy as np
import numpy.ma as ma
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.test")
ingredients_and_allergens = f1.readlines()

ingredient_count = {}

for I_A in ingredients_and_allergens:
    I_A = I_A.replace("\n","")
    I_A_s = I_A.split("(contains")
    
    ingredients = I_A_s[0].split(" ")
    allergens = I_A_s[1].split(",")
    for i in range(len(allergens)):
        allergens[i] = allergens[i].replace(" ", "")
        allergens[i] = allergens[i].replace(")", "")
    #print(ingredients)
    for ingredient in ingredients:
        if ingredient != "":
            if ingredient not in ingredient_count.keys():
                ingredient_count[ingredient] = [1, []]
                for allergen in allergens:
                    ingredient_count[ingredient][1].append(allergen)
            else:
                ingredient_count[ingredient][0] += 1
                for allergen in allergens:
                    ingredient_count[ingredient][1].append(allergen)

print(ingredient_count)
   
class food_item(object):
    def __init__(self, name, calories, protein, carbohydrate, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat

    def Sum(food_list):
        calories_total = 0
        protein_total = 0
        carbohydrate_total = 0
        fat_total = 0
         
        for i in food_list:
            calories_total += i.calories
            protein_total += i.protein
            carbohydrate_total += i.carbohydrate
            fat_total += i.fat
        
        if calories_total > 2500:
            print("WARNING: calories intake is above 2500")
        if fat_total > 90:
            print("WARNING: fat intake is above 90g")
        return [calories_total,protein_total,carbohydrate_total,fat_total]

###example usage###
apple = food_item("apple", 60, 0.3, 15, 0.5)
rice = food_item("rice", 200, 4.0, 45, 0.4)
chicken = food_item("chicken", 250, 35.0, 0, 8.0)
milk = food_item("milk", 120, 6.0, 12, 5.0)
burger = food_item("burger", 700, 25.0, 50, 40.0)
fries = food_item("fries", 500, 5.0, 60, 25.0)
ice_cream = food_item("ice cream", 300, 4.0, 35, 15.0)

food_list = [apple, rice, chicken, milk, burger, fries, ice_cream]

result_list = food_item.Sum(food_list)
print(f"Total calories:{result_list[0]}")
print(f"Total protein:{result_list[1]}")
print(f"Total carbohydrate:{result_list[2]}")
print(f"Total fat:{result_list[3]}")
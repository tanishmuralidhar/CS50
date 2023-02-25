cost_meal = int(input("How much did your meal cost: "))
tip_percentage = float(input("What percentage of your meal will you like to tip: "))
New_tip = float(tip_percentage / 100)
Amount_to_tip = New_tip * cost_meal
print("You should tip:", Amount_to_tip)

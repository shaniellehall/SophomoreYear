"""
Purpose: Write a main script that Prompts the user to enter: The beverage name, serving size, grams of sugar per serving and the milligrams of caffeine per serving
         Creates a BeverageItem object using the data entered by the user. Displays the beverage’s nutritional information. Asks how many servings were consumed.
         Calculates and displays: The total sugar consumed and The total caffeine consumed.
Name:    Shanielle Hall
UserID:  snh325   
Date:    9/23/2025
"""

import beverage
import inputroutines

if __name__ == "__main__":
    
    bev_name = input("Enter beverage name: ")
    
    print("Enter serving size in mL (0 - 1000): ", end="")
    serv_size = inputroutines.intInRange(0, 1000)
    
    print("Enter grams of sugar per serving (0.0 - 75.0): ", end="")
    grams_sugar = inputroutines.floatInRange(0.0, 75.0)
    
    print("Enter milligrams of caffeine per serving (0.0 - 400.0): ", end="")
    milli_caff = inputroutines.floatInRange(0.0, 400.0)
    
    bev_item = beverage.BeverageItem(bev_name, serv_size, grams_sugar, milli_caff)

    print("")
    print("Nutritional information per serving of", bev_item.getName())
    print("Serving Size:", bev_item.getServingSize(), "mL")
    print(f"Sugar: {bev_item.getSugar():.2f} grams")
    print(f"Caffeine: {bev_item.getCaffeine():.2f} mg")

    print("")
    print("Enter number of servings consumed (0 – 10): ", end="")
    serv_consu = inputroutines.intInRange(0, 10)

    total_sugar = bev_item.calculateTotalSugar(serv_consu)
    total_caffeine = bev_item.calculateTotalCaffeine(serv_consu)

    print(f"Total sugar consumed: {total_sugar:.2f} grams")
    print(f"Total caffeine consumed: {total_caffeine:.2f} mg")

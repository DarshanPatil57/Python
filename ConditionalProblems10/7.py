#7. Coffee Customization
#Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.


size = input("Choose your coffee size (Small, Medium, Large): ").capitalize()
extra_shot = input("Would you like an extra shot of espresso? (Yes or No): ").capitalize()

if size in ['Small', 'Medium', 'Large']:
    order = f"{size} coffee"
    
    if extra_shot == 'Yes':
        order += " with an extra shot of espresso"
    elif extra_shot != 'No':
        print("Invalid input for extra shot.")
    print("Your order:", order)
else:
    print("Invalid size entered.")

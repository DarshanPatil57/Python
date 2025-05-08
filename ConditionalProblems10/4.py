#4. Fruit Ripeness Checker
#Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Enter Fruit name : ")
color = input("Enter fruit color : ")

if fruit=='Banana':
    if color=='Green':
        print("Fruit is unripe")
    elif  color=='Yellow':
        print('Fruit is ripe')
    elif  color=='Brown':
        print("Fruit is overripe")
else:
    print('No fruit and color found')
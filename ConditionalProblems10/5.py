#5. Weather Activity Suggestion
#Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).


weather = input("Enter your current Weather : ").capitalize()

if weather == 'Sunny':
    print("Go for a walk")
elif weather == 'Rainy':
    print("Read a Book")
elif weather == 'Snowy':
    print('Build a snowman')
else:
    print('Incorrect input')
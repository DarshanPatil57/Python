#10. Pet Food Recommendation
#Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter your species name (Dog or Cat): ").lower()
age = int(input("Enter species age: "))

if species in ['dog', 'cat']:
    if species == 'dog':
        if age <= 2:
            print("Recommended food: Puppy food")
            
    elif species == 'cat':
        if age > 5:
            print("Recommended food: Senior cat food")
else:
    print("Sorry, we only have recommendations for dogs and cats.")


# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

# Method 1

age = int(input('Enter your age : '))
day='Wednesday'
if age > 18 :
    price =12
    print("You are adult . Your ticket Price is $ ",price)
else:
    price = 8
    print("You are Children . Your ticket Price is", price)

if day =='Wednesday':
    final_price = price-2
    print("Your final ticket price with discount is $",final_price)

# Method 2

age = int(input('Enter your age : '))
day='Wednesday'
price = 12 if age > 18 else 8

if day == 'Wednesday':
    price = price-2

print("Final Ticket price for you is $" , price)
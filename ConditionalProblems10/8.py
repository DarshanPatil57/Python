#8. Password Strength Checker
#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input('Enter your password : ').lower()

length = len(password)

if length < 6:
    print("Password Strength: Weak")
elif length <= 10:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

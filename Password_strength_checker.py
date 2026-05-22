password=input("Enter password:")

has_upper=False
has_lower=False
has_digit=False
has_symbol=False

symbols="!@#$%^&*()-_=+[];',./<>?:~`}|{"

for char in password:
    if char.isupper():
        has_upper=True
    elif char.islower():
        has_lower=True
    elif char.isdigit():
        has_digit=True
    elif char in symbols:
        has_symbol=True
if len(password)>=8 and has_upper and has_lower and has_digit and has_symbol:
    print("strong Password")
elif len(password)>=6 and ((has_digit or has_symbol) and (has_upper or has_lower)):
    print("Medium Password")
else:
    print("weak Password")
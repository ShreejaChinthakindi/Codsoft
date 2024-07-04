import random
upper_letters = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_letters = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','(',')','*','~']
print("password Generator! ")
length = int(input("Enter length of password: "))
user_input = input("Do you want specifications(yes/no): ")
password_l=[]
password = ''
if user_input == 'yes':
    n_upletters = int(input("How many upper letters do you want in your password? "))
    n_lowletters = int(input("How many lower letters do you want in your password? "))
    n_symbols = int(input("How many symbols do you want in your password? "))
    n_numbers = int(input("How many numbers do you want in your password? "))
    if length != n_upletters+n_lowletters+n_symbols+n_numbers:
        print("Your specifications do not match your length of password. \n Please enter your specifications that match the length of your password." )
    else:
        for i in range(0,n_upletters):
            char1=random.choice(upper_letters)
            password_l.append(char1)
        for i in range(0,n_lowletters):
            char2=random.choice(lower_letters)
            password_l.append(char2)
        for i in range(0,n_symbols):
            char3=random.choice(symbols)
            password_l.append(char3)
        for i in range(0,n_numbers):
            char4=random.choice(numbers)
            password_l.append(char4)
        random.shuffle(password_l)
        for i in password_l:
            password += i
        print("Your password:",password)
else:
    for i in range(0,length):
        all=upper_letters+lower_letters+numbers+symbols
        char5 = random.choice(all)
        password += char5
    print("Your password is:",password)
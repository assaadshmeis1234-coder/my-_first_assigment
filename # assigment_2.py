# assigment_2.py
stor_login = 'admin'
stor_pass = '1234'
loggin_success = False
for attempt in range (3):
    login = input('enter login :')
    password = input('enter password :')
    if login == stor_login and password == stor_pass:
        print('welcome')
        loggin_success = True
        break
    else:            
       print('try again')

if not loggin_success:
    print('your account is blocked')
    exit()
    
    
    
N = int(input("Enter a number N: "))

print("Prime numbers between 2 and {N}:")
for num in range(2, N + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
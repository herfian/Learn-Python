#Password Checker
username = input('What is your username? ')
password = input('What is your password? ')

password_lenght = len(password)
hidden_password = '*' * password_lenght

print(f'{username}, your password, {hidden_password}, is {password_lenght} letters long')

# Output :
# What is your username? Mark
# What is your password? 12345678
# Mark, your password, ********, is 8 letters long
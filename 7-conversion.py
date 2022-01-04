birth_year = input('what year were you born? ')
print(type(birth_year))

# Output :
# what year were you born? 1999
# <class 'str'>


age = 2021 - int(birth_year)
print(f'your age is : {age}')

# Output :
# your age is : 22
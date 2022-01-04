print(type("Hello"))
# Output : <class 'str'>

id = 'vermilian99'
pw = '123456'
sentence = '''
Hello
im
hereeeee
'''
print(sentence) 
# Output :
# Hello
# im
# hereeeee

first_name = "Tony"
last_name = "Stark"
full_name = first_name + ' ' + last_name
print(full_name)
# Output :
# Tony Stark

#Type Conversion
a = str(50)
b = int(a)
c = type(b)
print(c) # Output : <class 'int'>

#Escape Sequence
weather = '\t It\'s \"kind of\" sunny \n Hope you have a nice day!'
print(weather)
# Output :
#      It's "kind of" sunny 
#  Hope you have a nice day!

#Formatted Strings
age = 55
print(f'Hi {full_name}. You are {age} years old')
# Output :
# Hi Tony Stark. You are 55 years old
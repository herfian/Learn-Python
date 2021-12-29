#List Slicing
Amazon_store = [
  'Notebooks',
  'Sunglasses',
  'Toys',
  'Grapes',
  'Books'
]
#Mutable list
Amazon_store[0] = 'laptop'

# Output :
print(Amazon_store)
# ['laptop', 'Sunglasses', 'Toys', 'Grapes', 'Books']

print(Amazon_store[1])
# Sunglasses

print(Amazon_store[0:3])
# ['laptop', 'Sunglasses', 'Toys']

print(Amazon_store[0::2])
# ['laptop', 'Toys', 'Books']

#New
New_chart = Amazon_store[:]
New_chart[0] = 'Gum'
print(New_chart)
# ['Gum', 'Sunglasses', 'Toys', 'Grapes', 'Books']

print(Amazon_store)
# ['laptop', 'Sunglasses', 'Toys', 'Grapes', 'Books']
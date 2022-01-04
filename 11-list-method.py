basket = [1,2,3,4,5,6,7]

#Adding
basket.append(20)
basket.insert(5, 70)
print(basket)

# Output :
# [1, 2, 3, 4, 5, 70, 6, 7, 20]

#Removing
newlist = basket
newlist.pop(5) #Index
newlist.remove(20) #Value
print(newlist)

# Output :
# [1, 2, 3, 4, 5, 6, 7]

list1 = newlist
list1.clear()
print(list1)

# Output :
# []
word = ['a','b','c','d','e','f','a']

# Output :
print(word.index('d')) # 3
print('f' in word) # True
print('g' in word) # False
print('i' in 'hii my name is ian') #True
print(word.count('a')) # 2

#Method 3
wordR = ['k','p','x','v','q','w','g','h','l']
wordR.sort() # print(sorted(wordR))
wordR.reverse()
print(wordR)
# Output :
# ['x', 'w', 'v', 'q', 'p', 'l', 'k', 'h', 'g']

#List Patterns
print(list(range(1,100)))
# Output : 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

sentence = ' '.join(['hi','my','name','is','mark'])
print(sentence)
# Output :
# hi my name is mark

#List Unpacking
a,b,c, *other, d = 1,2,3,4,5,6,7,8,9,10,11,12,13
# Output :
print(a) # 1
print(b) # 2
print(c) # 3
print(other) # [4, 5, 6, 7, 8, 9, 10, 11, 12]
print(d) # 13
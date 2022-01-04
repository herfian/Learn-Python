set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9}

print(set1.difference(set2))
#Output {1, 2, 3}

print(set1.discard(5))
print(set1)
# Output
# None
# {1, 2, 3, 4}

print(set1.difference_update(set2))
print(set1)
# Output
# None
# {1, 2, 3}

print(set1.intersection(set2))
# Output
# {4, 5}

print(set1.isdisjoint(set2))
# Output
# False

print(set1.union(set2)) # / (set1 | set2)
# Output
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(set1.issubset(set2))
print(set2.issuperset(set1))
#Output
# False
# False
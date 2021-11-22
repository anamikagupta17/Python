a=set()
a.add('python')
a.add('     ')
print('add multiple elemetns in set')
a.update([1,2,3])
a.update((4,5))
print(a)
b={1,2,3,'anamika'}
b.remove('anamika')
print(b)
print('set methods')
st1={1,2,3,4,7,8}
st2={33,44,66,7,8,2}
print(st1)
print(st2)
print("Intersection",st1.intersection(st2))
print("Union",st1.union(st2))
print("difference",st1.difference(st2)) # return element of first set which is not in other set
print("subset",st1.issubset(st2))
print("Superset",st1.issuperset(st2))
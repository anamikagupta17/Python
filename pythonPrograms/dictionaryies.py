dict={1:"Anamika",2:"Parul",3:"Pramod"}
print(id(dict))
print("modify")
dict[2]="Adddddd"
print(dict)
print(id(dict))
print(dict[1])
print("insertion")
dict[4]="PM"
print(dict)
print("delete")
del dict[2]
print(dict)
#del dict #delete whole dict
print(1 in dict)
print(10 in dict)
print(3 not in dict)
print(7 not in dict)

print(id(dict))
print('new coppied dict')
stu=dict.copy()
print(stu)
print(id(stu))

print('create new dict')
keys=(101,102,103,104,105)
values="Anamika"
new_dict=dict.fromkeys(keys,values) # disct is a keyword values will assign same to th every key
print(new_dict)
print('get method')
print(new_dict.get(102))
print(new_dict.get(109))
print('items method')
it=new_dict.items()
print(it)
lst=list(it)
print(lst)
print(lst[0][0])
print(lst[0][1])
for r in lst:
    for c in r:
        print(c)

print('keys method')
print(new_dict.keys())
print('values method')
print(new_dict.values())
print('update method')
new_dict.update({103:"ana"})
print(new_dict)
print('pop method')
print(new_dict)
print('removed item value')
print(new_dict.pop(101))
print(new_dict.pop(1111,'default value'))
print(new_dict.popitem())
print('setdefault method')
print(new_dict.setdefault(102,'anamm'))
print(new_dict.setdefault(107,'anamm'))
print(new_dict)
print('Access values using for loop')
for k in new_dict:
    print(k)
    print(new_dict[k])
    print(k,"=",new_dict[k])


print("input from user")
a={}
n=int(input("number of elements :"))
for i in range(n):
    key=int(input('enter key :'))    
    value=input('enter value :')
    a.update({key:value})

print(a)    
print('nested dictionary')
nest_dic={1:{"rol1":101,"rol2":102},2:{"rol3":103,"rol4":104}}
print(nest_dic[1])
print(nest_dic[1]['rol1'])
for i in nest_dic:
        for k in nest_dic[i]:
            print(k,"-",nest_dic[i][k])
     
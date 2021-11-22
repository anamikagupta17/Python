data types
set->unordered,{},duplicate values are not acceptable,index can not be use because of unordered
tuple->can't modify ,()
list->[]->can perform all operation eg:modify,delete,....
disctionary/mapping/dist->store data as key & value ,{}
array->[]->store same  data type of data

operators
logical operators
AND
True and expression : return expression (last expression) eg: True and 100 and 200  =200
False and expression : return False eg: False and 200=False
OR
True or expression : return True  eg: True or 100 =True
False or expression : return expression (First expression) eg: False or 200 or 100 =200


membership operators
in ->find an element in a specifid sequence  eg: st1="Welcome"  'co' in st1 True
not in ->return True if element is present in sequence   eg: st1="Welcome"  'co' not in st1 False


identity operators
is->check two objects are same or not eg : a=10,b=10 a is b : True 

is not ->check two objects are same or not eg : a=10,b=10 a is not b : False 

type conversion
implicit : convert automatic one to other data type eg: 5/2 flaot
explicit/cast : programmer can convert according to choice  eg: int(n),float(n)

print(object,sep='character',end="charachter",file=sys.stdout,flush=False)
sep: could be any string or character, by default ' '
end : could be any string or character, by default '\n'
file: a object  with write menthod  by default sys.stdout
flush: a boolean,if output flushed(True) or buffered(False)default False

input()->convert all input values into string

\" python escape it  eg: "Anamika\"Gupta\""

range(start,stop,stepsize)
start->by defualt 0
stop->by default j-1(j is the value )
stepsize by default 1
all arguments must be integer(it can be postive or negative) & stepsize should not be 0

break ->condition ture break the loop
continue->condition ture skip the below part and start from top(stop at contiue and start excuting code from begining will not go down )
 eg: if(i==3)continue then it will skip  this 3 and print rest of the values

pass: when we don't want to perform  any action in true condiiton

python does not support multi dimentional array (but we can create multi dimentional array using thire party package like "numpy")
by deafult can't use array in python for that need to import module
syntax: array(type_code,[elements])
Array Methods
insert(postion,value)
pop()->delete in last
pop(position)->returns deleted element 
remove(value)->first occurance of element ,if element not present then will give error
index(value)->gives first occurance of element index
extend()->merge to array
slicing(start,stop,setpwise)->eg: array[1:3] ,array[0],array[:5],array[3:] stop-1(last element),array[1:9:2]

pip->package installer

not use any reserve kyword as file name(some time it will create issue: eg numpy,operator)
array functions
array()
linspace(start,stop,num=50,endpoint=true) ->if endpoint true then only include last element by default true
linspace used in data science(divide array elemnts)
logspace(start,stop,num=50,endpoint=true,base=10,dtype=None)->space number according to allgorithm
start(base^start)
stop(base^stop)
eg: logspace(1,3,5),array start from 10^1 and end array 10^3 will divide this array in 5 parts becuse num=5
arange(start,stop,setpsize,dtype=None)->start by default 0 till stop-1
zeros(shape,dtype=float,order='C')->create all 0's  order->column wise or row wise C=column,R=rows
ones(shape,dtype=float,order='C')->create all onces

all()->if all ture thin return true else false also empty aray return false
any()->if any one true then return true else false
where(con,a,b) if condition true then a else b
nonzero()->return array index of non zero(without zero) 
view()->share memory location so effect all they array (means all array will have same data but address will be different)
eg:a=array([10,20]),b=a.view()  if we change b then it will change in a also
copy()->copy array to another variable after change data will not be same while copy it will same 
reshape(array_name,(n,r,c))->chnage the shape of array 1d to 2D viceversa..
n->no of arrays(specially for 3D)
r->rows
c->cols

attributs of array
ndim ->array_name.ndim
shape->array_name.shape
size->size of the array
itemsize->size of items
nbytes->byts of array


mutuable object->values can be change eg: list,set,disctionary
immutable object->value can not be change(modify) eg: number,string ,tuples

ispace()->retun true if string contain only space
lstrip()->remove left space of string
rstrip()->remove right space of string
strip()->reove both side space left and right

we can pass a function as a parameter
function can return a functiona

Formal arguments : def add(x,y) : x,y formal arguments
Actual Arguments:add(3,4):3,4 Actual arguments
 1. Postional
 2. Keyword eg: add(a=2,b=3)
 3. default 
 4. variable lenth (accept any number of arguments (store in a tuple)) : eg def add(*num): num[0]+num[1]+....
 5. Keyword variable lenth (accept any number of arguments with key vlaue pair(store data in disctionary)) 
 eg: def add(**num): num[a]*num[b] :add(a=2,b=3,c=4)

 ** Anonymous function/lambda function
 lambda function return a function.we can use this for only expression
 so we store it in a variable and print that

IIFE(  Immitiatley invokedunction expression): call automatic

list
b=[3,4,5,6,7]
pop()->delete last element 
remove()->delete first occurnce of element
extend()->merge to list
clear()->delete all ements of list
clone: a=b[:]  // independent(if we change in a then it will not change in b )
copy():a=b.copy() //// independent (if we change in a then it will not change in b )
list()->also used to create list

higher order function(function pass other function)
filter()->it return those element of sequece, for which function return true
(it will return filter object then  need to convert in list or according to need)
None ->means true in filter 
map()-> it return map object so need to convert in list or...according to need
reduce()->used to reduce sequece in a single value
above function use for sequence(list,tuple,...)(iterable)


Generators->are function that return a sequece of values
yield->return element from generator function  into a generator object
next->uset to retrive elements from generator object

tuple
take less memory as compare to list
a=(1,2,3,4,'fsdgsds',10.4)
for signle element tuple need to create  as eg: (10,) otherwise it will be integer
we can create tuple without parenthesis() also
tuples elements can not be modify but we can concatinate 2tuples

set
unordered,no duplicate,mutable,set can't be nested means(can not create set inside set)
elements can be different type except mutalbe element(list,set,or dictionary)
we can not access set by index number because it is unordered 
a={12,23,45,67,87,4.2}
empty set : a=set()
remove()->delete element  but it will give error if element not there
discard()->delete element
clear()->delete all element of set

dictionary
unordered collection in key value pair,mutable
a={'a':101,'b':102}
empty dictionary: name={}
keys are case sensetive
if mention same key then old key overwritten
key is  immutable(can not change key name)
clear()->remove all eents of dictionary
copy()->copy all elemnt into new dict
get(key,defaultvalue)->get the value from key: if key not there then default value(optional will work
items()-:return key value pair
keys()->return all keys 
values()->return all values
update()->update values with key also add new element
pop(key,defaultvalue)->remove specified key it returs reoved item value if key not there then return default value
popiitem()->delete last added element from dictionaryand return deleted in from of tuple
setdefault()->return value to the key or if key not exist then insert and return vlaue


comperhension: single line code to perform a task
can use multiple if and for loop (in multiple loop outer loop run first)
list[]->return list
dictionary{}-> return dictionary
set{}->return set
***
id->return identity of object (identity is different for every object)
type()->return type of object
getsizeof()->return size of object in bytes (for using this need to import sys)
min()->return smallest object(can be list,object key value)
max()->return largest object(can be list,object key value)
sorted()->return new sorted object(list,tuple,set,dictionary)




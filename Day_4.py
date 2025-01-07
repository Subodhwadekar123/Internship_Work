# #Set operation
# set1=set(input("Enter the set no 1:"))

# set2=set(input("Enter the set no2: "))

# set3=set1.union(set2)
# print(set3)
# set4=set1.intersection(set2)
# print(set4)
# set1.intersection_update(set2)
# print(set1)

#List operation
# lst1=[i for i in range(50) if i%2==0 and i!=0]
# print(lst1)
# lst2=[j for j in lst1 if j>2 and j<20]
# print(lst2)


#Dictionary
# unordered becuase of keys
# dict_1={}
# print(dict_1)

# dict_1={i:i**2 for i in range(10)}
# print(dict_1)
# keys=(1,2,3,4,5,6)
# values=['a','b','c','d','e','f']
# dict_2={keys[i]:values[i] for i in range(len(keys))}
# print(dict_2)
# dict12 = {'name': 'John', 'age': 25, 'address': {'city': 'New York', 'state': 'NY','pincode':121314}}

#Frozenset()
# frozenset is immutable after created we cannot modify it.
# when we dont want to change in the set of data then we use frozen set..
# dict1=frozenset({1,2,3,4,5,6,7})
# dict2=frozenset({7,6,5})
# combined= dict1 | dict2
# comb=dict1.union(dict2)
# print(comb)
# intersect=dict1 & dict2
# diff=dict1 - dict2
# disjoint=dict1.isdisjoint(dict2)
# superset=dict1.issuperset(dict2)
# subset=dict1.issubset(dict2)    
# print(combined)
# print(intersect)
# print(diff)
# print(disjoint)
# print(superset)
# print(subset)

# #dictionary methods
# dic = {'name': 'John', 'age': 25, 'address': {'city': 'New York', 'state': 'NY','pincode':121314}}
# print(dic.keys()) #output: dict_keys(['name', 'age', 'address'])
# print(dic.values()) #output: dict_values(['John', 25, {'city': 'New York', 'state': 'NY'}])
# print(dic.items()) #output: dict_items([('name', 'John'), ('age', 25), ('address', {'city': 'New York', 'state': 'NY'})])
# print(dic['name'])
# print(dic.get('age'))
# dic['address']='Pune'

# dic.pop('address')
# dic.popitem()
# print(dic)
# dic.clear()

#iterate throught dictionary.items() and check the type of the value
# item = dic.items()
# for i in dic.items():
#     print(i)



# tempTupleDetails = next((i for i in item))#next() method returns the next item from the iterator
# print(tempTupleDetails)
# print(type(tempTupleDetails))
# dic2=dic.copy()
# print(dic2)


# shallow copy is only works for main dictionary not for sub dict
#deep copy : it will works on the both dicts
# sub dict means copied dictionary of old one into another dict

# import copy
# dic3=copy.deepcopy(dic)
# print(dic3)
# evensquare={i:i**3 for i in range(10) if i%2==0}
# print(evensquare)
# # task to_do_list
# Any datatype you can use
# buy grocery
# it will shows status o incomplete,1 complete

to_do_list={ #initially it will be incomplete
    'Buy Tshirt':0,
    'Buy pants':0,
    'Buy toothpaste':0,
    'Buy chocolates':0
    }
for keys in to_do_list.items() :
    print(keys)
for keys,values in to_do_list.items() :
    print(f"{keys}:{'complete' if values==1 else 'incomplete'}")

task_name=input("Enter the task from list to mark as complete:")
if task_name in to_do_list :
    to_do_list[task_name]=1
    print(f"{task_name} marked as complete ")
else :
    print(f"{task_name} not found in to do list")
print(to_do_list)
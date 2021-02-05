# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
'''So here we are going to study about python data type'''
 '''here in this you will study about data type and use of data type'
 datatypes are Numbers, Strings, Printing,Lists ,Dictionaries ,Booleans ,Tuples, Sets '''


# %%
# Number / Integer


1


# %%
x = 20 # assign a value to variable
print(x)
x # either for single variable you can write only variable name


# %%
# for square
print(2 ** 2)
print(4**2)


# %%
int((2*2) + (2*3) + (16/2))


# %%
''' in Python arthematical operator work in this way  
Order of operation - PEMDAS
  1. Parentheses ( )
  2. Exponent **
  3. Multiplication *
  4. Division / // %
  5. Addition +
  6. Subtraction -
  '''


# %%
4 % 2 # for check reminder


# %%
'''variable assign'''

x = 5
y = x+x
print([x,y])


# %%
'''now we understand about string
string are mention in 'string01' ,
"string02" , ''''''. 
'''
a =  "welcome in python"
print(a)


# %%
# string
"python programing language"


# %%
# here is another way to put value in string via format
name = 'sam'
age = 25
print('my name is {} and my age is {}'.format(name,age))


# %%
# for formating order in sequence way
name = 'sam'
age = 25
print('my name is {one} and my age is {two}'.format(one = name, two=age))


# %%
# for indexing in python
a = 'python'

# here index is start from 0 and end on -1


print(a[0]) # for print index 0 value
print(a[0:2]) # for print in specific range
print(a[:3]) # for print starting to 3
print(a[3:5]) # for specific range


# %%
# list
# list is mutable / means value can change
# list can work liae as array but it can also store strings

list_of_string = ['nik','vik','dik']
list_of_string.append('gil') # append for add something on the end of list
print(list_of_string[:1])# for print range in specifc order
print(list_of_string[0:2])


# %%
nest_list = [1,2,['nik','amit',[52,'amff','sim']]]
print(nest_list[2][0]) # here in this we can extract element from a list to list
print(nest_list[2][2][1]) # extract element from list to list to list


# %%
# example of mutable
lst  = [1,2,3,5]
print(lst[1])
lst[3] = 'python' # so here we chnage the index value of list 3 to python this is mutable 
print(lst)


# %%
# data type  - Dictionaries - {}
#to understand Dictionaries better you can compare it with phone book diary
d = {'key1':'value','key2':'value'} # here we are going to assign a key and value
d['key1']


# %%
# Dictionaries
dic = {'k1':[1,2,3]} # assign multiple value to dictonary
dic['k1'][0] # here in this we can extract the value via indexing


# %%
# Dictionaries

value = {'key':{'phone_key':[2236,2525,1155,4154]}}
print(value['key']) # for find the value of key
print(value['key']['phone_key'][2]) # extract specific key number

 


# %%
# Data type tupple   -   ()
# tupple is imutable

a = (52,12,'nik') # after asign a tupple you can change the variable
a


# %%
# data type - set {}
# main thing about set is data are unique in it.
s = {1,2,5,5,1,2,2,5,1,6,51,2,3,5} # in this set it will only capture unique element not repeted element
s.add(385) # add function is use to add something on last element in set
s


# %%




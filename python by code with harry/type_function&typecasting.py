a = 34
type(a) # this will give <class 'int'>
b = 3.5
type(b) # this will give <class 'float'>
c = "Hello"
type(c) # this will give <class 'str'>
# conversion
str(32) # this will convert integer 32 to string '32'
print(type(str(32))) # this will give <class 'str'>
a = 32.05
t = int(a) # this will convert float 32.05 to integer 32
print(t) # this will print 32
a = "123"
b = float(a)
print(b)
t = type(b)
print(t) # this will give <class 'float'>
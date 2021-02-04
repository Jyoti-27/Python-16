#!/usr/bin/env python
# coding: utf-8

# # Encapsulation
# ### Encapsulation in Python
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data. To prevent accidental change, an object’s variable can only be changed by an object’s method. Those type of variables are known as private variable.
# 

# - A class is an example of encapsulation as it encapsulates all the data that is member functions,variables,etc.

# In[2]:


class Car:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color
ford = Car(200,'Red')
Chev = Car(180,'Blue')
Aud1 = Car(190,'Black')

ford.speed = 300

print(ford.speed)
print(ford.color)


# In[3]:


class Car:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color
ford = Car(200,'Red')
Chev = Car(180,'Blue')
Aud1 = Car(190,'Black')

ford.speed = "sakakak"

print(ford.speed)
print(ford.color)


# # Did it makes any sense?
# - No
# - That's where encapsulation comes into picture.
# - Now let's see how to encapsulate our code.
# - To do that we have to create a function

# # Setter- to set the values
# # Getter- to get the values

# In[4]:


class Car:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color
        
    def set_speed(self,value): # Seeter for the attribute speed
        self.speed = value
        
    def get_speed(self):   # Getter for the attribute speed, to get this we don't have to pass any arguments.
        return self.speed
    
ford = Car(200,'Red')
Chev = Car(180,'Blue')
Aud1 = Car(190,'Black')

ford.set_speed(400)
ford.speed = 500
print(ford.get_speed())


# - There are 3 types of members here public, private and protected
# - The way you declare them shows what type of members they are
# - Even though we declared some members as protected,nothing can stop us from calling them
# 

# - Here the attribute __c can be used to make your attribute private.
# - No keywords like private exists in Python.Whenever you use double underscores it makes your data private.
# - When you use single underscore also it makes it private but nothing can stop you from changing the value of _b or accessing      _b
# - So if you truely want to make your data private please use double underscores in front of your variable.

# In[8]:


class Hello:
    def __init__(self,name):
        self.a = 15
        self._b = 30
        self.__c = 40
        
hello = Hello('name')
print(hello.a)
print(hello._b)
print(hello.__c)


# - Getter can be used to get some values. 
# - Setter can be used to modify values.

# In[14]:


class Car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color
        
    def set_speed(self,value): # Seeter for the attribute speed
        self.__speed = value
        
    def get_speed(self):   # Getter for the attribute speed, to get this we don't have to pass any arguments.
        return self.__speed
    
ford = Car(200,'Red')
Chev = Car(180,'Blue')
Aud1 = Car(190,'Black')

ford.set_speed(400)
ford.__speed = 500
print(ford.get_speed())
print(ford.color())


# - From the above it is clear that you can not access color because now it is a private attribute.
# - Now you can create setter and getter method for color also.

# In[11]:


class Car:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color
        
    def set_speed(self,value): # Seeter for the attribute speed
        self.__speed = value
        
    def get_speed(self):   # Getter for the attribute speed, to get this we don't have to pass any arguments.
        return self.__speed
    
    def set_color(self,value): # Seeter for the attribute speed
        self.__color = value
        
    def get_color(self):   # Getter for the attribute speed, to get this we don't have to pass any arguments.
        return self.__color
    
ford = Car(200,'Red')
Chev = Car(180,'Blue')
Aud1 = Car(190,'Black')

ford.set_speed(400)
ford.__speed = 500
print(ford.get_color())


# # Protected Members
# - Protected Members (in C++ and JAVA) are those members of the class which cannot be accesssed outside the class but can be accessed from within the class and it's subclasses. To accomplish this in python,just follow the convention by prefixing the name of the member by a single underscore"_".

# In[15]:


# Creating a base class 
class Base: 
    def __init__(self): 
          
        # Protected member 
        self._a = 2

# Creating a derived class     
class Derived(Base): 
    def __init__(self): 
          
        # Calling constructor of 
        # Base class 
        Base.__init__(self)  
        print("Calling protected member of base class: ") 
        print(self._a) 

obj1 = Derived() 
          
obj2 = Base() 
  
# Calling protected member 
# Outside class will  result in  
# AttributeError 
print(obj2.a)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





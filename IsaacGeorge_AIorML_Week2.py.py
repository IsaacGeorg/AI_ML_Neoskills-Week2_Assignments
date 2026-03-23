#!/usr/bin/env python
# coding: utf-8

# ## Task1: Basic Operations

# In[4]:


x = int(input("Enter the first number: "))    #gather x input from user (only integer values)
y = int(input("Enter the second number: "))   #gather y input from user (only integer values)

add= x+y
sub= x-y
mult= x*y         #performing basic operations
div= x/y
modulus= x%y
expon= x**y


#printing basic operations
print(f"Addition: {add}\nSubtraction: {sub}\nMultiplication: {mult}\nDivision: {div}\nModulus: {modulus}\nExponential: {expon}")


# ## Task2: Working with Lists and Arrays

# In[5]:


list1 =[5,38,49,35,27,15,48,2,57,35]      # creating a list
print(f"Length of the list, List1: {len(list1)}")   #print the length of the list


# In[7]:


print(f"Maximum value in list1: {max(list1)}\nand Minimum value of list1: {min(list1)}")  # prints the maximum and minimum values of the list, list1


# In[8]:


list1.append(18)    # add a value to list1
list1.remove(15)    # removing the value 15
print(list1)        # prints the list1


# In[14]:


asc= sorted(list1)                     # sort function to sort in ascending order
desc= sorted(list1,reverse= True)      # sort function to sort in descending order
print(f"Ascending order of list1: {asc}\nDescending order of list1: {desc}")    # prints the ascending and descending ordered list


# In[26]:


import numpy as np              #importing numpy package from python
print(list1)
array1= np.array(list1)         # converts the list1 to array using numpy as np
mean_value=np.mean(array1)      # calculate mean, median, standard deviation of array1
median=np.median(array1)
sd= np.std(array1)
print(f"Mean value: {mean_value}\nMedian value: {median}\nStandard Deviation: {sd}") #prints mean, median,standard deviation


# ## Task3: Dictionaries and Sets

# In[32]:


student={"name":"Jacob", "age": 27, "course": "Blockchain", "marks":56}      #created a dictionary
for k,v in student.items():                                            #using for loop printed key value pairs
    print(f"{k}:{v}")


# In[34]:


student["Grade"] = "B" # Adding a key-value pair to the dictionary student
print(student)


# In[35]:


Unique_courses = {"Blockchain","Marketing","IoT","AI","Python","Fullstack","IoT"}   # Adding a set of unique courses
print(f"Set of Unique courses= {Unique_courses}")


# In[41]:


d1={34,5,2,67,48,6,8,16,20,57}
d2={37,2,49,32,37,57,39,12,93}               # created two sets d1 and d2
Uni = d1.union(d2)                           # finding union, intersection, difference of set d1 and d2
inter = d1.intersection(d2)
diff = d1.difference(d2)
print(f"Union of 2 sets: {Uni}, Intersection of 2 sets: {inter}, Difference of 2 sets: {diff}")


# ## Task 4: File Handling

# In[44]:


with open("student_data.txt", "w") as f:                           # creating the file student_data.txt and uses w function
    f.write("Name: Maya, Course: Maths, Marks:68 \n")
    f.write("Name: Rudra, Course: Mechanics, Marks:76 \n")          # writing the contents of the file
    f.write("Name: Ragini, Course: Cloud Computing, Marks:91 \n")
    f.write("Name: Sheetal, Course: Python, Marks:50 \n")
    f.write("Name: Angel, Course: Maths, Marks:80 \n")
print("File created")


# In[45]:


with open("student_data.txt", "r") as f:                          # reading the student_data.txt file by using r function
    data= f.read()
    
print(data)


# In[46]:


with open("student_data.txt","r") as f:
    for line in f:                                        # uses a for loop to iterate line by line in the file
        parts=line.split(",")                             # splits the line into parts whenever a comma(,) came
        marks_part = parts[2]                             # takes up the marks part which lies in 2nd index
        marks = int(marks_part.split(":")[1])              # again splits the marks part to get the marks (only integer values)
        name_part=parts[0]                                 # takes the name part which lies in 0th index
        name = name_part.split(":")[1].strip()    # only takes the name and the strip function is used to remove the extra space
        
        if marks>75:
            print(name,marks)


# In[ ]:





# # String operation

# # str=""#falsy empty
# # str="abc"#truy having value

# str="hello world \n How are you.."
# print(len(str))
# words_count=str.split()
# print(words_count)  #written in list

# print(len(words_count))

# #count the new line 
# no_of_newline= str.count('\n')
# print(no_of_newline)

# #number of spaces
# no_of_spaces= str.count(' ')
# print(no_of_spaces)

#FILE HANDLING

# open("filename",'mode')  It used for opening file with filename and modes
# fileObj=open('filename','mode') 

# print(r"") using r in starting is for raw string 
# fileObj=open(r'C:\Users\subod\Internship 2024-25\demo.txt','r')#reading file  
# for i in fileObj:
#     print(i)
    # print(i.strip()) # reduces spaces from tailing(lft) and heading(rght)

#1
# print(fileObj.read()) #built in method for reading file. 

#2
# readline() 
# while True:
# line=fileObj.readline()
#     if not line:
#         break
#     print(line.strip())  #strip() for removing spaces

#3
# lines=fileObj.readlines() #read multiple lines in the form of list['','','','']
# print(len(lines))



# import os,sys #used for checking file is given or not 
# if os.path.isfile(r'C:\Users\subod\Internship 2024-25\demo.txt'):
#     print(True)
# f=open(r'C:\Users\subod\Internship 2024-25\demo.txt','w')
#     print(f.read())
#     f.close()  #it will close the file. close the file after every read function 
# else:
#     print("File is not found ")

#with resources
# temp_str=""
# str=input("Enter the data into file")
# with open(r'C:\Users\subod\Internship 2024-25\demo.txt','w') as f :
#     # f.write("My name is subodh wadekar")
#     f.write(f"{str}")

# with open(r'C:\Users\subod\Internship 2024-25\demo.txt','r') as f2 :
#     print(f2.read())
#     f2.seek(0) # explicitly moves pointer to starting after going to end of thr file means 0
#     f2.tell()   #it tells the pointer location in file
#     print(f2.readline())



# with open("demo2.txt",'w') as f3:
#     f3.write()


#all read operation  we can perform
#By this way we no need to close file manually ,it closes automatically
#Writing in file 'w' 

#TASK make paragraphs
#count characters done
#count words done
#no of new lines done 
# no of spaces done
#using file handling



# input::::::The margin clears an area around an element (outside the border).
# \n The margin does not have a background color, and is completely transparent.
# \n The top, right, bottom, and left margin can be changed independently using separate properties.
# \n A shorthand margin property can also be used, to change all margins at once.
# \n It is also possible to use negative values, to overlap content

import sys
print("Enter your string to enter in the data file: ")
str=sys.stdin.read()
# str=input(""" """)
# with open(r'C:\Users\subod\Internship 2024-25\demo.txt','r'):
print("*********************************************************")
    # print(f"Count of the characters: {len(str)}")
    # words_counts=str.split()
    # print(f"Words count are:{len(words_counts)}")
    # print(f"Count of New Lines:{str.count('\n')}")
    # print(f"count of spaces:{str.count(' ')}")


with open(r'C:\Users\subod\Internship 2024-25\demo2.txt','w+') as f1:
    f1.write(f"Input:{str}")
    f1.write("******************************\n")
    f1.write(f"Count of characters are:{len(str)}\n")
    words_counts=str.split()
    f1.write(f"Words count are:{len(words_counts)}\n")
    no_of_newline= str.count('\n')
    f1.write(f"counts of new lines:{no_of_newline}\n")
    f1.write(f"count of spaces:{str.count(' ')}\n")

    f1.seek(0)
    print("0:pointer starts from here")
    


with open(r'C:\Users\subod\Internship 2024-25\demo2.txt','r+') as f2:
    while True:
        line=f2.readline()
        if not line:
            break
        print(line.strip())
    f2.write("This is file mode (r+) where we can read and then write after it\n")

with open(r'C:\Users\subod\Internship 2024-25\demo2.txt','a+') as f3:
    f3.write("These are the string methods which we learned\n")





















#to upload image to python file
#  from IPython.display import I 

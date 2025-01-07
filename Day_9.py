#File handling

data=b"0101001"
with open(r'C:\Users\subod\Internship 2024-25\demo2.bin','wb')as f:
    f.write(data)
    f.write(b'1111111')
    
    with open(r'C:\Users\subod\Internship 2024-25\demo2.bin','rb') as f2:
        print(f"binary code{f2.read()}")

        # TASK:
        # convert an image and store it in file




#by this way we can store structured data in files
#to save the state of object like username,password(useful data) we use pickle,unpickle
#serilaization,deserializatrion






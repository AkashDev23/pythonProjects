with open("my_file.txt")as file:
    contents=file.read()
    print(contents)
    
with open("my_file.txt", mode="a") as file:
    #r is used to read the file and it's also the default
    #w is used whenever we need to write into the file. The previous data will be deleted. If this file isn't created then this will create a new file for us with this name. 
    #a is used to append in the file. The previous data won't be deleted just new data will be appended over the previous data. 
    file.write("Hello how are you")
    
    
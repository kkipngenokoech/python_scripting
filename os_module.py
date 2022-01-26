#python scripting
"""
it coordinates the behaviour of other programs
"""
import os
print(os.getlogin())#tells you about the user
print(os.getcwd())#gives you the current working directory
os.chdir("C:\\Users\\kip\\Documents\\LETS LEARN\\phyton")#changes the directory of the file
print(os.getcwd())
#os.mkdir("C:\\Users\\kip\\PycharmProjects\\python_scripting\\made_directory")#adds a directory to the path
#os.rmdir("C:\\Users\\kip\\PycharmProjects\\python_scripting\\made_directory")#deletes a directory to the path
print(os.getcwd())
os.chdir("C:\\Users\\kip\\PycharmProjects\\python_scripting")
#os.remove("C:\\Users\\kip\\PycharmProjects\\python_scripting\\sys_module.py")=removes a file from the directory
#print(os.path.join("C:\\Users\\kip\\PycharmProjects\\python_scripting\\os_module.py","C:\\Users\\kip\\PycharmProjects\\python_scripting\\sys_module.py"))
#the above line of code joins both paths and the below one splits
#print(os.path.split("C:\\Users\\kip\\PycharmProjects\\python_scripting\\sys_module"))
print(os.path.exists("C:\\Users\\kip\\PycharmProjects\\python_scripting\\os_module.py"))#twlls you if the path exists or not

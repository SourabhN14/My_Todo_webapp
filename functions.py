#def get_todo():
FILEPATH = "todos.txt"
# thsi can help to centralize the file path defination so if in
# future it needs to eb changed it can be done at one place itself
def get_todo(filepath = FILEPATH):
    """
    It read a text file and return a list of todos
    It is docstring
    """
    #with open("todos.txt",'r') as file:
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos

#print(help(get_todo)) # this way we can get the help detaisl of function get_todo
# it will give docstring as output

text = """
principal of productivity
Managing your inflow
Systemizing everything that repeats  
"""
print(text) # this will print doc string as is without any quotes
#def write_todo(filepath , todos_arg):
def write_todo(todos_arg,filepath = FILEPATH): # the non default shall be priority and only if non default can be passed
                                                 # then also it will work
    with open(filepath,'w') as file:
        file.writelines(todos_arg)

# this conditional block , the value of __name__ is "__main__"
if __name__ =="__main__":
    todos = get_todo("todos.txt")
    print(todos)
#python debugger
# Common pdb commands:
 
# n (next): Execute the next line
# s (step): Step into function calls
# c (continue): Resume execution
# q (quit): Exit the debugger

import pdb
 
def test():
    x = 10
    pdb.set_trace()  # Start debugger
    y = 20
    result = x + y
    print(result)
 
test()
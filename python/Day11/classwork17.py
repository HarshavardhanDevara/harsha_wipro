#print("*******************")
 
def make_pretty(func):
 
    def inner():

        print("********************")

        func()

        print("********************")

    return inner
 
@make_pretty

def ordinary():

    print("I am ordinary")
 
ordinary()  

 
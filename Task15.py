#Task 1:- This is Three nested functions 
def outer_fun():
    print("we are inside the outer function")
    def inner_fun():
        print("we are inside the inner function")
        def super_inner_fun():
            print("we are inside the super inner function")
        return super_inner_fun
    return inner_fun
super_inner_fun  = outer_fun()()   # call outer_fun(), then call what it returns
print(super_inner_fun)            
super_inner_fun()                  # actually run it

# Task 2 :- This is a four nested function
def outer_fun():
    print("we are inside the outer function")
    def inner_fun():
        print("we are inside the inner function")
        def super_inner_fun():
            print("we are inside the super inner function")
            def extra_super_inner_fun():
                print("we are inside the extra super inner function")
            return extra_super_inner_fun
        return super_inner_fun
    return inner_fun
extra_super_inner_fun  = outer_fun()()()   # call outer_fun(), then call what it returns
print(extra_super_inner_fun)               # prints the function object (not called yet)
extra_super_inner_fun()                    # actually run it


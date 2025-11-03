def outter_function():
    var1 = 30
    def inner_function():
        var2 = 40
        print(var1, var2)
    def inner_function2():
        var3 = 50
        print(var1,var3) #var2 cannot be included because of another local variable , local variable also have scope to each function

    inner_function()
    inner_function2()

outter_function()
#inner_function() # because of inner function scope it cannot be accesed/called outside the scope
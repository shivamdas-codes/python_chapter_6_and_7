# # method 1
# #function defination
# def var_name(a,b):  #defination with parameters a and b
#     result1 = a + b
#     result2 = a - b
#     print(result1,result2)  

#     return result1,result2  # return is used to send a value back from a function to the place where it was called. 

# var_name(5,10)  #printing the arguments with the given a and b
# var_name(10,5)  #printing the arguments with the given a and b


# method 2
# function defination
def new_var(num1 , num2):   #parameters
    return num1 + num2

sum = new_var(10,17)    #function call, arguments
print(sum)
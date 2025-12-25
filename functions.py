# method 1
#function defination
def var_name(a,b):  #defination with parameters a and b
    result1 = a + b
    result2 = a - b
    print(result1,result2)  

    return result1,result2  # return is used to send a value back from a function to the place where it was called. 

var_name(5,10)  #printing the arguments with the given a and b
var_name(10,5)  #printing the arguments with the given a and b


# method 2
# function defination
def new_var(num1 , num2):   #parameters
    return num1 + num2

sum = new_var(10,17)    #function call, arguments
print(sum)


# method 3
def null_value():   #no parametres assigned
    print("hello")

output = null_value() #the value which doesn't return anything it is consider as 'none'
print(output)
null_value()    #function call nothing here....
# this function doesnt return anything so python takes it as "NONE"

# -------------------------------------------------------------------------------------------------------------------------


# average of three numbers:
def numbers(a,b,c):
    average = a + b + c / 3
    print(average)

    return average
numbers(5,6,7)



# default parameters:
# example1:
def new_var(a,b):
    print(a*b)
    return(a*b)
new_var() 
# in this case it will always throw error because we didn't give any kind of arguments here

# example2:

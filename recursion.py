# # example program:
# def show(n):    #given parameter as 'n'

#     if n == 0:  #the recursion should perform till "0"                 "this is also known as BASE CASE"             
#         return  #after completion of recursion it will return the value to the "n"
#     """ in recursion the BASE CASE is very important if there is no base case then there is a chance that code will get crash """
   
#     print(n)
#     show(n-1)   #here the numbers will print in desending order.
#     # show(n-1)
#     # print(n)    #here it will print in ascending order.
# show(5) #calling 5 as argument



# recursion using factoriol:
def fact(n):
    if n == 1 or n == 0:
        return 1    #default value
    return fact(n-1) * n    
print(fact(5))



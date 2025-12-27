# example program:
def show(n):    #given parameter as 'n'
    if n == 0:  #the recursion should perform till "0"
        return  #after completion of recursion it will return the value to the "n"
    print(n)
    show(n-1)   #here the numbers will print in desending order.

    show(n-1)
    print(n)    #here it will print in ascending order.
show(5) #calling 5 as argument

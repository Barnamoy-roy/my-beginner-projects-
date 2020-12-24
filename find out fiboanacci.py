# fibonacci series

# the code for fiboanacci series is very small but it takes some time to understand the logic behind it

num1 = 0
num2 = 1
# creating a list with element 0 because it is not included in the code
fibonacci_list = [0]                                 # printing basic 0 and 1
for i in range(1, 20):                              # here we are printing the series for 20 terms
    result = num1 + num2                            # result is the sum of num1 and num2
    num2, num1 = num1, result                       # now we interchange the values of num1 and num2 to modify the result
    fibonacci_list.append(result)                   # now we print the result to get the fibonacci series

element = int(input("enter the number you want to find: "))            # basic code to check if the entered element belongs to the fibonacci series or not
if element in fibonacci_list:
    print("the element belong to the list and the position of the element is" , fibonacci_list.index(element))
else:
    print("sorry the element dosent belong to list")             # using if and else statements and also the index function of the lists for a more specific answer


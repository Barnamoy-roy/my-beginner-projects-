#binary search code

# gives the position of a element in a list or any other storing function and its index pos
# idea is to take a middle element of the array and then compare it to other elements to find the desired element
# depending upon position of the element and the mid index of array we manipulate to change the mid index to find the element

def search(list, element):      #calling a function with parameters list and element
    lower = 0
    higher = len(list)-1
    mid = 0                     # lower, mid are initially set to 0 and higher is the length of the string -1

    while lower <= higher:               # using a while loop to iterate till lower is greater than higher
         mid = (lower + higher) // 2     # mid index of the list is sum of lower and higher divided by 2
         if list[mid] == element:        # setting a condition if the element belongs to the index num of mid then we have to return mid
            return mid

         else:
            if list[mid] > element:      # if index of mid is grater than element pos then we manipulate the higher value
               higher = mid -1
            elif list[mid] < element:
                lower = mid +1           # if the index of mid is smaller than element pos then we manipulate the lower value
    return "element dosent belong to list"   # if the element dosent belong to list then we print the line saying that the element dosent belong to list

list = ["sample list"]
print(search(list, element))            # the sample list is given plz input ur own list


   #basically we iterate the list over and over till the mid index belongs to the position of the element

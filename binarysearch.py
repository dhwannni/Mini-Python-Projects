#a function that takes a list and target parameter 
#multiple variables : mid, start, end, steps (loop count)
#recursion or while loop 
#increase the steps each time a split is finished
#add conditions ->track the target position

#define a variable binary search and that has a list and element 
def binary_search(list, element):
    start = 0
    middle = 0
    end = len(list)
    steps = 0
#keep going through the loop until the start is less than the end 
    while (start <= end):
        print("Step", steps, ":", str(list[start:end+1]))#showing the list from start and the end 
        steps +=1 
        middle = (start + end)//2

        if element == list[middle]: #if the mean is equal to element 
            return middle
        if element <list[middle]: 
#if element < mean, the end is one less than the mean, making it a new list b/c end is the length of the list and makes the list smaller
            end = middle-1
        else: 
            start = middle +1
#if the element is not equal or less, so it is greater, the start becomes the mean +1 
    return -1

#test
mylis = [1,2,3,4,5,6,7,8,9,5,6,7,12]  
target = 9
binary_search(mylis, target)         
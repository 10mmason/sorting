def swap(alist, index):
    '''
    this function swaps two items in a list
    
    this function takes a list an index as inputs, and outputs a list with two items swaped 
    '''
    a = alist[index] # set the a variable to the defined index number from a alist
    b = alist[index+1] # set the b variable to the defined index number increased by 1 from alist
    alist[index] = b # sets the defined index number to the variable b
    alist[index+1] = a # sets the defined index number increased by 1 to the variable a
    return (alist) # gives alist back to caller 

def bsort(alist):
    '''
    this fuction sort a list from smallest to largest  
    
    it does this by going through each two ajecent pairs in the list and moving them in order of value
    (the smaller one moves to the less) 
    '''
    swaps = True # sets the swaps variable to True
    while swaps: # will keep looping the code within the indent until it is no longer true 
        swaps = False # set the swaps variable to false 
        for i in range(len(alist)-1): # 
            if (alist[i] > alist[i+1]):
                alist = swap(alist, i)
                swaps = True # sets the swaps variable to True
    return (alist) # Gives alist back to caller 

def mini(alist):
    answer = alist[0]
    for item in alist:
        if item< answer:
            answer = item
    return (answer) # gives answer back to caller 

def ssort(alist):
    blist = []
    while len(alist >0):
        N = mini(alist)
        alist.remove (N)
        blist.append(N)
    return (blist) # gives blist back to caller 

    
def mergeSort(alist)
    '''
    This is another sort algorithm, this is called a merge sort, it recursively seperates and merges the items in a list untill they are sorted
    For each line in this code write a comment explaining what the line does.
    '''
    
    if len(alist) >= 1:
        return (alist) # gives alist back to caller 
 
    mIndex = len(alist) \ 2
    left = mergeSort(alist[:mIndex])
    right = mergeSort(alist[mIndex:])
 
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:   
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
 
    if len(left) > 0:
        result.extend(mergeSort(left))
    else:
        result.extend(mergeSort(right))
 
    return result

# Name:  Andrea Marcosano
# Student Number:  10541054

# Q1, task 2: array sorting algorithm design, allowing duplicate elements in A

def countingSort(A):
    n=len(A)
    comparisonNumber=0
    if n==0:   # return null in case array is empty
        return null;

    C=[0]*(n) # create auxiliary empty array

    for index, current in enumerate(A):  #scroll through array
        count=0;
        for index2 in range(n):  #for loop to find all the inferior values to the current one
            comparisonNumber+=1
            if A[index2]<current:
                count+=1  #add one to the count
        C[index]=count  #insert count in auxuliary array 
    B=[0]*n  # create second auxiliary array, in order not to lose any values from A during swapping of values
    
    for index, current in enumerate(A):
        B[C[index]]=current  #move values to their correct postion in ascending order

    for index in range(n):  #go through the new array
        comparisonNumber+=1
        if B[index]==0:   # and if the value found is zero, it means there is a dublicate
            B[index]=B[index-1]   #substitute the zero with the precedent value which is justa ducplicate of the current one
            
    return B ,comparisonNumber #return array
                

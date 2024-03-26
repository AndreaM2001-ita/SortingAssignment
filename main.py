# Name: Andrea Marcosano
# Student Number: 10541054

#This si the main file for assingment 2 of Data structures and algorithms

#importing external srtoing algorithm provided by Dr Jitian XIAO
from selectionSort import selectionSort
from insertionSort import insertionSort
from mergeSort import mergeSort
from quickSort import quickSort
from heapSort import heapSort
from countingSort2 import countingSort2 #import from question 1

import time #to record timing of execution
import random #import random to generate random array

#present main menu
def printMenu1():
    while True:
        print('MENU')
        print('1. Test an individual sorting algorithm')
        print('2. Test multiple sorting algorithms')
        print('3. Experimental studies')
        print('4. Exit')
        pick=int(input('Select option '))
        if pick>0 and pick<5:
            return pick
        else:
            print('Error.. try again')
#function to print the menu needed for testing individual sorting algorithm
def printSubMenu1():
    while True:
        print('SUBMENU 1')
        print('1. selection sort')
        print('2. insertion sort')
        print('3. merge sort')
        print('4. quick sort')
        print('5. heap sort')
        print('6. counting sort')
    
        pick=int(input('Select option '))
        if pick>0 and pick<7:
            return pick
        else:
            print('Error.. try again')
# function to verify that the input for the main menu is taken correctly
def menu(subMenu):
    while True:
        try:
            return subMenu();
        except ValueError:
            print('invalid input, enter a digit')
            
#function to print separator
def separator():
    print("--------------------------------------------------------------------")

#function to validate the number enterred for length of array
def enterSize():
    while True:
        try:
            length=int(input('insert Length of array '))
            if length>0: #verify that number is greater than 0
                return length
            else:
                print('Error.. try again')
            
        except ValueError:
            print('invalid input, enter a digit')
#creation of array length n
def generateArray(size):
    array = []
    for count in range(size):
        array.append(random.randint(1, (size + 1)*10))
    #print(array)
    return array

def sort(sortingNumber, array):
    start_time = time.time()
    if sortingNumber==1:
        array,comparisonNumber=selectionSort(array)
    elif sortingNumber==2:
        array,comparisonNumber=insertionSort(array)
    elif sortingNumber==3:
        array,comparisonNumber=mergeSort(array)
    elif sortingNumber==4:
        array,comparisonNumber=quickSort(array)
    elif sortingNumber==5:
        array,comparisonNumber=heapSort(array)
    else:
        array,comparisonNumber=countingSort2(array)
    
    end_time = time.time()

    elapsed_time = (end_time - start_time)*1000000
    print(array)
    print ('The number of comparison was ', comparisonNumber)
    print('time of execution: ', f"{elapsed_time:.5f}","us")

#functgion to print the heading of the table
def printTable(results_values):

    #headers of table
    headers = ['Sorting Algorithm name', 'Array Size', 'Number of comparison', 'Runtime (us)']

    #print headers
    headers_row='| '
    for header in headers:
        headers_row=headers_row+header+' | '
    
    print('-'*(len(headers_row)-1))
    print(headers_row)
    print('-'*(len(headers_row)-1))

    #prin values
    for values in results_values:
        row='| '
        count=0
        for key, value in values.items():
            space=(len(headers[count])-len(value))

            row=row+value+space*' '+' | '
            count+=1
        print(row)
        print('-'*(len(headers_row)-1))

#calculate values of the different sorting alrorithms 
def getValues(array,algorithmName):
    start_time = time.time() #start time

    array,comparisonNumber=algorithmName(array) #get algorithm 

    end_time = time.time() #end time
    elapsed_time = (end_time - start_time)*1000000 #calculate time

    #create dictionary with results
    results = {
        'Sorting': algorithmName.__name__, 
        'Array Size':str(len(array)),
        'Comparison':str(comparisonNumber),
        'Elapsed Time': f"{elapsed_time:.2f}",
    }

    return results

#fucntion to manage the values within the dictionary to make it easy to print out
def parseValues(timing_results):
    results_values=[]
    for algorithm in timing_results:
        results_value = {'Sorting': algorithm['Sorting'],
                          'Elapsed time':algorithm['Elapsed Time']}
        results_values.append(results_value)

    
    # initialise  dictionary
    results_dict = {}

    #i terate over current dictionary values
    for values in results_values:
        sorting_algorithm = values['Sorting']
        elapsed_time = values['Elapsed time']
        if sorting_algorithm in results_dict:# checking if soprting algo is already in dictionary 
            results_dict[sorting_algorithm].append(elapsed_time) # if it is add the elapsed timne
        else: 
            results_dict[sorting_algorithm] = [elapsed_time]# if it not add the new list with elapsed times

    return results_dict
        

#function to print the table with the timing results
def printExperimentalValues(timing_results):
    #headers of table
    headers = ['Sorting Algorithm name',' n=100 ','  n=200  ','  n=400  ','  n=800  ',' n=1000 ',' n=2000 ',]

    #print headers
    headers_row='| '
    for header in headers:
        headers_row=headers_row+header+' | '
    
    print('-'*(len(headers_row)-1))
    print(headers_row)
    print('-'*(len(headers_row)-1))

    timing_results=parseValues(timing_results)

    for algorithm, values in timing_results.items():
        count=0
        spaceFirst=(len(headers[count])-len(algorithm))
        row = "| "+algorithm+spaceFirst*' '+" | "
        for value in values:
            count+=1
            space=(len(headers[count])-len(value))
            row=row+value+space*' '+' | '
            
            
        print(row)
        print('-'*(len(headers_row)-1))
    
#main
if __name__== '__main__':
    while True:
        pick=menu(printMenu1);
        separator();
        
        #switch menu
        if pick==1:
            sortingNumber=menu(printSubMenu1);
            length=enterSize();
            array=generateArray(length);
            print(array)
            sort(sortingNumber,array);
        elif pick==2:
            
            length=enterSize();
            array=generateArray(length);
            sortingAlgorithms=[selectionSort, insertionSort,mergeSort,quickSort,heapSort,countingSort2]
            results_values=[]
            for current in sortingAlgorithms:
                results_values.append(getValues(array,current))
            printTable(results_values);
        elif pick==3:
            sortingAlgorithms=[selectionSort, insertionSort,mergeSort,quickSort,heapSort,countingSort2]
            print("Ongoing experimental studies")
            array_lengths=[100,200,400,800,1000,2000]
            timing_results=[]
            for current in sortingAlgorithms:
                for array_length in array_lengths:
                    array=generateArray(array_length);
                    timing_results.append(getValues(array,current))
            
            printExperimentalValues(timing_results)


        else:
            print("Program is exiting...")
            break

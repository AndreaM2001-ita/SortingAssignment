# Name: Andrea Marcosano
# Student Number: 10541054

#This si the main file for assingment 2 of Data structures and algorithms

#importing external srtoing algorithm provided by Dr Jitian XIAO
import insertionSort
import selectionSort
import mergeSort
import quickSort
import CountingSort2 #import code from question 1

import random #import random to generate random array

#present main menu
def printMenu1():
    while True:
        print('MENU')
        print('1. Test an indivisual sorting algorithm')
        print('2. Test multiple sorting algorithms')
        print('3. Exit')
        pick=int(input('Select option '))
        if pick>0 and pick<4:
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
        print('5. counting sort')
    
        pick=int(input('Select option '))
        if pick>0 and pick<6:
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
    print('-------------------------------------------------')

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
    print(array)
    return array

def sort(sortingNumber, array):
    if sortingNumber==1:
        array,comparisonNumber=selectionSort.SelectionSort(array);
    elif sortingNumber==2:
        array,comparisonNumber=insertionSort.InsertionSort(array)
    elif sortingNumber==3:
        array,comparisonNumber=mergeSort.mergeSort(array);
    elif sortingNumber==4:
        array,comparisonNumber=quickSort.quicksort(array);
    else:
        array,comparisonNumber=CountingSort2.countingSort(array);
    print(array);
    print ('The number of comparison was ', comparisonNumber)
        

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

            sort(sortingNumber,array);
            
            
        elif pick==2:
            print('option 2')
        else:
            print('option 3')

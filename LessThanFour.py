## Author: Feras
## Description: A function that finds the numbers that are 
##  less than 4 and retruns a list whose values less than 4

def lessThanFour(intList):
    newList = [i for i in intList if i < 4]
    return newList
print(lessThanFour([1,5,2,4]))
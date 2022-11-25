# Write a Python function to sum all the numbers in a list.
# sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# Explanation:
# Summation should like 8+2+3+0+7 = 20
def sum(n):
    lst=[]
    output=0
    for i in range(n):
        ele=int(input("enter the elements:"))  #enter the elements
        lst.append(ele)
    for i in lst:
        output=i+output
    print(output)
n=int(input("enter the number of elements:"))  #how many elements enter into a list
sum(n)




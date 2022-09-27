#Amaan Razi HMWK #1
#testSumList.py

def sumList(nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

def main():
    nums = [5,2,4,7]
    print(sumList(nums))
    nums = [4,524,42,562]
    print(sumList(nums))
    nums = [3,5,63,733]
    print(sumList(nums))
    nums = []
    print(sumList(nums))


main()

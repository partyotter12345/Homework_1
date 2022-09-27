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
    nums = []
    print(sumList(nums))


main()

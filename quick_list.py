nums=[1,2,3,4,5]
nums2=[1,2,3,4,5,[7,8]]
empty=[]
def checkfive(nums):
    if 5 in nums:
        print("The number 5 is in the list")
    else:
        print("The number 5 is not in the list")
def first_last(nums2):
    print("%r is first, %r is last in the list"%(nums[0],nums[-1]))

checkfive(nums)
first_last(nums2)
nums=[1,2,3,4,5]
nums2=[1,2,3,4,5,[7,8]]
empty=[]

##def checknested(x,y):
##    if y in x:
##        print('Nested list found')
##    else:
##        print('Nested list not found')

def checkfive(x):
    if 5 in x:
        print('5 is in your list')
    else:
        print('5 not in list')

def first_last(x):
    print('The first entry is %r, last entry is %r'%(x[0],x[-1]))

print('First list is %r'%nums)
print('Second list is %r'%nums2)

checkfive(nums)

first_last(nums)

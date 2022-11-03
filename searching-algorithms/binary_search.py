from cgitb import reset


def search(nums, target):
    
    left = 0              # left
    right = len(nums)-1    # right
    while left <= right:
        mid = int((left + right)/2)
        
        # test the middle against the target
        if nums[mid] == target:
            return mid
            
        # update left and right indicators
        else:
            
            # take the left part
            if target < nums[mid]:
                right = mid-1
            
            # take the right part
            else:
                left  = mid+1
                
    return -1



nums = [-1,0,3,5,9,12]
print(search(nums, 3))
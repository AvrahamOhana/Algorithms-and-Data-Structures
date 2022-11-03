def searchInsert(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = int((left + right)/2)
        
        if nums[mid]==target:
                return mid
            
        # update left and right indicators
        else:
            
            # take the left part
            if target < nums[mid]:
                right = mid-1
            
            # take the right part
            else:
                left  = mid+1
    return left
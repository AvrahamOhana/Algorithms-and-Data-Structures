# solve using modified binary search
def firstBadVersion(self, n: int) -> int:
        left = 0              # left
        right = n-1    # right
        while left <= right:
            mid = int((left + right)/2)
            
            # test the middle against the target
            if isBadVersion(mid):
                return mid
                
            # update left and right indicators
            else:
                
                # take the left part
                if nums[mid] < target:
                    right = mid-1
                
                # take the right part
                else:
                    left  = mid+1
                    
        return -1

        
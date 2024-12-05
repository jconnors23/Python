class Solution(object):
    def removeElement(self, nums, val):
        # Input: nums = [0,1,2,2,3,0,4,2], val = 2 01322042 c = 1 01302242 c = 2 01304222 c = 3 r 8 - c = 5  
        # Output: 5, nums = [0,1,4,0,3,_,_,_]
        # 3 2 2 3 2 3 2 3 
        # swap el = k with first el != k, increment count, once at last index return len(nums)-count
        # 2 3 3 3 3 - broken 
       if (len(nums) == 1):
        if (nums[0] != val):
            return 1 
        return 0
        count = 0 
        for i in range (len(nums)-1):
            if nums[i] == val:
                x = i+1
                for j in range (x, len(nums)):
                   # print(f"value of i: {i}, value of j: {j}")
                    if nums[j] != val:
                        #print(f"nums second check, before swap: {nums}")
                        nums[i] = nums[j]
                        nums[j] = val
                        #print(f"nums post swap: {nums}")
                        count+=1
                        break
        return len(nums)-count, nums

print(Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
#print(Solution().removeElement(nums = [3,2,2,3], val = 3))


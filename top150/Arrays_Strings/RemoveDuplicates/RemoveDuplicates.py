class Solution():
    def removeDuplicates(nums):
        count=0
        for i in range(len(nums)-1):
            val = nums[i]
            for j in range(len(nums)-1):
                if (nums[j] != nums[i]):
                    count+=1
                    nums[count] = nums[j]
                
print(Solution.removeDuplicates([0,0,1,1,2,2,3,3,4]))




    # """ i = 0, j = 2, num[i] = 0, num[j] = 1  0 0 1 1 2 2 3 3 4  0 1 0 1 2 2 3 3 4 
    #     :type nums: List[int]
    #     :rtype: int
    #     Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
    #     such that each unique element appears only once. 
    #     The relative order of the elements should be kept the same. 
    #     Then return the number of unique elements in nums.
    #     Input: nums = [0,0,1,1,1,2,2,3,3,4]  1 1 1 1 1 2 3 4 
    #     Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

    #     keep first occurence, 
    #     track index, count
    #     find occurence of next val !=, 
    #     swap to index track 
    #     update index track, count
    #     keep going until at index len(nums)-1
    # """
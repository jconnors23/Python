class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if m == 0:
            nums1 = nums2 
            return nums1
        placed = 0
        for i in range(m):
            for j in range(len(nums1)-1):
                if nums2[i]<=nums1[j]:
                    nums1.insert(j, nums2[i])
                    placed+=1
                    break
                elif nums1[j] == 0 and placed < m:
                    nums1.insert(j, nums2[i])
                    placed+=1
                    if placed == m:
                        nums1 = nums1[:m+n]
                        #print(f"reached: + {nums1}")
                    break 
        return nums1 

            
print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
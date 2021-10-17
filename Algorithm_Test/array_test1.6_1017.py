class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for num2 in nums2 :
            idx = m - 1
            while nums1[idx] > num2 and idx >= 0:
                temp = nums1[idx+1]
                nums1[idx+1] = nums1[idx]
                nums1[idx] = temp
                idx -= 1
            nums1[idx+1] = num2
            m = m + 1
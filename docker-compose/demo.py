from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer to track where to place non-val elements

        k = 0

        # Iterate over the array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Place the current element at the kth position
                nums[k] = nums[i]
                # Increment k
                k += 1

        return k

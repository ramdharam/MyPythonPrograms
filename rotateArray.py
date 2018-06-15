def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0:
        return
    l = len(nums)
    if k > l:
        return
    nums = nums[::-1]
    nums = nums[k - 1::-1] + nums[k:]
    print nums[:k:-1]
    nums = nums[:k] + nums[:k-1:-1]
    return


a = [1,2,3,4,5,6,7]
rotate(a, 3)
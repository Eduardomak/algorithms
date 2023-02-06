def find_duplicate(nums: list):
    """Faça o código aqui."""
    if not isinstance(nums, list) or len(nums) <= 1:
        return False
    nums.sort()
    for index in range(1, len(nums)):
        if type(nums[index]) != int or nums[index] < 1:
            return False
        if nums[index] == nums[index - 1]:
            return nums[index]
    return False
    """ raise NotImplementedError """

def twoSum(self, nums: List[int], target: int) -> List[int]:
  indices_needed = []
  
  for val in range(len(nums)):
    for new_val in range(val+1,len(nums)):
      if nums[val] + nums[new_val] == target:
        values_needed_one = val
        values_needed_second = new_val
        return values_needed_one,values_needed_second


      

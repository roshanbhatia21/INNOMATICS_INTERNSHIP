class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ones,twos = 0
	    for i in range(len(nums)):
            twos = twos ^ (ones & nums[i])
	        ones = ones ^ nums[i]
		    common_bit_mask = ~(ones & twos)
		    ones &= common_bit_mask
		    twos &= common_bit_mask
	    return ones
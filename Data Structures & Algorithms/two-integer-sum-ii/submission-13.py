class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen ={}
        for index,number in enumerate(numbers):
            needed = target-number
            if needed in seen:
                return[seen[needed]+1,index+1]
            seen[number]=index
        return[]
        
        
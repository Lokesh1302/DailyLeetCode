class Solution:
    def checkArithmeticSubarrays(self, nums, l: List[int], r: List[int]) -> List[bool]:
        result = []
        for index in range(len(r)):
            start_index = l[index]
            end_index = r[index]
            newList = [nums[i] for i in range(start_index, end_index + 1)]
            newList.sort()
            if len(newList) > 1:
                common_diff = newList[1] - newList[0]
                expected = newList[0]
                for i in range(1, len(newList)):
                    expected = common_diff + expected
                    if newList[i] != expected:
                        common_diff = -1
                        break
                if common_diff == -1:
                    result.append(False)
                else:
                    result.append(True)
        return result

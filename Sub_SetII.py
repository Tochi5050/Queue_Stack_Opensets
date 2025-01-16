class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = []
        sub_set = set()
        sub_set.add(tuple(nums))
        sub_set.add(())

        for i in range(len(nums)):
            append_val = [] + [nums[i]]
            stack.append((append_val, i))
            if tuple(append_val) not in sub_set:
                sub_set.add(tuple(append_val))
            # append_val = []

        while stack:
            num, start = stack.pop()

            for i in range(start + 1, len(nums)):

                if i != len(nums):
                    numb = num
                    print(numb, 'top')
                    sub_set.add(tuple(numb))
                    stack.append((numb, i))
                num.append(nums[i])
                print(num, 'below')
                new_num = tuple(num)
                if len(new_num) <= len(nums):
                    sub_set.add(new_num)
                # print(sub_set)
                stack.append((num, i))
                if i != len(nums):
                    break

        for val in sub_set:
            if list(val) not in result and len(list(val)) <= len(nums):
                result.append(list(val))
        return result



# import operator
#
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#
#         ops = {
#             "+": operator.add,
#             "-": operator.sub,
#             "*": operator.mul,
#             "/": lambda x, y: int(x / y)
#         }
#
#         for val in tokens:
#             if val not in ops:
#                 stack.append(int(val))
#                 continue
#             # operator = ops[val]
#             value1 = stack.pop()
#             value2 = stack.pop()
#
#             result = ops[val](value2, value1)
#             stack.append(result)
#         return stack[0]

lsyt = [2]
print([] + [lsyt[0]])

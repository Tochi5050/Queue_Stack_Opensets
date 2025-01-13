import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv,
        }

        stack = []
        maxVal = None
        stackIsEmpty = False

        for val in tokens:
            if val not in ops:
                stack.append(int(val))
                continue
            elif val in ops:
                if maxVal is None:  # Assuming stack would have more than one number
                    popVal1 = stack.pop()
                    popVal2 = stack.pop()
                    stackIsEmpty = True if len(stack) == 0 else False
                    maxVal = ops[val](popVal2, popVal1)
                elif maxVal is not None:
                    popVal = stack.pop()
                    if stackIsEmpty == True and val == '-':
                        maxVal = ops[val](maxVal, popVal)
                        break
                    if stackIsEmpty == False and val == '-':
                        maxVal = ops[val](popVal, maxVal)
                        break
                    if val == '/' and not isinstance(ops[val](maxVal, popVal), float):
                        maxVal = 0
                    else:
                        maxVal = ops[val](maxVal, popVal)
        return maxVal if maxVal is not None else stack[0]
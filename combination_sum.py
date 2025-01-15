def combinationSum(candidates, target):
    result = []
    stack = [(0, [], target)]  # (current index, current combination, remaining target)

    while stack:
        index, current_combination, remaining = stack.pop()

        if remaining == 0:
            result.append(current_combination)
            continue

        for i in range(index, len(candidates)):
            if candidates[i] <= remaining:  # Only consider valid candidates
                stack.append((i, current_combination + [candidates[i]], remaining - candidates[i]))

    return result

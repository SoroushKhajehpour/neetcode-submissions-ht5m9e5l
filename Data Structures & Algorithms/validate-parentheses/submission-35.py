class Solution:
    def isValid(self, s: str) -> bool:
        closing_to_open = {"}":"{", ")":"(", "]":"["}

        stack = []

        for bracket in s:
            if bracket in closing_to_open:
                if not stack:
                    return False
                else:
                    top = stack.pop()
                    if top != closing_to_open[bracket]:
                        return False
            else:
                stack.append(bracket)
        if stack:
            return False
        return True

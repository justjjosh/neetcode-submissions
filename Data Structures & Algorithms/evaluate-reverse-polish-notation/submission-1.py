import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPERATORS = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv  # Performs float division
        }

        final_stack = []
        for item in tokens:
            if item not in OPERATORS:
                final_stack.append(item)
            else:
                operand2 = int(final_stack.pop())
                operand1 = int(final_stack.pop())
                result = OPERATORS[item](operand1, operand2)
                final_stack.append(result)

        return int(final_stack[-1])
        
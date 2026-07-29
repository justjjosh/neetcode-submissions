class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        OPERATORS = set(["+", "-", "*", "/"])

        final_stack = []
        for item in tokens:
            if item not in OPERATORS:
                final_stack.append(item)
            else:
                operand2 = int(final_stack.pop())
                operand1 = int(final_stack.pop())
                if item == "+":
                    result = operand1 + operand2
                if item == "-":
                    result = operand1 - operand2
                if item == "*":
                    result = operand1 * operand2
                if item == "/":
                    result = operand1 / operand2
                final_stack.append(result)

        return int(final_stack[-1])
        
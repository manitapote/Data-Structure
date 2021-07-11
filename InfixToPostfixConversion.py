from Stack import Stack


# Converts infix operation to postfix operation
def infix_to_postfix(expression):
    stack = Stack()

    operators = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    operators_key = '*/+-'
    output = []

    for i in expression:
        if i == '(':
            stack.push(i)
        elif i == ')':
            token = stack.pop()

            while token != '(':
                output.append(token)
                token = stack.pop()
        elif i not in operators_key:
            output.append(i)
        else:
            while not stack.is_empty() and operators[stack.peek()] >= operators[i]:
                output.append(stack.pop())

            stack.push(i)

    while not stack.is_empty():
        output.append(stack.pop())

    print(''.join(output))


infix_to_postfix('A*(B+C)*D')

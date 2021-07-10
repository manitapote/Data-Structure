from Stack import Stack

#Checks whether string has balanced number of paranthesis
def balance_par_check(text):
    s = Stack()
    brackets_open = '[({'
    brackets_close = '])}'
    balanced = True

    for i in range(len(text)):
        if text[i] in brackets_open:
            s.push(text[i])

        if text[i] in brackets_close:
            if s.is_empty():
                balanced = False
                break

            closing = s.pop()

            if brackets_close.index(text[i]) != brackets_open.index(closing):
                balanced = False
                break

    print(balanced)

balance_par_check('(())')
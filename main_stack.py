from stack import Stack

pairs = {')': '(', ']': '[', '}': '{'}


def match_pairs(stack):
    def add_closed_bracket(element, open_bracket_stack):
        if element in pairs.keys():  # if new bracket is closed bracket
            stack_closed.push(element)
            return True
        else:
            # print("Open bracket without closing")
            return False


    stack_closed = Stack()  # for closed bracket only

    while stack.get_size():
        el = stack.pop()

        if stack_closed.get_size():
            el_closed = stack_closed.peek()
            if el == pairs.get(el_closed):  # find match and remove pair
                stack_closed.pop()
            else:
                if not add_closed_bracket(el, stack_closed):
                    return False
        else:
            if not add_closed_bracket(el, stack_closed):
                return False

    if stack_closed.get_size():
        return False
    else:
        return True


if __name__ == '__main__':
    stack = Stack("({}({})[])")
    res = match_pairs(stack)
    print(res)






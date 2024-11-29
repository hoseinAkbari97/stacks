from stack import Stack

if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push('h')
    my_stack.push('e')
    my_stack.push('l')
    my_stack.push('l')
    my_stack.push('o')
    print(list(my_stack.data))
    print(my_stack.pointer)
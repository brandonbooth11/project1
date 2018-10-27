#Imports array stack and array queue classes from lecture
from array_stack import ArrayStack
from array_queue import ArrayQueue

def radixSort(a, x = 1):
    #runs a radix sort on an array

    #makes variables used later in the method
    cont = False
    next = 0
    q = [ArrayQueue(), ArrayQueue(), ArrayQueue(), ArrayQueue(), ArrayQueue(),
         ArrayQueue(), ArrayQueue(), ArrayQueue(), ArrayQueue(), ArrayQueue()]

    #puts values from a in appropriate queues based on the current digit in the x place
    for i in a:
        if x < i:
            cont = True
        q[int((i%(10*x) - i%x)/x)].enqueue(i)

    #puts values in queues back into the array sorted by the appropriate number
    for i in q:
        while not i.is_empty():
            a[next] = i.dequeue()
            next += 1

    #does the recursive call or base case of the method
    if cont:
        return radixSort(a, 10*x)
    return a

def postFix(e):
    '''
    I've noticed that this sometimes doesnt work because somehow the '*' and '-' characters
    are technically different on some computers than others, so if it doesnt work, just
    replace the symbols in my 'if' statements with the versions on your keyboard and then
    try your examples
    '''
    
    #solves an expression in postfix notation

    #makes the array stack to store values from the expression until they are used
    s = ArrayStack()

    #checks each char in the expression to see if it is a digit. If it is, it puts it in the stack,
    #otherwise it performs the proper operation on the last 2 numbers in the stack
    for i in e:
        if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            s.push(int(i))
        elif i == "+":
            s.push(s.pop()+s.pop())
        elif i == "-":
            a = s.pop()
            b = s.pop()
            s.push(b-a)
        elif i == "*":
            s.push(s.pop()*s.pop())
        elif i == "/":
            a = s.pop()
            b = s.pop()
            s.push(b/a)

    #returns the end value
    return s.pop()
            
#tests radix sort
a = [35, 53, 55, 33,52, 32, 25]
a = radixSort(a)
print(a)

#tests postfix expression solver
print(postFix("52+83-*4/"))

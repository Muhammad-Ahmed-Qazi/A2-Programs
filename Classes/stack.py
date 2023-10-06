from prettytable import PrettyTable as pt

stackD = pt()
stackD.field_names = ["Elements", "Pointer"]

null = -1
top = null

class MyStack:
    stack = list()

    def __init__(self, size):
        global top, null

        for i in range(size):
            self.stack.append(None)
        
        top = null
    
    def push(self, data):
        global top

        if top != (len(self.stack) - 1):
            top += 1
            self.stack[top] = data
        else:
            print("Overflow error! No space for additional data.\n")
    
    def pop(self):
        global top

        if top != null:
            data = self.stack[top]
            top -= 1
            return data
        else:
            return False

    def display(self):
        global stackD

        if top != -1:
            for i in range(top, -1, -1):    
                if i == top:
                    # print(stack[i], "   <--- top")
                    stackD.add_row([self.stack[i], "<-- top"])
                else:
                    # print(stack[i])
                    stackD.add_row([self.stack[i], ""])

            print(stackD)
        else:
            print("Stack is currently empty!")
        stackD.clear_rows()
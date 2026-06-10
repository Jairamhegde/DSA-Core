stack = []          # array used as stack
MAX = 5             # stack size limit (optional)

def push():
    if len(stack) == MAX:
        print("Stack Overflow")
    else:
        item = int(input("Enter element to push: "))
        stack.append(item)
        print(item, "pushed into stack")

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print(stack.pop(), "popped from stack")

def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements (top to bottom):")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])

while True:
    print("\n1.Push  2.Pop  3.Peek  4.Display  5.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
1

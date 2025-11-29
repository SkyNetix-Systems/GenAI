def add(a, b):
    result = a + b
    return result

def main():
    x = 10
    y = 20
    z = add(x, y)
    print("Result is:", z)

if __name__ == "__main__":
    main()


#▶ Continue (F5) → run until next breakpoint
#⏭ Step Over (F10) → go to next line (don’t go inside functions)
#⬇ Step Into (F11) → go inside the function being called
#⬆ Step Out (Shift+F11) → finish current function and go back
#◼ Stop → stop debugging
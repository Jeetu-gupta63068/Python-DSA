def func(i, n):
    if i > n:
        return

    print(i)          # Forward
    func(i + 1, n)
    print(i)          # Backtracking

func(1,5)

# N to 1 (tail)
def func(n):
    if n==0:
        return
    print(n)
    func(n-1)
func(4)
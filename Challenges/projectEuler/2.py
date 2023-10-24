def computeFib():
    x = 1
    y = 2
    ans = 0
    while x <= 4000000:
        if x % 2 == 0:
            ans += x
            x, y = y, x+y
    return str(ans)


if __name__ == "__main__":
	print(computeFib())
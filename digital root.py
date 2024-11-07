def digital_root(n):
    def add(s):
        total = 0
        for i in s:
            total += int(i)
        return total

    if n < 10:
        return n
    else:
        return digital_root(add(str(n)))
    
print(digital_root(100)) # 6
            
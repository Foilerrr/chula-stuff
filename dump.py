def tower_builder(n_floors):
    j = 1
    for i in range(1, n_floors + 1):
        print(" " * (n_floors - i) + "*" * j + " " * (n_floors - i))
        j += 2

tower_builder(10)
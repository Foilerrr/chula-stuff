def sort_array(source_array):
    test = []
    for i in source_array:
        if i % 2 == 1:
            test.append(i)
    
    for i in range(len(source_array)):
        for i in source_array:
            if i % 2 == 1:
                source_array[i] = test[0]
                test.remove(test[0])
    return source_array
print(sort_array([5, 3, 2, 8, 1, 4])) # [1, 3, 2, 8, 5, 4]

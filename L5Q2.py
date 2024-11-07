def run():
    solfile = input("Choose your solution file:")
    examfile = input("Choose your exam file:")
    sfile = open(f"{solfile}", "r")
    efile = open(f"{examfile}", "r")
    
    # Read and process files
    exam = efile.readlines()
    sol = sfile.readlines()
    
    # Close the files right after reading
    sfile.close()
    efile.close()

    # Continue with the processing
    examf = []
    solf = []
    student = []
    questions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in exam:
        x = i.strip("\n").split(" ")
        examf.append(x)
        
    for i in sol:
        x = i.strip("\n").split(" ")
        solf.extend(x)
    
    for i in range(8):
        total = 0
        for j in range(10):
            if examf[i][j] == solf[j]:
                total += 1
                questions[j] += 1
        student.append(total)
        
    questionsf = [i / 8 for i in questions]
    
    # Print student scores without extra space
    print(f"\nStudent score : {student}\n")
    
    for i in range(10):
        print(f"Questions {i + 1} : {questions[i] / 8}")
    
    min_val = min(questions)
    max_val = max(questions)
    
    hardest = [i + 1 for i, q in enumerate(questions) if q == min_val]
    easiest = [i + 1 for i, q in enumerate(questions) if q == max_val]
    
    print()
    print(f"Hardest : {' '.join(map(str, hardest))}")
    print(f"Easiest : {' '.join(map(str, easiest))}")

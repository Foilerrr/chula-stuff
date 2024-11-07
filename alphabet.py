def do_math(st) :
    booga = {}
    counter = 1
    for i in "abcdefghijklmnopqrstuvwxyz":
        booga[i] = counter
        counter += 1
        
    listst = st.split(" ")
    dictst = {}
    for i in listst:
        if i in booga:
            dictst[i] = i
    return dictst

print(do_math("24z6 1x23 y369 89a 900b"))

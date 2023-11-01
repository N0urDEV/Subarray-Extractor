def sous_tableau(T, index1, index2):
    if index1 > index2:
        index1, index2 = index2, index1

    tab = []
    for i in range(index1, index2 + 1):
        tab.append(T[i])

    return tab

while True:
    T = []
    for i in range(10):
        T.append(int(input("Enter the value of case " + str(i) + ":")))

    print("Enter the two indices, note that they start from 0 to 9")
    index1 = int(input("Index 1: "))
    index2 = int(input("Index 2: "))

    print("The subarray is:", sous_tableau(T, index1, index2))

    response = input("Would you like to fill another table? (Yes/No): ")

    if response.lower() != "yes":
        break

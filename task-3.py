N = int(input("Введіть значення N (1 < N < 9): "))

if (N > 1) and (N < 9):
    for i in range(1, N + 1):
        for j in range (i, N + 1):
            print(j, end=" ")
        print("\n")
else:
    print("Задане число не відповідає умові")

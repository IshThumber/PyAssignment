def Lapin(str):
    strlen = len(str)
    if strlen % 2 == 0:
        a = str[: (strlen // 2)]
        b = str[(strlen // 2) :]
    else:
        a = str[: (strlen // 2)]
        b = str[(strlen // 2) + 1 :]
    li_a = list(a)
    li_a.sort()

    li_b = list(b)
    li_b.sort()

    if li_a == li_b:
        print("Yes")
    else:
        print("No")


a = int(input())

for i in range(a):
    String = input()
    Lapin(String)

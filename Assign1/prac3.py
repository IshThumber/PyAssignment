n = int(input())

room = map(int, input().split())
room = sorted(room)


for i in range(len(room)):
    if i != len(room) - 1:
        if room[i] != room[i + 1] and room[i] != room[i + 1]:
            print(room[i])
            break
    else:
        print(room[i])
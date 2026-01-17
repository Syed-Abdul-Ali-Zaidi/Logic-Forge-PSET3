first = input()
first = first.split(' ')
N = int(first[0])
K = int(first[1])
Q = int(first[2])

temp = input()
temp = temp.split(' ')
temp = [int(i) for i in temp]

queries = []
for i in range(Q):
    query = input()
    query = query.split(' ')
    queries.append(query)

alert = ['No Alert' for i in range(N)]
for i in range(N-1):
    for j in range(i+1,N):
        if (temp[j] >= temp[i] + K) or (temp[j] <= temp[i] - K):
            alert[i] = j
            break

for i in queries:
    if i[0] == 'NEXT':
        alert_day = alert[int(i[1])]
        print(alert_day)
    else:
        L = int(i[1])
        R = int(i[2])
        count = 0
        for i in range(L,R+1):
            if str(alert[i]).isdigit():
                count += 1
        print(count)

print('Temp:',temp)
print('Alert',alert)
# Done!
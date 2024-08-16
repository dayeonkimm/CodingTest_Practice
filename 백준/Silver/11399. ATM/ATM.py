people = int(input())
time = list(map(int,input().split()))

time.sort(reverse=True)
sum = 0

for i in range(people):
    sum += (i+1)*time[i]
    
print(sum)    

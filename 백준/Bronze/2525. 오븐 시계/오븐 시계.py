a,b = map(int,input().split())
c = int(input())
total_minute = a*60 + b
total_minute +=c
end_hour=(total_minute//60)%24
end_minute = total_minute % 60
print(end_hour, end_minute)
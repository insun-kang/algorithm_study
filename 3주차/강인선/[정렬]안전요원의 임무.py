N = int(input())
member_list = []

for _ in range(N):
    member_age, member_name = map(str, input().split())
    member_age = int(member_age)
    member_list.append((member_age, member_name))

member_list.sort(key = lambda member: (member[0], member[1]))

for member in member_list:
    print(member[0], member[1])

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    applicants = []
    for j in range(N):
        doc, interview = map(int, input().split())
        applicants.append((doc, interview))
    sort_applicants = sorted(applicants, key = lambda x : x[0])

    best_applicants = sort_applicants[0][1]
    count = 1
    for one in sort_applicants[1:]:
        if one[1] < best_applicants:
            count += 1
            best_applicants = one[1]
    print(count)
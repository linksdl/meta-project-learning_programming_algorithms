def cal_matrix(matrixs):
    print(matrixs)
    l_ = 0
    r_ = 0
    h_ = 0
    for i in range(len(matrixs)):
        s = [str(i) for i in matrixs[i]]
        print(' '.join(s))


while True:
    n = int(input())
    matrixs = [[0] * 3 for _ in range(n)]
    for i in range(n):
        nums = list(map(int, input().split()))
        # print(nums)
        matrixs[i][0] = nums[0]
        matrixs[i][1] = nums[1]
        matrixs[i][2] = nums[2]

    outline = cal_matrix(matrixs)
    print(outline)

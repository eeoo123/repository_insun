# 정규분포 N(0,1)에서 무작위로 샘플포인트 100개 추출하여 표본 1개 만들기
import numpy as np
mean = 0
std = 1
size1 = 100
sample1 = np.random.normal(mean, std, size1)

# 정규분포 N(0,1)에서 무작위로 샘플포인트 100개짜리 표본 100개 만들기
mean = 0
std = 1
size = (100, 100)
samples = np.random.normal(mean, std, size)


# 표본평균 구하기(sample1으로)
x = 0
for i in range(size1):
    x += sample1[i]/size1

# SE[X-] 구하기
#o = 0
#o += (std ** 1/2) / (size1 **1/2)
s = 0
for i in range(size1):
    s += ((sample1[i]-x) **2 / (size1-1)) ** 1/2

# 95% 신뢰구간 구하기
# low = mean - 1.96 * o
# high = mean + 1.96 * o

low = []
high = []
# 샘플 100개 신뢰구간 구하기
for i in range(size1):
    low.append(x - 1.96 * (1 / (size1 ** 1/2)))
    high.append(x + 1.96 * (1 / (size1 ** 1/2)))

    print(f"실험{[i+1]} 하한 : {low[i]}", end = "")
    print(f"실험{[i+1]} 상한 : {high[i]}")

for i in range(size1):
    if (low[i] < 0 and high[i] > 0):
        score = 0
        score += 1
    else:
        print(f"신뢰노구간 : 실험{i+1}")


# 신뢰구간에 포함인지 확인

# 비포함된 신뢰구간

# 신뢰구간 비율

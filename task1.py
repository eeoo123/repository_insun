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

# 표본평균과 모평균(표본평균의 평균)구하기(samples 이용)
x_sum = 0
x_list1 = []
for i in samples:
    x1 = 0
    for j in i:
        x1 += j
    x_1 = x1 / len(i)  # 표본평균
    x_list1.append(x_1)
    x_sum += x_1
m = x_sum / len(samples) # 모평균


print(f"모평균 : {m}")

# SE[x-] 구하기
def SE(n, sam):
    s2 = 0
    for i in sam:
        s2 += ((i - x_list1[n]) ** 2 )
    se = (((s2 / (len(sam) - 1)))**0.5) / ((size1)** 0.5)
    return se

def Confidence(x0, se0): # 신뢰구간
    low0 = x0 - 1.96 * se0
    high0 = x0 + 1.96 * se0
    return low0, high0


# samples 신뢰구간
num = 0
no = []
for i in x_list1:
    low_t, high_t = Confidence(i, SE(num, samples[num]))
    print(f"실험{num+1} 하한 : {low_t} 상한 {high_t}")
    # 신뢰구간 확인
    if (not(low_t <= m <= high_t)):
        no.append(num+1)
    num += 1

no_count = 0
for i in no:
    print(f"95%신뢰구간에 포함안됨 : 실험{i}")
    no_count += 1

print(f"모평균 미포함 신뢰구간 개수 : {no_count}")




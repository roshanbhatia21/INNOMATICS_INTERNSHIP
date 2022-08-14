import math
def cdf(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))
mean = 205
std = 15
n = 49
target = 9800
mean_s = n * mean
std_s = std * n**(1/2)
print(round(cdf(target, mean_s, std_s), 4))
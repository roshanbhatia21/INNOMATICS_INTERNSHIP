
import math
def cdf(x, mean, std):
    return 1/2*(1+math.erf((x-mean) / std / 2**(1/2)))
mean = 70
std = 10
print(round((1 - cdf(80, mean, std))*100, 2))
print(round((1 - cdf(60, mean, std))*100, 2))
print(round(cdf(60, mean, std)*100, 2))
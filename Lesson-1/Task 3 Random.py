import math

start = 50
end = 100
len_range = end - start + 1

gen_num = (int(str(id(i))[::-1][:5]) for i in range(len_range))


res = {}
for num, _ in enumerate(range(len_range - 1)):
    g = next(gen_num)
    sin = abs(math.sin(round(math.radians(g), 1)))
    delta = int(len_range * sin)
    res[num] = start + delta

print(res)

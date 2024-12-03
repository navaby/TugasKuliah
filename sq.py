sequence_a = []
n = 2
for i in range(7):
    sequence_a.append(n)
    if i < 2:
        n += 1  
    else:
        n += n // 2  
print(' '.join(map(str, sequence_a)))
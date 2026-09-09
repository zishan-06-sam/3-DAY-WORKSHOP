n = 4  
width = 2 * n - 1

for i in range(1, width + 1):
    if i == 1 or i == width:
        row = ['*'] * width          
    else:
        left_count = abs(i - n) + 1  
        gap = width - 2 * left_count
        row = ['*'] * left_count + [' '] * gap + ['*'] * left_count
    print(' '.join(row))
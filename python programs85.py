rows, cols = 4, 8

for r in range(rows):
    if r == 0 or r == rows - 1:
        print('*' * cols)          
    else:
        print('*' + ' ' * (cols - 2) + '*')   
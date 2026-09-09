rows = 3
cols = 8

for r in range(rows):
    line = ""
    for c in range(cols):

        if (c % 4 == 0 and r == 0) or (c % 4 == 2 and r == rows - 1) or (c % 4 in (1, 3) and r == 1):
            line += "* "
        else:
            line += "  "
    print(line)
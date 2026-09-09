def read_until_stop():
    count = 0
    total = 0
    while True:
        num = float(input("Enter a number (-1 to stop): "))
        if num == -1:
            break
        count += 1
        total += num

    if count > 0:
        print("Count:", count)
        print("Average:", total / count)
    else:
        print("No numbers entered.")

read_until_stop()
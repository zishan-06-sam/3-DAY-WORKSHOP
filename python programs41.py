hour = int(input("Enter hour (0-12): "))
minute = int(input("Enter minute (0-59): "))

hour_angle = (hour % 12) * 30 + (minute * 0.5)
minute_angle = minute * 6

angle = abs(hour_angle - minute_angle)

if angle > 180:
    angle = 360 - angle

print("The angle between the hands is: " + str(angle) + " degrees")
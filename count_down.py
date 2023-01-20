import time

num = int(input("Enter time in seconds: "))
for x in range(num, 0, -1):   #reverse number
    seconds = x % 60
    minutes = int(x/60)%60
    hours = int(x/3600)
    print(f"{hours}:{minutes}:{seconds:02}")
    time.sleep(1)


print("Time up!")

import datetime

time = datetime.datetime.now()
time = time.hour
# print(time)

# Main Logic

if (time >= 0 and time < 5):
    print("Good Night")
elif (time >= 5 and time < 12):
    print("Good Morning")
elif (time >= 12 and time < 18):
    print("Good Afternoon")
else:
    print("Good Evening")
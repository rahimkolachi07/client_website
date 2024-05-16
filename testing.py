import datetime
current_time = datetime.datetime.now().time()
print(int(int(current_time.hour)%4.5))
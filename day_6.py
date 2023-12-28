with open("day_6.txt", "r") as f:
    file = f.read()
    
lines = file.split("\n")

times = []
time_data = lines[0]
time_data_points = time_data.split(" ")
for point in time_data_points:
    try:
        time = int(point)
    except ValueError:
        continue
    times.append(int(time))
    
records = []
record_data = lines[1]
record_data_points = record_data.split(" ")
for record in record_data_points:
    try:
        record = int(record)
    except ValueError:
        continue
    records.append(int(record))

counters =[]
for i in range(0, len(records)):
    race_duration = times[i]
    record = records[i]
    counter = 0
    for i in range(0,race_duration):
        speed = i
        duration = race_duration - i
        distance = speed * duration
        if distance > record:
            counter +=  1
    counters.append(counter)
    
possible = 1
for counter in counters:
    possible = possible * counter
    
print(possible)

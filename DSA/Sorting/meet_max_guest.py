import sys
# time of arrival
# time of departure
# For a person to meet another, arrival needs to be lower than departure
# common time period for most guests to be present
arrival = [13, 28, 29, 14, 40, 17, 3]
departure = [107, 95, 111, 105, 70, 127, 74]

# Sort Array and Compare values (Efficient Method)
def max_guests(arr, dep):
    # sort arrival and departure times in the array
    arr.sort()
    dep.sort()
    # there will always be one arrival at the beginning,
    # that's why we ignore first arrival time and start our guest count at 1
    i, j, n = 1, 0, len(arr)
    count, result = 1, 1
    while i < n and j < n:
        # if current arrival time is lower than departure, a guest has arrived
        if arr[i] <= dep[j]:
            count += 1
            i += 1
        # if current arrival time is higher than departure, meaning a guest has left
        else:
            count -= 1
            j += 1
        # max value represents maximum number of guests visited
        result = max(count, result)
    return result

print(max_guests(arrival, departure))

# Dummy Array (Less Efficient) Method
def max_overlap(start, end):
    n = len(start)
    # Find max arrival and departure time
    max_arrival = max(start)
    max_depart = max(end)
    max_time = max(max_arrival, max_depart)
    # Create a dummy array of 0 value
    guests = [0] * (max_time + 2)
    # Tracks current guest count and time when max guests were present
    count, time_index = 0, 0

    for i in range(n):
        # 1 represents a guest came, -1 represents a guest left, 0 represents no overall movement
        guests[start[i]] += 1
        guests[end[i]] -= 1

    max_count = -1
    # Treverse dumy array to find number and time when max guests were present
    for i in range(max_time + 1):
        count += guests[i]
        if max_count < count:
            max_count = count
            time_index = i

    return f"Maximum guests visited is {max_count} at {time_index} time."

print(max_overlap(arrival, departure))

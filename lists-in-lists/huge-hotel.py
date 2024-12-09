# A huge hotel, 3 building 15 floors and 20 rooms
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

print(rooms)

# Booking a room: in the second building, on the tenth floor, room 14
rooms[1][9][13] = True

print("Occuping room")
print(rooms)

# Book second room on the fifth floor located in the first building
rooms[0][4][1] = False
print(rooms)

# Check if there are any vacancies on 15th floor of the third building
vacancy = 0
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print("Vacany: ", vacancy)

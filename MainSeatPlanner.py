# This program makes allocating seats to people for exams easier

from School import School
from Grade import Grade
from Room import Room

# Returns two-digit number as string
def format_number(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)

# Upadates available seats
def update_available_seats(available_seats_list, alloted_seat):
    # Prepare a list of seats to remove
    seats_to_remove = []
    room_sn = int(alloted_seat[2:4])
    desk_sn = int(alloted_seat[4:6])
    seat_sn = int(alloted_seat[6:])
    # Add the seats in current desk as well as surrounding desk of the same side to the seats_to_remove list
    for i in range(-2,4,2):
        for j in range(1, 3 + 1):
            seats_to_remove.append("SN" + format_number(room_sn) + format_number(desk_sn + i) + str(j))
    # For the seats in another side 
    # If the alloted desk is in corner side
    if desk_sn % 2 == 0:
        if seat_sn == 1:
            for i in [-3, -1, 1]:
                seats_to_remove.append("SN" + format_number(room_sn) + format_number(desk_sn + i) + str(3))
    # If the alloted desk is in door side
    else:
        if seat_sn == 3:
            for i in [-1, 1, 3]:
                seats_to_remove.append("SN" + format_number(room_sn) + format_number(desk_sn + i) + str(1))

    # Remove each them if the availble_seats_list contains it
    for seat in seats_to_remove:
        if seat in available_seats_list:
            available_seats_list.remove(seat)
    return available_seats_list

# Allots seat for each student of the grade
def allot_seat(grade_sn):
    # Set current_room to the first room
    current_room = school.roomList[0]
    current_room_counter = 1
    # Create a grade object
    grade = Grade(grade_sn)
    # Set the current_room_available_seats for the grade
    grade.current_room_available_seats = list(current_room.emptySeats)
    # For creating a list of sections, taking user input
    no_of_sections = input("How many sections are there in grade " + str(grade_sn) + "?")
    sections_string = input("What are those sections?(Use space as separator between sections.)")
    # Creates a list of sections
    sections = sections_string.split()
    for i in range(len(sections)):
        # Capitalizing the first letter of the word
        current_section = sections[i].capitalize()
        # Taking the first letter of the capitalized word and replacing the corresponding section in the sections list
        sections[i] = current_section[0]
    for section in sections:
        no_of_students = int(input("How many students are there in " + str(grade.gradeSN) + "'" + section +"'?"))
        for j in range(1, no_of_students + 1):
            # Assigning symbol number to each student
            student = format_number(grade.gradeSN) + format_number(j) + "'" + section +"'"
            # Adding each student to the students list of the corresponding grade
            grade.students.append(student)
    for student in grade.students:
        # If current_room doesn't have any available seats for the students in current grade, move onto the next room.
        if len(grade.current_room_available_seats) == 0:
            current_room_counter
            current_room_counter += 1
            # If roomList doesn't have another room, add new_room and move onto the new room.
            if len(school.roomList) < current_room_counter:
                global to_create_room_counter
                to_create_room_counter +=1
                new_room = Room(to_create_room_counter)
                no_of_desks_in_each_side = int(input("How many desks are there in each side of Room No. " + str(to_create_room_counter) + "?"))
                # Add each seat to emptySeats
                for i in range(1, no_of_desks_in_each_side * 2 + 1):
                    for j in range(1, 3 + 1):
                        new_room.emptySeats.append("SN" + format_number(to_create_room_counter) + format_number(i) + str(j))
                school.roomList.append(new_room)
            current_room = school.roomList[current_room_counter - 1]
            grade.current_room_available_seats = list(current_room.emptySeats)
        # Place the student in the first available seat
        # Remove that seat form "emptySeats" and update current_room_available_seats
        #TODO adapt this for creating gradewise seat planning list
        current_seat = grade.current_room_available_seats[0]
        current_room.roomSeatFinal.update({current_seat: student})
        current_room.emptySeats.remove(current_seat)
        school.roomList[current_room_counter - 1] = current_room
        grade.current_room_available_seats = list(update_available_seats(grade.current_room_available_seats, current_seat))
        # TODO allot the seats for random student not in increasing order of Roll No.

# Create object "school" and set the attributes from user input.
school_name = input("Enter the name of school:")
school_address = input("Enter the address of school:")
least_grade = int(input("Grades start from:"))
highest_grade = int(input("Upto which grade:"))
school = School(school_name, school_address, least_grade, highest_grade)

# Take the examination infos as user input.
examination_name = input("Enter the title of examination:")
examination_year = input("Enter the examination year:")

to_create_room_counter = 1
# Create the first room and add it to the roomList
new_room = Room(to_create_room_counter)
no_of_desks_in_each_side = int(input("How many desks are there in each side of Room No. " + str(to_create_room_counter) + "?"))
# Add each seat to emptySeats
for i in range(1, no_of_desks_in_each_side * 2 + 1):
    for j in range(1, 3 + 1):
        new_room.emptySeats.append("SN" + format_number(to_create_room_counter) + format_number(i) + str(j))
school.roomList.append(new_room)

# Starting from highestGrade, allot seats for each student in each grade
grade_sn_counter = school.highestGrade
while grade_sn_counter + 1 > school.leastGrade:
    allot_seat(grade_sn_counter)
    grade_sn_counter -= 1

for room in school.roomList:
    sorted_roomSeatFinal = sorted(room.roomSeatFinal.items())
    print(sorted_roomSeatFinal)
# TODO Create PDF file.

# The object "school" must have attributes schoolName, schoolAddress, leastGrade, highestGrade and roomList.
class School:
    def __init__(self, school_name, school_address, least_grade, highest_grade):
        self.schoolName = school_name
        self.schoolAddress = school_address
        self.leastGrade = least_grade
        self.highestGrade = highest_grade
        self.roomList = []
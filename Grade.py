# The object "grade" must have attributes gradeSN, sectionsList, noOfStds and nonAllotedStds.
class Grade:
    def __init__(self, grade_sn):
        self.gradeSN = grade_sn
        self.students = []
        self.current_room_available_seats = []
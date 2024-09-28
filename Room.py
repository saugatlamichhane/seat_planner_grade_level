# The object "room" must have attributes roomSN, emptySeats roomSeatFinal.
class Room:
    def __init__(self, room_sn):
        self.roomSN = room_sn
        self.emptySeats = []
        self.roomSeatFinal = {}
class Geo:

    @staticmethod
    def NorthingEastingToDecimal( degrees, minutes, seconds, direction ):
        direction_factor = {'N':1, 'S':-1, 'E': 1, 'W':-1 }
        return (int(degrees)+int(minutes)/60.0+int(seconds)/3600.0) * direction_factor[direction]

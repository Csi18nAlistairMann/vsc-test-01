#
# This is just a simple class that gives effect to a deliberately low quality
# facility - that of sending back an average OR a failure

class Maffs:
    def average_of_three_non_zeroes(self, v1, v2, v3):
        if (v1 == 0 or v2 == 0 or v3 == 0): 
            return -1
        return ((v1 + v2 + v3) / 3)

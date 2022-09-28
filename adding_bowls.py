class AddingBowls:
    def __init__(self):
        x=0
    def total(self,name1,name2,dict,name3=""):

        try:
            total1 = dict[name1]
        except KeyError:
            total1 = 0
        try:
            total2 = dict[name2]
        except KeyError:
            total2 = 0
        try:
            total3 = dict[name3]
        except KeyError:
            total3 = 0

        return total1 + total2 + total3


    def total2(self,name1,dict):
        try:
            total1 = dict[name1]
        except KeyError:
            total1 = 0

        return total1

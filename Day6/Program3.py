# A Python Program to understand instance variable or static variable

class Players(object):
    #Static Variable/Class Variable
    firstname = 'Virat'
    LastName = 'Kohili'

    def __init__(self, pno, pty):
       #instance Variable
        self.playerno = pno
        self.plyertype = pty

    def changename(self,nm):
        self.firstname = nm

a = Players(17, 'Batsman')

print( "PLayer is {} {}".format(a.firstname,a.LastName))
print(a.playerno)
print(a.plyertype)
a.changename("Amruth")
print(a.firstname)

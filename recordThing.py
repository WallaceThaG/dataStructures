class RecordType():
    def __init__(self, theID, theLastName, theFirstName, theDept):
        self.id = theID
        self.lastName = theLastName
        self.firstName = theFirstName
        self.dept = theDept

myRecord = RecordType(1234, "Kellett", "Zhandos", 567)

array = []
for i in range(10):
    array[i].id
class RecordType():
  def __init__(self, theID, theLastName, theFirstName, theDept):
    self.id = theID
    self.lastName = theLastName
    self.firstName = theFirstName
    self.dept = theDept

# record1 = record(ID, lastName, firstName, dept)
record1 = (2468, "Jones", "John", 243)

print(record1.id)

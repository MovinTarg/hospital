class Patient(object):
    def __init__(self, id_number, name, allergies):
        self.id_number = id_number
        self.name = name
        self.allergies = allergies
        self.bed_number = None
    def info(self):
        print 'Id#: ' + self.id_number + ' | Name: ' + self.name + ' | Bed#: ' + str(self.bed_number)
        print 'Alergies:'
        for allergy in self.allergies:
            print allergy
        return self

class Hospital(object):
    def __init__(self, c_name, capacity):
        self.c_name = c_name
        self.patients = []
        self.capacity = capacity
        self.numBeds = range(1, self.capacity+1)
        self.beds = dict.fromkeys(self.numBeds)
    def admit(self, newPatient):
        if len(self.patients) < self.capacity:
            self.patients.append(newPatient)
            print 'Patient ' + newPatient.name + ' admitted'
            for bed, occupant in self.beds.iteritems():
                if occupant == None:
                    self.beds[bed] = newPatient.name
                    newPatient.bed_number = bed
                    break
        else:
            print 'Sorry, no insurance, go die elsewhere'
        return self
    def discharge(self, patientId):
        self.patients.remove(patientId)
        print 'Patient ' + patientId.name + ' discharged'
        patientId.bed_number = None
        for bed, occupant in self.beds.iteritems():
                if occupant == patientId.name:
                    self.beds[bed] = None
        return self
    def display(self):
        # print self.beds
        for person in self.patients:
            person.info()
        return self

patient1 = Patient('1', 'Pete', ['dust', 'flowers'])
patient2 = Patient('2', 'Todd', ['flowers', 'fish'])
patient3 = Patient('3', 'Minh', ['fish', 'dust'])
patient4 = Patient('4', 'Mike', ['happiness', 'fish'])
# patient1.info()

hospital1 = Hospital('Mt. Hope', 5)
hospital1.admit(patient1).admit(patient2).admit(patient3).discharge(patient2).admit(patient4).display()

hospital2 = Hospital('Mt. Hope', 3)
hospital2.admit(patient1).admit(patient2).admit(patient3).admit(patient4).display()
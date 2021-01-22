class Person :
    sum = 0

    def __init__(self, age, sex) :
        self.age = age
        self.sex = sex
        Person.sum = Person.sum + 1
    
    def prt(self) :
        print("This is a person : ", self.age, ' ', self.sex, ' ', Person.sum)

class Student(Person) :
    def __init__(self, age, sex, score) :
        Person.__init__(self, age, sex)
        self.score = score
    def prt(self) :
        print("This is a student : ", self.age, self.sex, self.score, Person.sum)
    

def test() :
    a = Person(10, 1)
    a.prt()
    b = Person(10, 0)
    b.prt()
    print("the sum of person is ", Person.sum)

    c = Student(18, 1, 100)
    c.prt()
    d = Student(19, 0, 95)
    d.prt()
    print("the sum of person is ", Person.sum)

test()
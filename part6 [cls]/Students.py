""" Создайте структуру с именем student, содержащую поля: 
фамилия и инициалы, номер группы, успеваемость (массив из пяти элементов). 
Создать массив из десяти элементов такого типа, 
упорядочить записи по возрастанию среднего балла. 
Добавить возможность вывода фамилий и номеров групп студентов, 
имеющих оценки, равные только 4 или 5.

(Я использовал файл input2.txt  в соответствующей папке, 
чтобы упростить ввод данных. Да, так проще.)
"""

class Student:
    all_students = []
    
    def __init__(self, fam, NameO, group, study: list):
        self.fam = fam
        self.IO = NameO
        self.grp = group
        self.study = study
        Student.all_students.append(self)
    
    def getFam(self):
        return self.fam
    
    def getIO(self):
        return self.IO
    
    def getGrp(self):
        return self.grp
    
    def getMid(self):
        return self.find_mid()
    
    def find_mid(self):
        vsp = 0
        for i in self.study:
            vsp += i
        vsp /= len(self.study)
        return vsp
    
    def dict_4and5():
        d = {}
        for i in Student.all_students:
            flag = True
            for j in i.study:
                if  j < 4:
                    flag = False
            if  flag:
                if d.get(i.grp) == None:
                    d[i.grp] = []
                d[i.grp].append(i.fam)
        for key, item in d.items():
            print('Группа', key)
            for j in item:
                print('\t', j)
        
        return d

    def sorted_up():
        vsps = Student.all_students
        for i, ival in enumerate(vsps):
            for j, jval in enumerate(vsps):
                if i != j and ival.find_mid() > jval.find_mid():
                    vsps[i], vsps[j] = vsps[j], vsps[i]
        Student.all_students = vsps
        return Student.all_students

with open('Git_Class/input2.txt', 'r') as f:
    n = int(f.readline())
    lst_students = []
    for i in range(n):
        fam = f.readline().strip('\n')
        nameo = f.readline().strip('\n')
        grp = f.readline().strip('\n')
        marks = f.readline().strip('\n').split()
        for j, val in enumerate(marks):
            marks[j] = int(val)
        lst_students.append(Student(fam, nameo, grp, marks))

lst_students = Student.sorted_up()

for i in lst_students:
    print(i.getFam(), '\t', i.getGrp(), '\t', i.getMid())

n = input('\nПоказать список студентов, имеющих только 4 или 5?(y/n) ')
if n == 'y':
    Student.dict_4and5()
input()

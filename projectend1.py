import sqlite3

conn = sqlite3.connect('TIiME_C.db')
c = conn.cursor()

c.execute(''' create table if not exists Students (id integer primary key autoincrement,firstname text not null,
    lastname text not null , email text not null, dateOFbirth integer  not null, dateOFEnroll integer not null)
         ''')

c.execute(''' create table if not exists Lecturer (id integer primary key autoincrement, firstname text not null,
    lastname text not null, email text not null, hierdate text not null, department text not null)
         ''')

c.execute('''create table if not exists Assignments (id integer primary key autoincrement,name text not null,description text not null,
    Lecturerid integer not null, foreign key (Lecturerid) references Lecturer(id))
         ''')

c.execute('''create table if not exists Grades (id integer primary key autoincrement, grade integer not null, assignmentid integer not null,
    studentid integer not null, foreign key (assignmentid) references Assignments(id), foreign key (studentid) references Students(id))
         ''')

conn.commit()



'______________________________________________________________________________'
class Students:
    count_id_Students = 0
    def __init__(self, firstname, lastName, email, dateOFbirth, dateOFEnroll):
        Students.count_id_Students += 1
        self.id_Students = Students.count_id_Students                                     
        self.firstname = firstname
        self.lastName = lastName
        self.email = email
        self.dateOFbirth = dateOFbirth
        self.dateOFEnroll = dateOFEnroll
        c.execute('''
        INSERT INTO Students (firstname, lastname, email, dateofbirth, dateofenroll) 
        VALUES (?, ?, ?, ?, ?)
        ''', (self.firstname, self.lastName, self.email, self.dateOFbirth, self.dateOFEnroll))
        conn.commit()

    
    # جلب جميع الطلاب من قاعدة البيانات    
    def get_all_Students(c) : 
        for i in c.execute('select * from Students'):
            print(i)
          
    
    #دالة اضافة طالب    
    def add_student_to_db(cursor, firstname, lastName, email, dateOFbirth, dateOFEnroll):
        add=''' INSERT INTO Students (firstname, lastname, email, dateofbirth, dateofenroll)
        VALUES (?, ?, ?, ?, ?)
        '''
        c.execute(add, (firstname, lastName, email, dateOFbirth, dateOFEnroll))
        return cursor.lastrowid
# حذف طالب من قاعدة البيانات    
    def delete_student(self,c):
        c.execute('''
                  delete from Grades where studentid=?
                  ''',(self.id_Students,))
        c.execute('''
                   delete from Students where id=?    
                  ''',(self.id_Students,))
    
            # البحث عن طالب من خلال تاريخ ميلاد(بين تاريخين)            
    def Search_aboutStudent(c,a,b) :
        x = c.execute('''
                      select * from Students where dateOFbirth between ? and ?
                      ''',(a,b))
        for i in x:
            print(i)
    
 
    
'______________________________________________________________________________'
class Grades:
    count_id_Grades = 0
    def __init__(self, grade, assignmentld, studentld):
        Grades.count_id_Grades += 1
        self.id_Grades = Grades.count_id_Grades
        self.grade = grade
        self.assignmentld = assignmentld
        self.studentld = studentld
        c.execute('''
        INSERT INTO Grades (grade, assignmentid, studentid) 
        VALUES (?, ?, ?)
        ''', (self.grade, self.assignmentld, self.studentld))

  
   



'______________________________________________________________________________'


class Assignments:
    count_id_Assignments = 0
    def __init__(self, name, description, lecturerld):
        Assignments.count_id_Assignments += 1
        self.id_Assignments = Assignments.count_id_Assignments
        self.name = name
        self.description = description
        self.lecturerld = lecturerld
        c.execute('''
        INSERT INTO Assignments (name,description, lecturerid) 
        VALUES (?, ?,?)
        ''', (self.name,self.description, self.lecturerld))
        
        
        
    def createGrades(self, grade, id_Students):
        return Grades(grade, self.id_Assignments, id_Students) 
       
    
       
     
    def add_Grade_to_db(self ,cursor,grade, studentid):
        c.execute('''
        insert into Grades(grade,assignmentid,studentid)
        values(?,?,?)
        ''',(grade,self.id_Assignments,studentid))
   
      
    
   
    def get_all_Grades_for_Assignments(self , c ):
      
        a = c.execute('''
                  
               select grade from Grades where assignmentid = ?
                  
                  ''', (self.id_Assignments,)  )
        for i in a:
            print(i)
            
            
            
            
    def update_Grade_for_assignment(self,c,grade,studentid) :
       c.execute('''
                 update Grades set grade=? where assignmentid=? and  studentid=?
                 ''',(grade,self.id_Assignments,studentid))        

 


'___________________________________________________________________________'



class Lecturer:
    count_id_Lecturer = 0
    def __init__(self, firstname, lastName, email, hierDate, department):
        Lecturer.count_id_Lecturer += 1
        self.id_Lecturer = Lecturer.count_id_Lecturer
        self.firstname = firstname
        self.lastName = lastName
        self.email = email
        self.hierDate = hierDate
        self.department = department
        c.execute('''
        INSERT INTO Lecturer (firstname, lastname, email, hierdate, department) 
        VALUES (?, ?, ?, ?, ?)
        ''', (self.firstname, self.lastName, self.email, self.hierDate, self.department))
    
   
    def createAssignments(self, name, description):
        return Assignments(name, description, self.id_Lecturer)
    
    # اضافة محاضر     
    def add_Lecturer_to_db(curos,firstname,lastName, email,hierDate,department):
        add_l='''
        insert into Lecturer (firstname,lastName,email,hierDate,department) 
        values(?,?,?,?,?)
        '''
        c.execute(add_l,(firstname,lastName,email,hierDate,department))
        return c.lastrowid
    
    
    def add_Assignment_to_db ( self, cursor ,name, description  ) : 
        add_assig='''
        insert into Assignments (name, description ,Lecturerid )
        values(?,? ,? )
        '''
        c.execute(add_assig,(name, description ,self.id_Lecturer   ))
        print('enter')
   
    # جلب جميع المحاضرين من قاعدة البيانات     
    def get_all_Lecturers(c): 
        for i in c.execute('select * from Lecturer'):
            print(i)
            
            
            
    def get_all_Assignments_for_Lecturer(self , c ):
      
        a = c.execute('''
                  
               select * from Assignments where Lecturerid = ?
                  
                  ''', (self.id_Lecturer,)  )
        for i in a:
            print(i)
       
        

    #دالة بحث عن المحاضرين عن طريق الاسم او البريد الالكتروني   
    def Search_about_Lecturer(firstname,email):
        a = c.execute('''
                  select *from Lecturer where firstname=? or email=?
                  ''',(firstname,email))
                  
        for i in a:
            print(i)





    def delete_Lecturer(self,c):
      c.execute('DELETE FROM Grades WHERE assignmentid IN (SELECT assignmentid FROM Assignments WHERE Lecturerid = ?)', (self.id_Lecturer,))
      c.execute('DELETE FROM Assignments WHERE Lecturerid = ?', (self.id_Lecturer,))
      c.execute('DELETE FROM Lecturer WHERE id = ?', (self.id_Lecturer,))
      conn.commit()

    
 
    
 
    
 


'______________________________________________________________________________'
# إنشاء اوبجيكتات وإدخال البيانات في قاعدة البيانات
obj_st1 = Students('zaid', 'alsalh', 'z@gmail.com', 2002, 2024)
obj_st2 = Students('abdalrzak', 'alsaleh', 'ab@gmail.com', 2004, 2024)
obj_st3 = Students('mohamad', 'ali', 'm.a@gmail.com', 2003, 2024)

obj_lect1 = Lecturer('abd', 'almohaemen', 'abd@gmail.com', 2015, 'dr it')
obj_lect2 = Lecturer('mohamad', 'noor', 'm.n@gmail.com', 2015, 'dr it')

obj_assi = obj_lect1.createAssignments('it', 'it course description')
obj_gra = obj_assi.createGrades(500, obj_st1.id_Students)



# إضافة طالب جديد 
new_student_id = Students.add_student_to_db(c, 'majd', 'abdulhai', 'majd@gmail.com', 2005, 2022)




# اضافة محاضر جديد
new__Lecturer=Lecturer.add_Lecturer_to_db(c, 'mohamad', 'depesh', 'm.d@gmail.com', 2000, 'it')



#اضافة وضيفة جديدة الى دكتور معين
new_assi2 = obj_lect2.add_Assignment_to_db(c, 'math', 'PI')




# اضاغة درجة طالب في وضيفة معينة
new_Grade = obj_assi.add_Grade_to_db(c, 50, obj_st2.id_Students)




# جلب جميع المحاضرين
Lecturer.get_all_Lecturers(c)



#جلب جميع الطلاب
Students.get_all_Students(c)



# جلب جميع وضايف دكتور معين
obj_lect1.get_all_Assignments_for_Lecturer(c)




# جلب علامة وضيفة معينة
obj_assi.get_all_Grades_for_Assignments(c)





# حذف طالب مع علامته
#obj_st1.delete_student(c)



# حذف محاضر مع وضائفة مع علامات الوضايف
#obj_lect1.delete_Lecturer(c)



#  تعديل درجة طالب حسب وظيفته
#obj_assi.update_Grade_for_assignment(c, 70, obj_st2.id_Students)



# دالة البحث عن المحاضرين عن طريق الاسم او البيرد
#Lecturer.Search_about_Lecturer(firstname='abssd', email='abd@gmkail.com')



#  البحث عن طالب عن طريق تاريخ ميلادة بين تاريخين
#Students.Search_aboutStudent(c, 2004, 2005)


'______________________________________________________________________________'



conn.commit()
#conn.close()





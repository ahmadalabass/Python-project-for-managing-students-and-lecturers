import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton , QTableWidget  , QMainWindow  , QTableWidgetItem 
from PyQt5 import QtGui , QtWidgets 

import sqlite3
conn = sqlite3.connect('arood.db')
c = conn.cursor()


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('TIEM C')
window.setGeometry(600, 400, 400, 300)
window.setStyleSheet('background-color:#FBEEE6;')
window.setWindowIcon(QtGui.QIcon('C:\\Users\\ZaidAlsalh\\Desktop\\pngegg.png'))

text = QtWidgets.QLabel(' MAIN WINDOW ' , window)
text.setStyleSheet('color:black; font-size:30px; border-radius:50px;')
text.move(80,8)


labe = ''' 
1 - لعرض جميع الطلاب اضغط على زر All Students
2 - لعرض جميع الطلاب اضغط على زر All Lechare

'''
text2=QtWidgets.QLabel(labe , window)
text2.move(57,150)
text2.setStyleSheet('color:black; font-size:16px; border-radius:20px;')


button1 = QPushButton(' All Students' , window) 
button1.setGeometry(45,90,150,40)
button1.setStyleSheet('background-color:#F4ECF7; color:black; font-size:17px; border:0.5px solid black ; border-radius:9px;')
button1.setIcon(QtGui.QIcon('C:\\Users\\ZaidAlsalh\\Desktop\\student.png'))
button1.setToolTip('عرض جميع الطلاب ')

button2 = QPushButton('All Lecturer' , window)
button2.setGeometry(210,90,150,40)
button2.setStyleSheet('background-color:#F4ECF7; color:black; font-size:17px; border:0.5px solid black ; border-radius:9px;')
button2.setIcon(QtGui.QIcon('C:\\Users\\ZaidAlsalh\\Desktop\\Lecturer.png' ))
button2.setToolTip('عرض جميع المحاضرين')



def pris1():
    window1 = QMainWindow()
    window1.setWindowTitle('All Students')
    window1.setStyleSheet('background-color:#FBEEE6;')
    window1.setWindowIcon(QtGui.QIcon('C:\\Users\\ZaidAlsalh\\Desktop\\student.png'))
    window1.setGeometry(800, 200, 1000, 400)
    
    
    table = QTableWidget(window1)
    table.setGeometry(0,0,800,700)
    table.setStyleSheet('background-color:#F4ECF7; color:black; font-size:18px; border:1px solid black ; border-radius:9px;')
    table.setColumnCount(6)
    table.setHorizontalHeaderLabels(['ID' , 'firstname' , 'lastName' , 'email', 'dateOFbirth', 'dateOFEnroll'])
    
    
    
    coom = c.execute('select * from Students')
    z = coom.fetchall()
    table.setRowCount(len(z))
    row = 0
    for i in z:
        table.setItem(row,0, QTableWidgetItem(str(i[0])))
        table.setItem(row,1, QTableWidgetItem(str(i[1])))
        table.setItem(row,2, QTableWidgetItem(str(i[2])))
        table.setItem(row,3, QTableWidgetItem(str(i[3])))
        table.setItem(row,4, QTableWidgetItem(str(i[4])))
        table.setItem(row,5, QTableWidgetItem(str(i[5])))

        row +=1
        
    


    button_1 = QPushButton(' Search' , window1) 
    button_1.setGeometry(820,60,150,40)
    button_1.setStyleSheet('background-color:#F4ECF7; color:black; font-size:17px; border:0.5px solid black ; border-radius:7px;')
    button_1.setIcon(QtGui.QIcon('C:\\Users\\ZaidAlsalh\\Desktop\\SERCH.png'))
    
    inputt =QtWidgets.QLineEdit(window1)
    inputt.setToolTip('ادخل تاريخ ملاد الطالب المراد البحث عنة')
    inputt.setGeometry(820,15,150,40)
    inputt.setStyleSheet('background-color:#F4ECF7; color:black; font-size:17px; border:0.5px solid black ; border-radius:7px;')
    inputt.setPlaceholderText('  ادخل التاريخ :  ')
    def pres_input1():
        window3 = QMainWindow()
        window3.setWindowTitle('Search Students')
        window3.setStyleSheet('background-color:#F4ECF7;')
        window3.setWindowIcon(QtGui.QIcon('C:\\Users\\ZaidAlsalh\\Desktop\\SERCH.png'))
        window3.setGeometry(800, 200, 1000, 400)
        
        a = c.execute('''
                select * from Students where dateOFbirth = ?  
                
                
                ''',(inputt.text() ,  ) )
        a =c.fetchall()
        
        table1 = QTableWidget(window3)
        table1.setGeometry(0,0,1000,500)
        table1.setColumnCount(6)
        table1.setRowCount(len(a))
        table1.setStyleSheet('background-color:#F4ECF7; color:black; font-size:18px; border:1px solid black ; border-radius:9px;')
        table1.setHorizontalHeaderLabels(['ID' , 'firstname' , 'lastName' , 'email', 'dateOFbirth', 'dateOFEnroll'])
        
        row1 = 0
        for i in a:
            table1.setItem(row1,0, QTableWidgetItem(str(i[0])))
            table1.setItem(row1,1, QTableWidgetItem(str(i[1])))
            table1.setItem(row1,2, QTableWidgetItem(str(i[2])))
            table1.setItem(row1,3, QTableWidgetItem(str(i[3])))
            table1.setItem(row1,4, QTableWidgetItem(str(i[4])))
            table1.setItem(row1,5, QTableWidgetItem(str(i[5])))
            row1 += 1
        window3.show()
        window3.exec_()
    button_1.clicked.connect(pres_input1) 

    button_2 = QPushButton(' DELETE' , window1) 
    button_2.setGeometry(820,200,150,40)
    button_2.setStyleSheet('background-color:#F4ECF7; color:black; font-size:17px; border:0.5px solid black ; border-radius:7px;')
    button_2.setIcon(QtGui.QIcon('C:\\Users\\ZaidAlsalh\\Desktop\\DELETE.png'))

    inputt1 =QtWidgets.QLineEdit(window1)
    inputt1.setGeometry(820,155,150,40)
    inputt1.setStyleSheet('background-color:#F4ECF7; color:black; font-size:17px; border:0.5px solid black ; border-radius:7px;')
    inputt1.setToolTip('ادخل ايدي الطالب المراد حذفة ')
    inputt1.setPlaceholderText('  ادخل الايدي :  ')
    
    def pres_input2():
        print(inputt1.text())
        c.execute('''
                  delete from Students where id=?
                  ''',(inputt1.text()),)
    
    button_2.clicked.connect(pres_input2)
    window1.show()
    window1.exec_()

    
def pris2():
    window2 = QMainWindow()
    window2.setWindowTitle('All Lecturer')
    window2.setStyleSheet('background-color:#FBEEE6;')
    window2.setWindowIcon(QtGui.QIcon('C:\\Users\\ZaidAlsalh\\Desktop\\Lecturer.png'))
    window2.setGeometry(800, 200, 800, 400)
    
    
    table = QTableWidget(window2)
    table.setGeometry(5,0,800,800)
    table.setStyleSheet('background-color:#F4ECF7; color:black; font-size:18px; border:1px solid black ; border-radius:9px;')
    table.setColumnCount(6)
    table.setHorizontalHeaderLabels(['ID' , 'firstname' , 'lastName' , 'email', "hierdate", "department"])
    coom = c.execute('select * from Lecturer')
    z = coom.fetchall()
    table.setRowCount(len(z))
    row = 0
    for i in z:
        table.setItem(row,0, QTableWidgetItem(str(i[0])))
        table.setItem(row,1, QTableWidgetItem(str(i[1])))
        table.setItem(row,2, QTableWidgetItem(str(i[2])))
        table.setItem(row,3, QTableWidgetItem(str(i[3])))
        table.setItem(row,4, QTableWidgetItem(str(i[4])))
        table.setItem(row,5, QTableWidgetItem(str(i[5])))

        row +=1
        
 
    


   
    
    window2.show()
    window2.exec_()

button1.clicked.connect(pris1)
button2.clicked.connect(pris2)


window.show()
app.exec_()

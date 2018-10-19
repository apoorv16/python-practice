import sqlite3
import re
import webbrowser
pj = input("enter name of new or existing project to open\n")
s = sqlite3.connect('%s'% pj)

class insert():
    def insert(self): 
        try:
            n = int(input("how many rows you want to insert\n"))
            for i in range(n):
                rollno = ''
                name = ''
                marks = ''
                r = int(input("enter rollno\n"))
                rollno = rollno + str(r)
                name = name + input("enter name\n")
                m = int(input("enter marks\n"))
                marks = marks + str(m)
                string = ''
                string = string + rollno + ',' + name + ',' + marks
                s.execute('insert into st values(%s)' % string)
                s.commit()
                return s
        except:
            print("Error!\n")


class display():
    def display(self):
        a = s.execute('select * from st')
        print("table : ")
        for i in a:
            print(i)

class delete():
    def delete(self):
        rn = int(input("enter student's rollno who want to delete\n"))
        s.execute('delete from st where rollno = (%d)' % rn)
        s.commit()
class update():
    def update(self):
        rn = int(input("enter student's rollno whose data you want to update\n"))
        col = input("enter coloumn you want to update\n")
        if col == 'rollno' or 'marks':
            val = int(input("enter new value\n"))
            s.execute('update st set %s = %d where rollno = %d'% (col,val,rn))
            s.commit()
        else:
            val = input("enter new value of name\n")
            s.execute('update st set %s = %s where rollno = %d'% (col,val,rn))
            s.commit()
class insert_from_csv_file():
    def csv(self):
        try:
            path = input("enter path of csv file\n")
            o = open(r'%s' % path)
            ab = o.read()
            b = re.findall("(.+),'", ab)
            for ij in b:
                b = int(ij)
            q = re.findall(",(.*?),",ab)
            for e in q:
                q = str(e)
            f = re.findall("',(.+)",ab)
            for e in f:
                f = int(e)
            n = int(input("do you want to insert or update ?\n 1. insert\n 2.update\n"))
            if n == 1:
                s.execute('insert into st values(%d,%s,%d)' % (b, q, f))
                s.commit()
                print("inserted successfully!\n")
            elif n == 2:
                col = input("enter coloumn name you want to update\n")
                if col == 'rollno' or 'marks':
                    val = int(input("enter new value\n"))
                    s.execute('update st set %s = %d where rollno = %d' % (col, val, b))
                    s.commit()
                    print("updated successfully\n")
        except:
            print("error please try again")
class close():
    def close(self):
        s.close()
        print("file closed successfully\n")


while True:
    print("1.insert\n 2.display\n 3.delete\n 4.update value\n 5.insert/update from a csv file\n 6.close file\n")
    val = int(input("enter what do you want to do\n"))
    if val == 1:
        i = insert()
        i.insert()
        input("press enter to view menu\n")
    elif val == 2:
        d = display()
        d.display()
        input("press enter to view menu\n")
    elif val == 3:
        de = delete()
        de.delete()
        input("press enter to view menu\n")
    elif val == 4:
        u = update()
        u.update()
        input("press enter to view menu\n")
    elif val == 5:
        w = insert_from_csv_file()
        w.csv()
        input("press enter to view menu\n")
    elif val == 6:
        c = close()
        c.close()
        break

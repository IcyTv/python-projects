import sqlite3 as sql
import argparse, os

parser = argparse.ArgumentParser(description='AlarmClock')

parser.add_argument('-l','--list',action='store_true',help='Show all contacts', dest='list')
parser.add_argument('-a','--add', action='store_true', help='Add new contacts', dest='add')
parser.add_argument('-e', '--edit', action='store_true', help='Edit contacts', dest='edit')
parser.add_argument('-del', '--delete', action='store_true', help='Delete contact', dest='delete')
parser.add_argument('-n','--name',action='store', help='Name of the contact', dest='name')
parser.add_argument('-adr','--adress', action='store', help='Adress of contact', dest='adress')
parser.add_argument('-ph', '--phone', action='store', help='Phone number of contact', dest='phone')
parser.add_argument('-w', '--work', action='store', help='Workplace of contact', dest='work')
parser.add_argument('-r', '--relationship', action='store', help='Relationship to the contact', dest='relationship')

results = parser.parse_args()
results.res = results.relationship

def connect():
    global connection, cursor
    try:
        connection = sql.connect('./assets/AdressBook.db')
    except:
        import os
        os.system('mkdir assets')
        connection = sql.connect('./assets/AdressBook.db')
    cursor = connection.cursor()
    try:
        cursor.execute("""
        CREATE TABLE book (
        id INTEGER PRIMARY KEY,
        name VARCHAR(50),
        adress VARCHAR(200),
        phone VARCHAR(40),
        work VARCHAR(50),
        rel VARCHAR(25)
        );""")
        print 'CREATED TABLE'
    except:
        pass


if __name__ == '__main__':
    connect()
    if results.list:
        print 'ALL CONTACTS'
        cursor.execute('SELECT * FROM book')
        for i in cursor.fetchall():
            print "\n---------------------\n"
            for n in i:
                if type(n) != type(1) and type(n) != type(None):
                    print n.encode("utf-8","ignore")
        print "\n---------------------\n"

    elif results.add:
        print 'NEW CONTACT'
        if results.name:
            cursor.execute('SELECT * FROM book WHERE name="{}"'.format(results.name))
            if not cursor.fetchone():
                if not results.phone:
                    results.phone = 'NULL'
                else:
                    results.phone = '"{}"'.format(results.phone)
                if not results.adress:
                    results.adress = 'NULL'
                else:
                    results.adress = '"{}"'.format(results.adress)
                if not results.work:
                    results.work = 'NULL'
                else:
                    results.work = '"{}"'.format(results.work)
                if not results.rel:
                    results.rel = 'NULL'
                else:
                    results.rel = '"{}"'.format(results.rel)
                cursor.execute('INSERT INTO book (id, name, adress, phone, work, rel) VALUES (NULL, "{}", {}, {}, {}, {})'.format(results.name, results.adress, results.phone, results.work, results.rel))
            else:
                print 'NAME ALREADY EXISTS'
        else:
            print 'NAME MISSING'
    elif results.delete:
        print 'DELETE CONTACT'
        if results.name:
            cursor.execute('DELETE FROM book WHERE name="{}"'.format(results.name))
        else:
            print 'NAME MISSING'
    elif results.edit:
        print 'EDIT CONTACT'
        if results.name:
            if results.phone:
                cursor.execute('UPDATE book SET phone="{}" WHERE name="{}"'.format(results.phone, results.name))
            if results.adress:
                cursor.execute('UPDATE book SET adress="{}" WHERE name="{}"'.format(results.adress, results.name))
            if results.work:
                cursor.execute('UPDATE book SET work="{}" WHERE name="{}"'.format(results.work, results.name))
            if results.rel:
                cursor.execute('UPDATE book SET rel="{}" WHERE name="{}"'.format(results.rel, results.name))
        else:
            'NAME MISSING'
    else:
        print 'NO ARGUMENTS SPECIFIED'
        os.system('"{}"'.format(__file__) + ' -h')
    connection.commit()
    connection.close()

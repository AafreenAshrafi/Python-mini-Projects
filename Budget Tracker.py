#budget tracker
import sqlite3
import time
import datetime
conn = sqlite3.connect('BudgetTracker.db')
c = conn.cursor()
#to make db connect above used
def create_Tabe():
    c.execute('CREATE TABLE IF NOT EXISTS stufftoplot(datestamp TEXT,Expenses REAL,Income REAL,RecuuringCost REAL)')
def data_entry():
    datestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    Income = int(input('enter the income '))
    Expenses = int(input('enter the expenses '))
    #here is recurring calculations
    RecurringCost = int(((Income-Expenses)/Income)*100)
    print('the recurring cost in percentage is ',RecurringCost,'%')
    c.execute('INSERT INTO stufftoplot(datestamp,Expenses,Income,RecuuringCost) Values(?,?,?,?)',(datestamp,Expenses,Income,RecurringCost))
    conn.commit()
def read_data():
    #day = input('enter the date from which you want to get data (example:2018-09-22 00:33:35) ')
    c.execute("SELECT * FROM stufftoplot where datestamp > '2018-09-22 00:33:35'")
    data = c.fetchall()
    print(data)
    #for row in c.fetchall():
    #print('your recurring cost is ',row[2])
def del_data():
    c.execute('DELETE from stufftoplot')

Choice=input('''choose 1: to enter data
             choose 2: to show data
             any key: to exit
             ''')
if Choice =='1':
    data_entry()
else :
    read_data()

    

    
    
#del_data()    
#create_Tabe()


#read_data()
c.close()
conn.close

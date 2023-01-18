from datetime import date
from random import randint

from bokeh.io import output_file, show
from bokeh.layouts import widgetbox as wd
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn

import pymssql

sqlConn = None

def connectSQLServer():
    
    attr = dict(
        server = '10.20.213.10',
        database = 'csc1002',
        user = 'csc1002',
        password = 'csc1002',
        port = 1433,
        as_dict = True
    )

    try:
        return pymssql.connect(**attr)
    except Exception as e:
        print(e)
        quit()


#Select Query
def select():
    print ('Fetching course data from SQL server ...')
    tsql = "SELECT * FROM lgu.course order by dept_name"
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql)
        a = []
        b = []
        c = []
        d = []
        e = []
        for row in cursor:
            #print(row['dept_name'], row['title'])
            a.append(row['course_id'])
            b.append(row['title'])
            c.append(row['dept_name'])
            d.append(row['credits'])
            e.append('instructor')
        output_file('data_table.html')

    data = dict(
            course_id=a,
            title=b,
            dept_name=c,
            credits=d,
            instructor=e
        )
    source = ColumnDataSource(data)

    columns = [
            wd.TableColumn(field="course_id", title="Course ID"),
            wd.TableColumn(field="title", title="Title"),
            wd.TableColumn(field='dept_name',title='Deptment'), 
            wd.TableColumn(field='credits',title='Credits'),
            wd.TableColumn(field='instructor',title='Instructor')
        ]
    data_table = wd.DataTable(source=source, columns=columns, width=400, height=280)

    show(widgetbox(data_table))
if __name__ == '__main__':
    sqlConn = connectSQLServer()
    select()



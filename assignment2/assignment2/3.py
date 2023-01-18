import pymssql
from bokeh.layouts import widgetbox, layout
from bokeh.plotting import curdoc
from bokeh.io import show
from bokeh.models import widgets as wd
import string
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn

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
            TableColumn(field="course_id", title="Course ID"),
            TableColumn(field="title", title="Title"),
            TableColumn(field='dept_name',title='Deptment'), 
            TableColumn(field='credits',title='Credits'),
            TableColumn(field='instructor',title='Instructor')
        ]
    data_table = DataTable(source=source, columns=columns, width=400, height=280)

    curdoc().add_root(widgetbox(data_table))

def structure():
    btnGroupLetters = RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
    btnGroupTitle = RadioButtonGroup(name='title',labels=['begins with...','...contains...','...ends with'],active=1)
    btnGroupDept = RadioButtonGroup(name='title',labels=['begins with...','...contains...','...ends with'],active=1)
    title_input = wd.TextInput(title='Title',value='',placeholder='contains......')
    paragraph = wd.Paragraph(text='option')
    optionGroup = wd.RadioGroup(labels=['and','or'],active=0)
    dept_input = wd.TextInput(title='Department',value='',placeholder='contains......')
    refresh = Button(label='Refresh')
    refresh.on_click(select)
    layout_query = layout(
        [
            [widgetbox(btnGroupLetters,width=1000)],
            [widgetbox(btnGroupTitle),widgetbox(btnGroupDept)],
            [widgetbox(title_input),widgetbox(paragraph,optionGroup,width=100),widgetbox(dept_input)],
            [widgetbox(refresh,width=100)]
        ]
    )

    layout_chart = layout(
        []
    )

    tab1 = wd.Panel(child=layout_query,title='Course Info')
    tab2 = wd.Panel(child=layout_chart,title='Statistics')
    tabs = Tabs(tabs=[tab1,tab2])

    curdoc().add_root(tabs)


if __name__ == '__main__':
    sqlConn = connectSQLServer()
    select()
    structure()

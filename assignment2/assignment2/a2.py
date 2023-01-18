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
    tsql = "SELECT * FROM lgu.course order by dept_name"
    with sqlConn.cursor(as_dict=True) as cursor:
        cursor.execute(tsql)
        


if __name__ == '__main__':
    sqlConn = connectSQLServer()
    select()

from bokeh.layouts import widgetbox, layout
from bokeh.plotting import curdoc
from bokeh.models.widgets import RadioButtonGroup,Button,Select,MultiSelect,TextInput,Tabs,RadioGroup
from bokeh.io import show
from bokeh.models import widgets as wd
import string

btnGroupLetters = RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
btnGroupTitle = RadioButtonGroup(name='title',labels=['begins with...','...contains...','...ends with'],active=1)
btnGroupDept = RadioButtonGroup(name='title',labels=['begins with...','...contains...','...ends with'],active=1)
title_input = wd.TextInput(title='Title',value='',placeholder='contains......')
paragraph = wd.Paragraph(text='option')
optionGroup = wd.RadioGroup(labels=['and','or'],active=0)
dept_input = wd.TextInput(title='Department',value='',placeholder='contains......')
refresh = Button(label='Refresh')

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





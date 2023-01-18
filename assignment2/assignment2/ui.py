from bokeh.layouts import widgetbox, layout
from bokeh.plotting import curdoc
from bokeh.models.widgets import RadioButtonGroup,Button,Select,MultiSelect,TextInput,Tabs,RadioGroup
from bokeh.io import show
from bokeh.models import widgets as wd
import string
from datetime import date
from random import randint
from bokeh.io import output_file, show
from bokeh.layouts import widgetbox
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




output_file('ui.html')

data = dict(
        dates=[date(2014, 3, i+1) for i in range(10)],
        downloads=[randint(0, 100) for i in range(10)],
    )
source = ColumnDataSource(data)

columns = [
        TableColumn(field="dates", title="Date", formatter=DateFormatter()),
        TableColumn(field="downloads", title="Downloads"),
    ]
data_table = DataTable(source=source, columns=columns, width=400, height=280)

def refreshClock():
    show(widgetbox(data_table))

btnGroupLetters = RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
btnGroupTitle = RadioButtonGroup(name='title',labels=['begins with...','...contains...','...ends with'],active=1)
btnGroupDept = RadioButtonGroup(name='title',labels=['begins with...','...contains...','...ends with'],active=1)
title_input = wd.TextInput(title='Title',value='',placeholder='contains......')
paragraph = wd.Paragraph(text='option')
optionGroup = wd.RadioGroup(labels=['and','or'],active=0)
dept_input = wd.TextInput(title='Department',value='',placeholder='contains......')
refresh = Button(label='Refresh')
refresh.on_click(refreshClock)



layout_query = layout(
    [
        [widgetbox(btnGroupLetters,width=1000)],
        [widgetbox(btnGroupTitle),widgetbox(btnGroupDept)],
        [widgetbox(title_input),widgetbox(paragraph,optionGroup,width=100),widgetbox(dept_input)],
        [widgetbox(refresh,width=100)]
        [widgetbox(data_table)]
    ]
)

layout_chart = layout(
    []
)



tab1 = wd.Panel(child=layout_query,title='Course Info')
tab2 = wd.Panel(child=layout_chart,title='Statistics')
tabs = Tabs(tabs=[tab1,tab2])




curdoc().add_root(tabs,data_table)











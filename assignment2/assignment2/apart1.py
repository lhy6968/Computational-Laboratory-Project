from bokeh.models import widgets as wd
from bokeh.plotting import curdoc
def structure():
    btnGroupLetters = wd.RadioButtonGroup(labels=list(string.ascii_uppercase), active=-1)
    btnGroupTitle = wd.RadioButtonGroup(name='title',labels=['begins with...','...contains...','...ends with'],active=1)
    btnGroupDept = wd.RadioButtonGroup(name='title',labels=['begins with...','...contains...','...ends with'],active=1)
    title_input = wd.TextInput(title='Title',value='',placeholder='contains......')
    paragraph = wd.Paragraph(text='option')
    optionGroup = wd.RadioGroup(labels=['and','or'],active=0)
    dept_input = wd.TextInput(title='Department',value='',placeholder='contains......')
    refresh = wd.Button(label='Refresh')
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

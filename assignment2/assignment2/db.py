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
        for row in cursor:
            print(row['dept_name'], row['title'])

if __name__ == '__main__':
    sqlConn = connectSQLServer()
    select()

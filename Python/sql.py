import pyodbc

server = 'HYDTRNG5\SQLEXPRESS'
database = 'rajasree'
username = 'sa'
password = 'rajasree@123'
cxcn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)


mycursor = cxcn.cursor()
res = mycursor.execute("select empno,sal,comm from emp")
myrecs = res.fetchall();
print(myrecs)
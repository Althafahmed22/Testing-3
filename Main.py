import  mysql.connector as Mc
connection=Mc.connect(host='localhost',
                                   user='root',
                                   password='Althafmd4321@',
                                   database='Python_Db')
if connection.is_connected():
    print("DataBase connect Sucessfully......")
# create_table_query = """
#         CREATE TABLE Employees (
#             EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
#             FirstName VARCHAR(50) NOT NULL,
#             LastName VARCHAR(50) NOT NULL,
#             Email VARCHAR(100) UNIQUE,
#             HireDate DATE NOT NULL,
#             Salary DECIMAL(10, 2),
#             DepartmentID INT
#         );
#         """
cursor=connection.cursor()
#cursor.execute(create_table_query)
print("table created sucessfully........" )
Show_Table = "Select * from Employees"
cursor.execute(Show_Table)



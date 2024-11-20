import pyodbc

try:
    conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\MSSQLLocalDB;DATABASE=BeerDB;Trusted_Connection=yes'
    )

    # conn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=(local);PORT=1433;DATABASE=BeerDB;UID=flask_user;PWD=admin123')
    # conn = pyodbc.connect('Trusted_Connection=yes', driver = '{ODBC Driver 17 for SQL Server}',
    #                   server = 'localdb', database = 'BeerDB')
    print("Connection successful!")
except Exception as e:
    print(f"Connection failed: {e}")
import pyodbc

def get_connection():
    str_connection = (
        "Driver={MySQL ODBC 9.2 Unicode Driver};"
        "Server=localhost;"
        "Database=caminatas_caninas;"
        "PORT=3306;"
        "User=user_ptyhon;"
        "Password=Clas3s1Nt2024_!;"
    )
    try:
        connection = pyodbc.connect(str_connection)
        return connection
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

import psycopg2

#conn = psycopg2.connect(database="scrapping", user="postgres", password="123456", host="127.0.0.1", port="5432")
conn = psycopg2.connect(database="de13n0npb5i3e2", user="wqmogzpwevlzeo", password="3191ee1775b5d2f24bd3e942bc43b673822c30afefd75704f1909de27c3c6176", host="ec2-54-235-153-124.compute-1.amazonaws.com", port="5432")
print ("Opened database successfully")

def createTables():
    cur = conn.cursor()
    
    cur.execute('''CREATE TABLE WebPages
       (ID SERIAL PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL);''')

    
    cur.execute('''CREATE TABLE Auditoria
       (ID SERIAL PRIMARY KEY     NOT NULL,
        PageID SERIAL references WebPages(ID) NOT NULL,
        Date TEXT NOT NULL,
        Errores TEXT NOT NULL,
        Estado TEXT NOT NULL,
        Registros INT NOT NULL);''')

    

    cur.execute('''CREATE TABLE Bet
       (Team1 TEXT NOT NULL,
        Team2 TEXT NOT NULL,
        PageID SERIAL references WebPages(ID) NOT NULL, 
        Year INT NOT NULL,
        Time1 VARCHAR(5),
        Draw REAL NOT NULL,
        Bet1 REAL NOT NULL,
        Bet2 REAL NOT NULL,
        PRIMARY KEY(Year,Team1,Team2,PageID)
        
        );''')
    print("Table created successfully")

    conn.commit()
    conn.close()

createTables()

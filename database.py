import psycopg2

conn = psycopg2.connect(database="scrapping", user="postgres", password="123456", host="127.0.0.1", port="5432")
print ("Opened database successfully")

def createTables():
    cur = conn.cursor()
    cur.execute('''CREATE TABLE WebPages
       (ID SERIAL PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL);''')

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

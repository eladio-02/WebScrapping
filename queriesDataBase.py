import psycopg2

conn = psycopg2.connect(database="scrapping", user="postgres", password="123456", host="127.0.0.1", port="5432")
print ("Opened database successfully")


def selectWebPage(name):
    
    cur = conn.cursor()
    cur.execute("SELECT id from webpages where name = '"+name+"'"+";")
    rows = cur.fetchall()
    if(len(rows)==0):
        return True
    return False

def selectGame(team1,team2,year,page):
    cur = conn.cursor()
    cur.execute("SELECT * from bet where team1 = '"+team1+"' and team2 = '"+team2+"' and year = "+str(year)+" and pageid = "+str(page)+";")
    rows = cur.fetchall()
    if(len(rows)==0):
        return True
    return False
    
def insertWebPage(name):
    try:
        
        conn = psycopg2.connect(database="scrapping", user="postgres", password="123456", host="127.0.0.1", port="5432")
        if(selectWebPage(name)):
            cur = conn.cursor()
            cur.execute("INSERT INTO webpages (name) VALUES "+ "('" +name + "')");
            conn.commit()
            print("Records created successfully")
            conn.close()
        else:
            print("Ya existe esa pagina que desea insertar")
    except:
        print("Ha ocurrido un problema con la inserción de la pagina web")
    
    
def insertMatchInfo(team1,team2,year,time,bet1,draw,bet2,page):
    
    conn = psycopg2.connect(database="scrapping", user="postgres", password="123456", host="127.0.0.1", port="5432")
    if (selectGame(team1,team2,year,page)):
        cur = conn.cursor()
        
        cur.execute("INSERT INTO bet (Team1, Team2, PageID, Year, Time1, Draw, Bet1, Bet2) \
          VALUES ('"+team1+"','"+team2+"',"+str(page)+","+str(year)+",'"+str(time)+"',"+str(draw)+","+str(bet1)+","+str(bet2)         +");");
        conn.commit()
        print("Records created successfully");
        conn.close()
insertWebPage('bet365')
insertWebPage('wanabet')


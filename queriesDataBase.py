import psycopg2

#conn = psycopg2.connect(database="scrapping", user="postgres", password="123456", host="127.0.0.1", port="5432")
conn = psycopg2.connect(database="de13n0npb5i3e2", user="wqmogzpwevlzeo", password="3191ee1775b5d2f24bd3e942bc43b673822c30afefd75704f1909de27c3c6176", host="ec2-54-235-153-124.compute-1.amazonaws.com", port="5432")

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


def insertAuditoria(page, date, errores, estado, registros):
    try:
        
        conn = psycopg2.connect(database="de13n0npb5i3e2", user="wqmogzpwevlzeo", password="3191ee1775b5d2f24bd3e942bc43b673822c30afefd75704f1909de27c3c6176", host="ec2-54-235-153-124.compute-1.amazonaws.com", port="5432")
        
        cur = conn.cursor()
        print("INSERT INTO auditoria (page, date, errores, estado, registros) \
        VALUES ("+str(page)+",'"+date+"', '"+errores+"', '"+estado+"', "+str(registros)+");")
        
        cur.execute("INSERT INTO auditoria (pageid, date, errores, estado, registros) \
        VALUES ("+str(page)+",'"+date+"', '"+errores+"', '"+estado+"', "+str(registros)+");");
        conn.commit()
        print("Records created successfully")
        conn.close()
        
    except:
        print("Ha ocurrido un problema con la inserción")

        
    
def insertWebPage(name):
    try:
        
        conn = psycopg2.connect(database="de13n0npb5i3e2", user="wqmogzpwevlzeo", password="3191ee1775b5d2f24bd3e942bc43b673822c30afefd75704f1909de27c3c6176", host="ec2-54-235-153-124.compute-1.amazonaws.com", port="5432")
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
    
    conn = psycopg2.connect(database="de13n0npb5i3e2", user="wqmogzpwevlzeo", password="3191ee1775b5d2f24bd3e942bc43b673822c30afefd75704f1909de27c3c6176", host="ec2-54-235-153-124.compute-1.amazonaws.com", port="5432")
    if (selectGame(team1,team2,year,page)):
        cur = conn.cursor()
        
        cur.execute("INSERT INTO bet (Team1, Team2, PageID, Year, Time1, Draw, Bet1, Bet2) \
          VALUES ('"+team1+"','"+team2+"',"+str(page)+","+str(year)+",'"+str(time)+"',"+str(draw)+","+str(bet1)+","+str(bet2)         +");");
        conn.commit()
        print("Records created successfully");
    conn.close()
insertWebPage('bet365')
insertWebPage('wanabet')


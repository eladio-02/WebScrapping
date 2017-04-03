from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import queriesDataBase as DB
import unicodedata
import datetime

dicc = {'Ene':'01','Feb':'02','Mar':'03','Abr':'04','May':'05','Jun':'06','Jul':'07','Ago':'08','Set':'09','Oct':10,'Nov':11,'Dic':12}

'''def scrappingBet365Date(elemento):
    bet365 = webdriver.Chrome()
    bet365.get("https://www.bet365.es/")
    bet365.implicitly_wait(15) # seconds
    bet365.find_element_by_class_name("lpdgl").click()
    bet365.implicitly_wait(30) # seconds
    bet365Parser = BeautifulSoup(bet365.page_source, 'html.parser')
    bet365.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div[14]").click()
    
    bet365.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]").click()
    bet365Parser = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')
    print(bet365.find_elements_by_xpath("//*[contains(text(), '"+elemento.getText()+"')]"))
    bet365.find_elements_by_xpath("//*[contains(text(), '"+elemento[0].getText()+"')]").click()
    

    
    date = bet365Parser.find_all('div', {"class":["cm-MarketGroupExtraData_TimeStamp "]})
    arrayDate = date[0].getText().split(" ")
    bet365.close()
    bet365.quit()
    return(arrayDate[0]+"/"+dicc[arrayDate[1]]+"/"+str(datetime.datetime.now().year))
'''
def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
 
def scrappingWanabet():
    wanabet = webdriver.Chrome()
    wanabet.get("https://www.wanabet.es/#!/sport/filter/football/spain/laliga")
    wanabet.implicitly_wait(20) # seconds
    wanabetParser = BeautifulSoup(wanabet.page_source, 'html.parser')
    listaEquipos = wanabetParser.find_all('div', {"class":["KambiBC-event-participants__name","KambiBC-event-participants__name"]})
    listaApuestas = wanabetParser.find_all('span', {"class":["KambiBC-mod-outcome__odds"]})
    listaHoras = wanabetParser.find_all('span', {"class":["KambiBC-event-item__start-time--time"]})
    
    j=0
    i=0
    k=0
    print(len(listaEquipos))
    
    while i < (len(listaEquipos)):
        
        print(elimina_tildes(listaEquipos[i].getText().strip()),elimina_tildes(listaEquipos[i+1].getText().strip()))
        DB.insertMatchInfo(elimina_tildes(listaEquipos[i].getText().strip()),elimina_tildes(listaEquipos[i+1].getText().strip()),datetime.datetime.now().year, listaHoras[k].getText(),listaApuestas[j].getText(), listaApuestas[j+1].getText(),listaApuestas[j+2].getText(),2)
        
        k+=1
        i+=2
        j+=3
        
    
    wanabet.close()
    wanabet.quit()

        


def scrappingBet365():
    bet365 = webdriver.Chrome()
    
    bet365.get("https://www.bet365.es/")
    bet365.implicitly_wait(15) # seconds
    bet365.find_element_by_class_name("lpdgl").click()

    bet365.implicitly_wait(30) # seconds
    bet365Parser = BeautifulSoup(bet365.page_source, 'html.parser')
    bet365.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div[14]").click()

    bet365.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]").click()
    element = bet365.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div[2]/div")

    #print(element.get_attribute('innerHTML'))  
    #bet365.find_element_by_class_name("wn-Classification ").click()
    

    bet365Parser = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')

    
    listaEquiposHora = bet365Parser.find_all('div', {"class":["sl-CouponParticipantWithBookCloses sl-CouponParticipantIPPGBase sl-MarketCouponAdvancedBase_LastChild ","sl-CouponParticipantWithBookCloses sl-CouponParticipantIPPGBase "]})
    listaApuestas = bet365Parser.find_all('span',{"class":["gl-ParticipantOddsOnly_Odds"]})
    
    i=0
    
    for elemento in listaEquiposHora:
        #print(bet365Parser.find_element_by_xpath("//div[@class='"+elemento.getClass()+"']/div[text()='"+elemento.getText()+"']").click())
        teams = elemento.getText()[5::].split(" v ")
        
        #MatchInfo(team1,team2,year,time,bet1,draw,bet2,page)
        
        DB.insertMatchInfo(elimina_tildes(teams[0]),elimina_tildes(teams[1]),datetime.datetime.now().year,elemento.getText()[0:5],listaApuestas[i].getText(),listaApuestas[i+20].getText(),listaApuestas[i+40].getText(),1)
        #BS.MatchInfo(elemento.getText()[0:5] +" - "+str(datetime.datetime.now().year)+"     "+ str(elemento.getText()[5::].split(" v ")) + "            "+listaApuestas[i].getText()+"   "+listaApuestas[i+20].getText()+"  "+listaApuestas[i+40].getText())
        i+=1
        
    
    bet365.close()
    bet365.quit()
    
print("Haciendo Scrapping en Bet365.....")
scrappingBet365()
print("Haciendo Scrapping en Wanabet.....")
scrappingWanabet()

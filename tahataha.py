from bs4 import BeautifulSoup
import sys
import requests
import os
import time
import keyboard
keyboard.press_and_release('fill','chift')    
def getsource():
    geta = input('enter websites url:')
    print("yourwebsitesourcecode")
    print('=====================================================')
    getb = requests.get(geta)
    soup = BeautifulSoup(getb.text,'lxml')
    ask = input("***hello i am taha i want to code this tools because i want to be a programmer so i want to release the beautuful soup")
    if ask == "y":
        print(soup.pretify())
    else:
        var = soup.pretify()    
        f = open('geta.html','m')
        f.write(var)
        f.close()
        getsource()







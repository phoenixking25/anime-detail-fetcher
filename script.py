import click
from bs4 import BeautifulSoup
import requests
import sys
import re
import base64
import os
import Tkinter, tkFileDialog
import keyboard 


apiurl = "https://myanimelist.net/api/anime/search.xml?q="

@click.command(help = "It is a tool to get ratings and other information of the animes stored in a folder of can search itself too")


def main():
    auth = encoder()
    directory = getpath()
    dirs = os.listdir(directory)
    for i in dirs:
        try:
            if keyboard.is_pressed('q'):
                print('You Pressed A Key!')
                break
            elif keyboard.is_pressed('s'):
                continue
        except:
            pass
        req_url = apiurl + i.replace(" ", "_")
        print "searching for %r......."% i
        headers = {"Authorization": "Basic " + auth}
        r = requests.get(req_url, headers = headers)
        data = r.text
        if data == '':
            print "name error"
            continue
        soup = BeautifulSoup(data, 'html.parser')
        # print data.encode('cp437', 'ignore')
        name = []
        scores = []
        for score in soup.find_all('score'):
            scores.append(score.string)
        for title in soup.find_all('title'):
            name.append(title.string)
        for i in xrange(len(name)):
            print name[i].encode('cp437', 'ignore')
            print scores[i]


def encoder():
    username = raw_input("Enter your myanimelist username: ").strip()
    password = raw_input("Enter your myanimelist password: ").strip()
    encoded = base64.b64encode(username + ":" + password)
    return encoded

def getpath():
    root = Tkinter.Tk()
    root.withdraw()
    dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    return dirname

if __name__ == '__main__':
    main()

import imaplib
import pprint
import imaplib_connect
import subprocess
import ConfigParser
import sys
import re
from email import parser
import requests
import json
import urllib2
import os

def sendRequest(mailFrom,eventName,apiKey):
    url = "https://maker.ifttt.com/trigger/" + eventName + "/with/key/" + apiKey
    print url
    payload = "{\"value1\" : \"" + mailFrom + "\"}"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.17.1",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "fa0abf01-12a1-412c-91ef-48c68369137c,6148a7af-e753-4c92-a2ca-a393d524f84b",
        'Host': "maker.ifttt.com",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "29",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

config = ConfigParser.ConfigParser()
config.read([os.path.abspath('settings.ini')])

eventName = config.get("IFTT","eventName")
apiKey = config.get("IFTT","apiKey")

print "the Event Name is " + eventName
print "the API Key is " + apiKey

imaplib.Debug = 4
c = imaplib_connect.open_connection()
c.select()

typ,gotString =  c.fetch(sys.argv[1],"(RFC822)")

msg = parser.Parser().parsestr(gotString[0][1])
print msg["From"]
for key in config.options("MAGNET"):
    z = re.search(key,msg["From"])
    if z:
        print "Got Mail from " + key + " i.e2 " + config.get("MAGNET",key)
        sendRequest(config.get("MAGNET",key),eventName,apiKey)
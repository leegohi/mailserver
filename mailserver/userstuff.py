#encoding:utf-8
import requests
import quopri

def do_stuff(b):
    decode_string=quopri.decodestring(b)
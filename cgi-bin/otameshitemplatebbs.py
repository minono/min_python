#!/home/minori/.pyenv/shims/python
# coding:utf-8

import sqlite3
con = sqlite3.connect(":memory:")

text_factory = str
from string import Template
from os import path
from httphandler import Request, Response#, get_htmltemplate
import cgitb; cgitb.enable()

cur = con.cursor()

try:
    cur.execute("""CREATE TABLE bookmark (title text, url text);""")

except:
    pass

req = Request()
f = req.form
value_dic = {'message':'', 'title':'', 'url':'', 'bookmarks':''}

if f.has_key('post'):
    if not f.getvalue('title', '') or not f.getvalue('url', ''):
        value_dic['message'] = u'タイトルとURLは必須項目です'
        value_dic['title'] = unicode(f.getvalue('title', ''), 'utf-8', 'ignore')
        value_dic['url'] = f.getvalue('url', '')

    else:
        sql = """INSERT into bookmark(title, url) VALUES(?, ?)"""
        cur.execute(sql,(f.getvalue('title', ''), f.getvalue('url', '')))
        
                    
        con.commit()
        con.close()

#追加部分




res = Response()
f = open(path.join(path.dirname(__file__), 'bookmarkform.html'))
t = Template(unicode(f.read(), 'utf-8', 'ignore'))
body = t.substitute(value_dic)
res.set_body(body)
print res


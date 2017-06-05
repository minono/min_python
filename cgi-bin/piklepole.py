#!home/minori/.pyenv/shims/python
# coding:utf-8

import pickle
from httphandler import Request, Response, get_htmltemplate
import cgitb; cgitb.enable()

form_body = u"""

    <form method="POST" action="/cgi-bin/pickle.pyenv">
        好きな軽量言語は？<br />
        %s
        <input type="submit" />
    </form>"""

radio_parts = u"""
<input type="radio" name="language" value="%s" />%s
<div style="border-left: solid %sem red; ">%s</div>
"""

lang_dic = {}
try:
    f = open('./favorite_language.dat')
    lang_dic = pickle.load(f)
except IOError:
    pass

content = ""req = Request()
if req.form.has_key('language'):
    lang = req.form['language'].value
    lang_dic[lang] = lang_dic.get(lang, 0) +1


f = open('./favorite_language.dat', 'w')
pickle.dunp(lang_dic, f)

for lang in ['Perl', 'PHP', 'Python', 'Ruby']:
    num = lang_dic.get(lang, 0)
    content += radio_parts%(lang, lang, num, num)

res = Response()
body = form_body%content
rss.set_body(get_htmltemplate()%body)
print res

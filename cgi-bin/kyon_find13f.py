content = ""
>"

    if friday13:
        content += u"%d年には合計%d個の13日の金曜日があります" % (
            year, friday13)
    else:
        content += u"%d年には13日の金曜日がありません"


print "Content-type: text/html\n"
print (html_body % content).encode("utf-8")







content = ""
>"

    if friday13:
        content += u"%dǯ�ˤϹ��%d�Ĥ�13���ζ�����������ޤ�" % (
            year, friday13)
    else:
        content += u"%dǯ�ˤ�13���ζ�����������ޤ���"


print "Content-type: text/html\n"
print (html_body % content).encode("utf-8")







# -*- coding: utf-8 -*-


def readfile(name):
    file = open(name, 'r')
    content = file.read()
    file.close()
    return content


def writefile(name, content):
    file = open(name, 'w')
    file.write(content)
    file.close()

#!/usr/bin/python
# coding: utf-8

class fiddler_response:
    def __init__(self):
        pass

    def get_file(self):
        f_bh = open('Response.txt',"r")
        content_bh = f_bh.read().decode("utf-16")
        lines_bh = content_bh.split('\n')
        tmp = lines_bh[4].split("data\":")
        print tmp[1]
        item = tmp[1].replace('u\'','\'r')
        print item
        return item[0].split(", \"info\"")

    def get_response_list(self):
        pass
if __name__ == '__main__':
    a= fiddler_response()
    print type(a.get_file()[0].replace('u\'',''))
    print a.get_file()[0].replace('u\'',' ')
    print a.get_file()
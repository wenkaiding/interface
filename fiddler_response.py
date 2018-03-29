#!/usr/bin/python
# coding: utf-8
import json

class fiddler_response:
    def __init__(self):
        pass

    def get_file(self):
        f_bh = open('D:\Fiddler Sessions\Response.txt',"r")
        content_bh = f_bh.read().decode("utf-16")
        lines_bh = content_bh.split('\n')
        tmp = lines_bh[4].split("data\":")
        tem = tmp[1].split("\"info\"")
        return  json.loads(str(tem[0][0:tem[0].__len__()-1]))

    def get_response_list(self):
        item = []
        for tem in self.get_file()["product_list"]:
            item.append(tem)
        return self.add_icon(item)
    def add_icon(self,list):
        for item in list:
            if isinstance(item,dict):
                if item["is_tmall"]==1 or item["productstyle"] == "superfan":
                    item["title"] = "icon "+item["title"]
            return list

    def check_response(self,ui,fid):
        if isinstance(ui,list) and isinstance(fid,list):
            for i in range(0,ui.__len__()):
                self.check_response(ui[i],fid[i])

        elif isinstance(ui,dict) and isinstance(fid,dict):
            for k,v in ui:
                assert ui[k]==fid[k],"ui result is different from fiddler response，" \
                                     "ui result is：{} and fiddler response is ：{}".format(ui[k],fid[k])
        else:
            return "input error，must be list or dict"

    def clear_file(self):
        f = open('D:\Fiddler Sessions\Response.txt', "w")
        f.truncate()


if __name__ == '__main__':
    a= fiddler_response()
    print a.get_response_list()

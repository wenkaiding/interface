#!/usr/bin/python
# coding: utf-8
import json
import os
import time
import unittest
from appium import webdriver

class demo:
    def __init__(self):
        PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Lenovo P1c72'
        desired_caps['app'] = PATH('C:\Users\wenkai.ding\Desktop\Fanli.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)





        # desired_caps['appPackage'] = 'com.xiangchao.starspace'　　
        # desired_caps['appActivity'] = 'com.xiangchao.starspace.activity.SplashActivity'

        # 如果设置的是app在电脑上的路径，则不需要配appPackage和appActivity，同理反之


    def run_test(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']

        time.sleep(10)
        self.driver.swipe(x * 3 / 4, y / 2, x / 8, y / 2, 800)
        time.sleep(10)
        self.driver.swipe(x * 3 / 4, y / 2, x / 8, y / 2, 800)
        time.sleep(3)
        self.driver.swipe(x * 3 / 4, y / 2, x *3/4 , y / 2, 800)
        time.sleep(10)



        self.driver.find_element_by_id("com.fanli.android.apps:id/tv_search_hint").click()
        self.driver.find_element_by_id("com.fanli.android.apps:id/home_search_pre_edit_head_search_edit_btn").send_keys("123456")
        self.driver.find_element_by_id("com.fanli.android.apps:id/home_search_pre_edit_head_search_btn").click()
        city_list = []
        shop_list = []
        price_list = []
        title_list = []
        fanli_content_list = []
        self.driver.swipe(500,811,500,330,4000)
        for i in range(0,4):
            time.sleep(6)
            title = self.driver.find_elements_by_id("com.fanli.android.apps:id/item_home_search_result_product_name")
            shop = self.driver.find_elements_by_id("com.fanli.android.apps:id/item_info_middle_shop_name")
            city = self.driver.find_elements_by_id("com.fanli.android.apps:id/item_info_middle_address")
            price = self.driver.find_elements_by_id("com.fanli.android.apps:id/item_home_search_result_product_price")
            fanli_content = self.driver.find_elements_by_id("com.fanli.android.apps:id/item_home_search_result_product_price")
            print "title:{}".format(title)
            print i
            for tem in title:
                title_list.append(tem.text)
            for tem in shop:
                shop_list.append(tem.text)
            for tem in city:
                city_list.append(tem.text)
            for tem in price:
                price_list.append(tem.text)
            for tem in fanli_content:
                fanli_content_list.append(tem.text)

            print "title_list:{}".format(title_list)
            print "shop_list{}".format(shop_list)
            print "city_list{}".format(city_list)
            print "price_list{}".format(price_list)
            print "fanli_content_list{}".format(fanli_content_list)
            time.sleep(3)
            for i in range(0,5):
                self.driver.swipe(500, 367, 500, 1, 5000)
        all_list = [title_list,shop_list,city_list,price_list,fanli_content_list]
        return all_list

    def swipe_to_next(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 1 / 2, y * 90 / 100, x * 1 / 2, y * 80 / 100, 450)

    def get_ui_item(self,all_list):
        item=[]

        for i in range(0,10):
            tmp = {}
            tmp["title"]=all_list[0][i]
            tmp["shopname"]=all_list[1][i]
            tmp["city"]=all_list[2][i]
            tmp["promotion_price"]=all_list[3][i]
            print "++++++++++++++++++++++++++++++"
            print i
            print tmp
            print "++++++++++++++++++++++++++++++"
            item.append(tmp)
        print item
        print "##########"
        return item


    def get_file(self):
        f_bh = open('Response.txt', "r")
        content_bh = f_bh.read().decode("utf-16")
        lines_bh = content_bh.split('\n')
        tmp = lines_bh[4].split("data\":")
        tem = tmp[1].split("\"info\"")
        return json.loads(str(tem[0][0:tem[0].__len__() - 1]))


    def get_response_list(self):
        item = []
        for tem in self.get_file()["product_list"]:
            item.append(tem)
        return item


    def check_response(self, ui, fid):
        if isinstance(ui, list) and isinstance(fid, list):
            print ui
            print fid
            for k in range(0, ui.__len__()):
                print k
                self.check_response(ui[k], fid[k])

        elif isinstance(ui, dict) and isinstance(fid, dict):
            for k, v in ui.iteritems():
                print "now check ui_{}:{} fid_{}:{}".format(k,ui[k].encode("utf-8"),k,fid[k].encode("utf-8"))
                assert ui[k] == fid[k], "ui result is different from fiddler response，" \
                                        "ui result is：{} and fiddler response is ：{}".format(ui[k].encode("utf-8"),fid[k].encode("utf-8"))
        else:
            return "input error，must be list or dict"

    def main(self):
        all_list=self.run_test()
        ui_list=self.get_ui_item(all_list)
        fid_list = self.get_response_list()
        self.check_response(ui_list,fid_list)

if __name__ == '__main__':
    demo = demo()
    demo.main()


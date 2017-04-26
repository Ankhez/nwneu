# -*- coding:utf-8 -*-
import requests, datetime
from lxml import html


class MyParse(object):


    @staticmethod
    def checkthepagination(filename, url, **kwargs):
        r = requests.post(url, data = kwargs)
        with open(filename, 'w') as output_file:
            output_file.write(r.text.encode('utf-8'))

        with open(filename, 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            f.writelines(['<meta http-equiv="Content-Type" content="text/html;charset=utf-8">'] + lines)

#update parse file if we need
    @staticmethod
    def updateparse(filename, url, freq):
        if datetime.datetime.now().hour % freq == 0:
            MyParse.lets_parse(filename, url)

#parse from url to file
    @staticmethod
    def lets_parse(filename, url):
        r = requests.get(url)
        with open(filename, 'w') as output_file:
            output_file.write(r.text.encode('utf-8'))

#red file and return all info from
    @staticmethod
    def read_file(filename):
        with open(filename) as input_file:
            text = input_file.read()
        return text

#return info from xpath
    @staticmethod
    def parse_user_datafile_bs(filename, xpath):
        text = MyParse.read_file(filename)
        tree = html.fromstring(text)
        valuefromparse = tree.xpath(xpath)
        return valuefromparse

if __name__ == "__main__":
    pass

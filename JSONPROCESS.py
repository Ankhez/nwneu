# -*- coding: utf-8 -*-
import json
from BasicActions import BasicAction
import random


class JSONDate(BasicAction):
    class_description = "JSON_PROCESS"

    @staticmethod
    def forsave(filename):
        with open(filename, "r") as f:
            json_data = json.load(f)
            return json_data

    def writeinjson(self, filename, info):
        json_data = self.forsave(filename)
        with open(filename, "w+") as f:
            json_data.update(info)
            json.dump(json_data, f, ensure_ascii=False)

    def get_key(self, dictionary, item):
        for key, value in dictionary.items():
            if item.lower() in value:
                if key.__len__ != 0:
                    key = unicode.split(key, ', ')
                    numberofanswer = random.randrange(0, key.__len__())
                    return key[numberofanswer]
                else:
                    return key
        newitem = {None: item.encode('utf-8')}
        self.writeinjson("testjson.json", newitem)
        return item

    def compare_values(self, locator):
        foranswer = []
        values = self.get_text_from_element(locator)
        size = values.__len__()
        while size != 0:
            word = self.get_key(self.forsave("WordsAnswerDate.json"), values[size.__sub__(1)])
            foranswer.append(word)
            size -= 1
        return foranswer

    def name_add_with_action(self, filename, info):
        self.writeinjson(filename, info)






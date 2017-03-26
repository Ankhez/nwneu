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
            f.close()
            return json_data

    def writeinjson(self, filename, info):
        json_data = self.forsave(filename)
        with open(filename, "w+") as f:
            json_data.update(info)
            json.dump(json_data, f)
            f.close()

    def get_key(self, dictionary, item, fullname):
        for key, value in dictionary.items():
            if item.lower() in value:
                if key.__len__ != 0:
                    key = unicode.split(key, ', ')
                    numberofanswer = random.randrange(0, key.__len__())
                    return key[numberofanswer]
                else:
                    return key
        newitem = {item.lower(): fullname}
        self.writeinjson("testjson.json", newitem)
        self.writeinjson("NamesWithAction.json", {fullname: "needtosave"})
        return unicode("Я только обучаюсь, как бы ты сам ответил на это же сообщение? Ответ напиши в одном сообщении.: "
                       , 'utf-8')+item

    def compare_values(self, locator, fullname):
        foranswer = []
        values = self.get_text_from_element(locator)
        size = values.__len__()
        while size != 0:
            word = self.get_key(self.forsave("WordsAnswerDate.json"), values[size.__sub__(1)], fullname)
            foranswer.append(word)
            size -= 1
        return foranswer

    def name_add_with_action(self, filename, info):
        if self.check_name_in_dictionary(self.forsave(filename), info) is not True:
            self.writeinjson(filename, {info.encode('utf-8'): "needtoanswer"})
        else:
            pass

    @staticmethod
    def check_name_in_dictionary(dictionary, name):
        for key, value in dictionary.items():
            if name in key:
                return True

    @staticmethod
    def foo(name, fullname):
        for key, value in name.items():
            if fullname in value:
                if key.__len__ != 0:
                    key = unicode.split(key, ', ')
                    numberofanswer = random.randrange(0, key.__len__())
                    return key[numberofanswer]
                else:
                    return key

    @staticmethod
    def del_by_value(dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                del dictionary[key]
                return dictionary

    @staticmethod
    def writeinjson_without_save(filename, info):
        with open(filename, "w+") as f:
            json.dump(info, f)
            f.close()







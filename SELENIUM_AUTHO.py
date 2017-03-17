import json, codecs
import pickle


def forsave(file):
    with open(file, "r") as f:
        json_data = json.load(f)
        return json_data


def writeinJSON(file, info):
    json_data = forsave(file)
    with open(file, "w+") as f:
        json_data.update(info)
        json.dump(json_data, f, indent=0)

c = {"test":"das"}
writeinJSON("testjson.json", c)




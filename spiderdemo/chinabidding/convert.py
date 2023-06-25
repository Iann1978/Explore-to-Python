from urllib import parse
import json

# Read text file cloths.json and decode it to utf-8
def read_json_file():
    with open('spiderdemo/chinabidding/cloths.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        parse.decode(data)
        print(data)


read_json_file()
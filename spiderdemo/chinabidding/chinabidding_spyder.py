

from peewee import *

db = MySQLDatabase('test_peewee', user='root', password='123456', host='127.0.0.1', port=3306)
db.connect()

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

class Cloth(Model):
    tag = CharField()
    loc = CharField()
    title = CharField()

    class Meta:
        database = db # this model uses the "people.db" database


db.create_tables([Cloth, Person, Pet])




from urllib import request
import xpath
from bs4 import BeautifulSoup


url = 'http://www.chinabidding.cc/search/index.html?keyword=%E6%9C%8D%E8%A3%85&h_lx=0&date=90&search_field=0&vague=0&h_province=0&submit=+'

resp = request.urlopen(url)

html = resp.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')

li_elements = soup.select('#center_box .lists_center li')

for li in li_elements:
    tag = li.select('span')[0].text
    loc = li.select('span')[1].text
    title = li.select('a')[0].text
    print("hehe:", tag, loc, title)
    Cloth.create(tag=tag, loc=loc, title=title)
    # yield {
    #     "tag": li.select('span')[0].text,
    #     "loc": li.select('span')[1].text,
    #     "title": li.select('a')[0].text,
    # }



# print(resp.read().decode('utf-8'))



# from datetime import date
# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
# uncle_bob.save() # bob is now stored in the database
# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5))



# grandma1 = Person.select().where(Person.name == 'Grandma').get()
# print(grandma1.name)

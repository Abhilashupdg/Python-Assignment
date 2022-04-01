from abc import ABC, abstractclassmethod, abstractmethod
import logging

logging.basicConfig(filename='abs_class.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

class Person(ABC):

    @abstractmethod
    def get_gender(self):
        pass

class Male(Person):
    def get_gender(self):
        logging.info("Male")

class Female(Person):
    def get_gender(self):
        logging.info("Female")



male = Male()
male.get_gender()

female = Female()
female.get_gender()

person = Person()
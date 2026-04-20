from collections.abc import Iterable
import logging
logging.basicConfig(filename="list_module.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class ListMethods:
    def __init__(self,l):
        """
        Initializing list values
        """
        try:
            if type(l) == list:
                self.l=l
                logging.info(f"List object created with value: {l}")
            else:
                logging.error("Raising exception since list is not passed")
                raise Exception(f"You have not entered a list: {l}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def append_list(self,x):
        """
        This method will append element at the end of the list
        """
        try:
            self.l = self.l + [x]
            logging.info(f"List object appended with value: {x}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def clear_list(self):
        """
        This method will remove all items from list
        and make it empty list
        """
        try:
            self.l = []
            logging.info("List object cleared")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def copy_list(self):
        """
        This method will return a shallow copy of the list.
        """
        try:
            x = self.l[:]
            logging.info("Created shallow copy of the list")
            return x
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def count_list(self,x):
        """
        This method will return number of occurrences of parameter passed.
        """
        try:
            c=0
            for i in self.l:
                if x == i:
                    c += 1
            logging.info(f"number of occurrences of parameter {x} in the list: {c}")
            return c
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def extend_list(self,x):
        """
        This method will extend list by appending elements from the iterable.
        """
        try:
            if isinstance(x, Iterable):
                for i in x:
                    self.l = self.l + [i]
            else:
                self.l = self.l + [x]
            logging.info(f"List {self.l} is extended by parameter: {x}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def index_list(self, x):
        """
        This method will return the parameter first index
        """
        try:
            for i, j in enumerate(self.l):
                if x == j:
                    logging.info(f"Parameter: {x} found at position:{i} in the List {self.l}")
                    return i
            raise Exception(f"Parameter: {x} is not found in the list: {self.l}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def insert_list(self, i, x):
        """
        This method will insert object before index.
        """
        try:
            self.l = self.l[0:i] + [x] + self.l[i:]
            logging.info(f"Parameter: {x} inserted at index:{i} in the List {self.l}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def pop_list(self, i=-1):
        """
        This method will remove and return item at index
        If index is not given it will remove last and return.
        """
        try:
            x = self.l[i]
            if i == -1:
                self.l = self.l[0:-1]
            else:
                self.l = self.l[0:i] + self.l[i+1:]
            logging.info(f"Element: {x} removed from index:{i} in the List {self.l}")
            return x
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def remove_list(self, x):
        """
        This method will remove first occurrence of parameter.
        """
        try:
            c = self.index_list(x)
            if type(c) == int:
                x=self.pop_list(c)
                logging.info(f"Element: {x} removed from index:{i} in the List {self.l}")
            else:
                raise Exception(f"Parameter: {x} is not found in the list: {self.l}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def reverse_list(self):
        """
        This method will reverse the list.
        """
        try:
            self.l = self.l[::-1]
            logging.info("List is reversed")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def sort_list(self,rev=False):
        """
        This method will sort list in ascending order if rev parameter is False
        or sort list in descending order if rev parameter is True.
        """
        try:
            i = 0
            while (i < len(self.l) - 1):
                j = i + 1
                while (j < len(self.l) - 1):
                    if (self.l[i] > self.l[j]):
                        temp = self.l[i]
                        self.l[i] = self.l[j]
                        self.l[j] = temp
                    j = j + 1
                i = i + 1
            if rev:
                self.reverse_list()
                logging.info("List is sorted in ascending order ")
            else:
                logging.info("List is sorted in descending order ")
        except Exception as e:
            print(e)
            logging.exception(str(e))
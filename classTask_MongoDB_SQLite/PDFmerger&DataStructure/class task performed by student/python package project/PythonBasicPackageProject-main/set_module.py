import random
import logging
logging.basicConfig(filename="set_module.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class SetMethods:
    def __init__(self,s):
        """
        Initializing set values
        """
        try:
            if type(d) == set:
                self.s=s
                logging.info(f"Set object created with value: {s}")
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {s}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def add_set(self,x):
        """
        This method add an element to a set
        """
        try:
            l = list(self.s)
            l.append(x)
            self.s=set(l)
            logging.info(f"Element {x} is added to the Set")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def clear_set(self):
        """
        This method will remove all elements from this set
        """
        try:
            self.s = set()
            logging.info("set is now empty")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def copy_set(self):
        """
        This method will return a shallow copy of a set
        """
        try:
            logging.info("Returned a shallow copy of a set..")
            l = list(self.s)
            return set(l)
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def difference_set(self, set2):
        """
        This method will return the difference of two or more sets as a new set
        """
        try:
            if type(set2) == set:
                s1 = set()
                for i in self.s:
                    if i not in set2:
                        s1.add(i)
                logging.info(f"Difference of sets {self.s} and {set2}: {s1}")
                return s1
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def difference_update_set(self, set2):
        """
        This method will remove all elements of another set from this set.
        """
        try:
            if type(set2) == set:
                self.s=self.difference_set(set2)
                logging.info("Difference updates of sets is assigned to original set")
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def discard_set(self,x):
        """
        This method will Remove an element from a set if it is a member.
        If the element is not a member, do nothing.
        """
        try:
            if x in self.s:
                self.s = self.difference_set({x})
                logging.info(f"Discard element {x} from the sets")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def intersection_set(self,set2):
        """
        This method will return the intersection of two sets as a new set.
        """
        try:
            if type(set2) == set:
                s1 = set()
                for i in self.s:
                    if i in set2:
                        s1.add(i)
                logging.info(f"Intersection of sets {self.s} and {set2}: {s1}")
                return s1
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def intersection_update_set(self, set2):
        """
        This method will update a set with the intersection of itself
        """
        try:
            if type(set2) == set:
                self.s = self.intersection_set(set2)
                logging.info("Intersection updates of sets is assigned to original set")
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def isdisjoint_set(self, set2):
        """
        This method will return True if two sets have a null intersection.
        """
        try:
            if type(set2) == set:
                s = self.intersection_set(set2)
                logging.info(f"Checking if {self.s} and {set2} are disjoint or not")
                return False if s else True
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def issubset_set(self, set2):
        """
        This method will check whether another set contains this set
        """
        try:
            logging.info(f"Checking if {self.s} is a subset of {set2} or not")
            if type(set2) == set:
                flag = 0
                for i in self.s:
                    if i not in set2:
                        flag = 1
                return False if flag==1 else True
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def issuperset_set(self, set2):
        """
        This method will check whether this set contains another set.
        """
        try:
            logging.info(f"Checking if {self.s} is a superset of {set2} or not")
            if type(set2) == set:
                flag = 0
                for i in set2:
                    if i not in self.s:
                        flag = 1
                return False if flag==1 else True
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def pop_set(self):
        """
        This method will remove and return any random set element.
        Raises KeyError if the set is empty.
        """
        try:
            if self.s:
                l = list(self.s)
                r = random.randint(0,len(l)-1)
                x = l.pop(r)
                self.s = set(l)
                logging.info(f"Poping set element {x} from set")
                return x
            else:
                logging.error("Raising exception since set is empty")
                raise KeyError(f"Set: {self.s} is empty")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def remove_set(self, x):
        """
        This method will Remove an element from a set; it must be a member.
        If the element is not a member, raise a KeyError.
        """
        try:
            if x in self.s:
                l = list(self.s)
                l.remove(x)
                self.s = set(l)
                logging.info(f"Removed set element {x} from set")
            else:
                logging.error("Raising exception since set is empty")
                raise KeyError(f"Element: {x} is not present in set: {self.s}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def symmetric_difference_set(self,set2):
        """
        This method will Return the symmetric difference of two sets as a new set.
        (i.e. all elements that are in exactly one of the sets.)
        """
        try:
            logging.info(f"Creating symmetric_difference of sets: {self.s} and {set2}")
            if type(set2) == set:
                return self.s ^ set2
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def symmetric_difference_update_set(self,set2):
        """
        This method will Update a set with the symmetric difference of itself and another
        """
        try:
            logging.info("Creating symmetric_difference_update of 2 sets")
            if type(set2) == set:
                self.s = self.s ^ set2
            else:
                logging.error("Raising exception since set is not passed")
                raise Exception(f"You have not entered a set: {set2}")
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def union_set(self,*args):
        """
        This method will Return the union of sets as a new set.
        (i.e. all elements that are in either set.)
        """
        try:
            u = self.copy_set()
            for x in args:
                if type(x) != set:
                    logging.error("Raising exception since set is not passed")
                    raise Exception(f"You have not entered a set: {x}")
                    return
                u = u | x
            logging.info(f"Creating union of sets: {u}")
            return u
        except Exception as e:
            print(e)
            logging.exception(str(e))

    def update_set(self,*args):
        """
        This method will Update a set with the union of itself and others.
        """
        try:
            logging.info(f"Creating update of  sets..")
            self.s = self.union_set(*args)
        except Exception as e:
            print(e)
            logging.exception(str(e))
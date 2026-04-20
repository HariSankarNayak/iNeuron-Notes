import logging
class set_func:
    logging.basicConfig(filename="set_logger.log", level= logging.INFO, format='%(asctime)s \t %(levelname)s \t %(message)s')
    
    def __init__(self,s):
        try:
            if type(s) == set:
                self.s = s
                logging.info(f"Valid set is entered: {self.s}")
            else:
                raise Exception("Not a valid set, please enter set")
        except Exception as e:
            logging.warning("Warning, problem occured")
            logging.exception(f"Error occurred: {e}")
    
    def set_appender(self, value):
        """Returns the new set after adding the passed value to the set"""
        l=[""]
        logging.info(f"Method set_appender called. Adding {value} to the set")
        a = list(self.s)
        a = a + l
        a[len(a)-1] = value
        self.s = set(a)
        logging.info(f"New set: {self.s}")
        return self.s
        
    def clear_set(self):
        """Returns the set after clearing every element i.e. returns null set"""
        logging.info("Method clear_set called")
        self.s= set()
        logging.warning("Set cleared")
        return self.s
    
    def set_copy(self):
        """Returns the copy of the set"""
        logging.info("Method clear_set called")  
        return self.s
    
    def set_differ(self, s3):
        """Returns the differnce of two sets as a new set.
        i.e Returns the set with the elements which are in this set but not in other"""
        logging.info("Method set_differ called")
        a = list(self.s)
        b = list(s3)
        l=[]
        le = 0
        for i in range(0,len(a)):
            for j in range(0, len(b)):
                if a[i] == b[j]:
                    l.append(a[i])                  
        while le < len(l):
            a.remove(l[le])
            le +=1
        logging.info(f"Difference set: {set(a)}")
        return set(a)
    
    def set_differ_update(self, s3):
        """Removes those elements in this set which are in other set"""
        logging.info("Method clear_set called")
        a = list(self.s)
        b = list(s3)
        l=[]
        le = 0
        for i in range(0,len(a)):
            for j in range(0, len(b)):
                if a[i] == b[j]:
                    l.append(a[i])                  
        while le < len(l):
            a.remove(l[le])
            le +=1
        self.s=set(a)
        logging.info(f"Updated set: {self.s}")
        return self.s
        
    def set_intersection(self, s3):
        """Returns the intersection of two sets as a new set
        i.e Returns the set with elements which are common in both the set"""
        logging.info("Method set_intersection called")
        l=[]
        for i in self.s:
            for j in s3:
                if i == j:
                    l.append(i)                  
        logging.info(f"Intersection is {set(l)}")
        return set(l)
    
    def set_intersection_update(self, s3):
        """Updates the current set with the are common in both the sets"""
        logging.info("Method set_intersection_update called")
        l=[]
        for i in self.s:
            for j in s3:
                if i == j:
                    l.append(i)                  
        self.s=set(l)
        logging.info(f"Updated set of intersection: {self.s}")
        return self.s
    
    def set_discard(self, value):
        """Removes the element passed from the given set if it is a member.
        If element is not a member then it returns nothing"""
        logging.info("Method set_discard called")
        logging.warning(f"Discarding: {value} from the set")
        a = list(self.s)
        for i in a:
            if i == value:
                a.remove(value)
                self.s=set(a)
                return self.s
                break
    
    def set_remove(self, value):
        """Removes the element passed from the given set if it is a member.
        If element is not a member then it raises Key Error"""
        logging.info("Method set_remove called")
        logging.warning(f"Removing: {value} from the set")
        try:
            a = list(self.s)
            for i in a:
                if i == value:
                    a.remove(value)
                    self.s=set(a)
                    return self.s
                    break
            else:
                raise KeyError("Key Error Occurred : Value not present")
        except KeyError as e:
            logging.warning("Warning problem occured")
            logging.exception(f"Error occurred: {e}")
            
    def set_union(self, s3):
        """Returns the union of two sets as a new set.
        i.e. Elements that are present either set"""
        logging.info("Method set_union called")
        logging.info(f"Creating union of current set and {s3}")
        try:
            a = list(self.s)
            b = list(s3)
            a.extend(b)
            logging.info(f"Union set:{set(a)}")
            return set(a)
        except Exception as e:
            logging.warning("Warning problem occured")
            logging.exception(f"Error occurred: {e}")
    
    def set_updater(self, s3):
        """Update a set with the union of itself and others."""
        logging.info("Method set_updater called")
        logging.warning(f"Updating current set with union of current set and {s3}")
        try:
            a = list(self.s)
            b = list(s3)
            a.extend(b)
            self.s = set(a)
            logging.info(f"Updated set:{self.s}")
            return self.s
        except Exception as e:
            logging.warning("Warning problem occured")
            logging.exception(f"Error occurred: {e}")
            
    def set_symm_diff(self, s3):
        """Return the symmetric difference of two sets as a new set.
    (i.e. all elements that are in exactly one of the sets.)."""
        logging.info("Method set_symm_diff called")
        try:
            a = list(self.set_union(s3))
            b = list(self.set_intersection(s3))
            for i in b:
                    a.remove(i)
            logging.info(f"Symmetric Difference set:{set(a)}")
            return set(a)  
        except Exception as e:
            logging.warning("Warning problem occured")
            logging.exception(f"Error occurred: {e}")
            
    def set_symm_diff_update(self, s3):
        """Update a set with the symmetric difference of itself and another."""
        logging.info("Method set_symm_diff_update called")
        try:
            a = list(self.set_union(s3))
            b = list(self.set_intersection(s3))
            for i in b:
                    a.remove(i)
            self.s = set(a)
            logging.info(f"Updated set:{self.s}")
            return self.s 
        except Exception as e:
            logging.warning("Warning problem occured")
            logging.exception(f"Error occurred: {e}")
    
    def set_isDisjoint(self, s3):
        """Returns True if their intersection set is a null set
        i.e. Both the sets have unique elements"""
        logging.info("Method set_isDisjoint called")
        a = self.set_intersection(s3)
        if a == set():
            return True
        else:
            return False
    
    def set_isSubset(self, s3):
        """Returns True if another set contains this set"""
        logging.info("Method set_isSubset called")
        a = self.set_intersection(s3)
        if len(a) == len(self.s):
            return True
        else:
            return False
    
    def set_isSuperset(self, s3):
        """Returns True if this set contains other set"""
        logging.info("Method set_isSuperset called")
        a = self.set_intersection(s3)
        b = self.set_differ(s3)
        if a != set() and len(a) == len(s3) and b != set():
            return True
        else:
            return False
        
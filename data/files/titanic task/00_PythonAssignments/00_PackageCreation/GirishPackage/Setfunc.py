# Write a class for the set, including all possible subfunctions for set

import logging

class MySet1:
    def __init__(self, set1):
        logging.basicConfig(filename="LoggingInformation_Set.log", level=logging.DEBUG)
        logging.basicConfig(filename="LoggingInformation_Set.log", level=logging.INFO)
        logging.basicConfig(filename="LoggingInformation_Set.log", level=logging.WARNING)
        logging.basicConfig(filename="LoggingInformation_Set.log", level=logging.ERROR)

        if (type(set1) == set):
            self.s1 = set1
        else:
            raise Exception("Given input argument is NOT type of 'Set'")

    def check_type(self, s2):
        if (type(s2) != set):
            raise Exception("Given input argument is NOT type of 'Set'")

    def Add_Value(self, val):
        '''
        Function to add the value to given set
        '''
        try:
            # self.s1[len(self.s1)] = val, .... item assingment not allowed
            l = list(self.s1)
            l.append(val)
            self.s1 = set(l)
            return self.s1

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Clear_Set(self):
        '''
        Function to clear the set
        '''
        try:
            self.s1 = {}
            return self.s1
        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Copy_Set(self):
        '''
        Function to copy set
        '''
        try:
            return self.s1
        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def find_set_diff(self, s2):
        '''
        local function to find the differences in the given two sets
        '''
        l1 = []
        for i in self.s1:
            flag_Found = False
            for j in s2:
                if (j == i):
                    flag_Found = True
                    break
                else:
                    flag_Found = False

            if (flag_Found == False):
                l1.append(i)

        return set(l1)

    def Diff(self, s2):
        '''
        Function to find the difference between given two sets
        '''
        try:
            self.check_type(s2)

            diff = self.find_set_diff(s2)

            return diff
        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Diff_Update(self, s2):
        '''
        Function to find the difference between given two sets & update it in initialized setd
        '''
        try:
            self.check_type(s2)

            self.s1 = self.find_set_diff(s2)

            return self.s1

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Discard_Val(self, val):
        '''
        Function to discard one value from set
        '''
        try:
            l1 = list(self.s1)
            new_list = []
            for i in l1:
                if (val == i):
                    pass
                else:
                    new_list.append(i)

            if (len(new_list) != 0):
                self.s1 = set(new_list)
            else:
                logging.info("Given Value is not present in the set, No operations done")
                pass

            return self.s1

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def find_intersection(self, s2):
        '''
        local function to find the intersection between two sets
        '''
        try:
            l1 = []
            for i in self.s1:
                flag_Found = False
                for j in s2:
                    if (j == i):
                        l1.append(i)
                        break

            return set(l1)

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Intersect(self, s2):
        '''
        Function to find the intersection between two sets
        '''
        try:
            self.check_type(s2)

            # find the intersection
            intersection_val = self.find_intersection(s2)

            return intersection_val

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Intersect_Update(self, s2):
        '''
        Function to find the intersection between two sets & update in the initialized set
        '''
        try:
            self.check_type(s2)

            # find the intersection
            self.s1 = self.find_intersection(s2)

            return self.s1

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Is_Disjoint(self, s2):
        '''
        Function to find if the given sets are disjoint or not
        '''
        try:
            self.check_type(s2)

            flag_disjoint = False
            for i in self.s1:
                for j in s2:
                    if (j == i):
                        flag_disjoint = True
                        break
                if (flag_disjoint == True):
                    break

            if (flag_disjoint == True):
                return False
            else:
                return True

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Is_Subset(self, s2):
        '''
        Function to find if the given set is Subset of initialized set
        '''
        try:
            self.check_type(s2)

            for i in self.s1:
                flag_subset = False
                for j in s2:
                    if (j == i):
                        flag_subset = True
                        break

                if (flag_subset != True):
                    break

            return flag_subset

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Is_Superset(self, s2):
        '''
        Function to find if the given set is Superset of initialized set
        '''
        try:
            self.check_type(s2)

            for i in s2:
                flag_superset = False
                for j in self.s1:
                    if (j == i):
                        flag_superset = True
                        break

                if (flag_superset != True):
                    break

            return flag_superset

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Pop_From_Set(self):
        '''
        Function to pop first value from initialized set
        '''
        try:
            l1 = list(self.s1)
            return (l1[0])

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Remove_From_Set(self, val):
        '''
        Function to remove first value from initialized set
        '''
        try:
            l1 = list(self.s1)
            new_list = []

            for i in l1:
                if (val == i):
                    pass
                else:
                    new_list.append(i)

            self.s1 = set(new_list)
            return self.s1

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def find_symm_diff(self, s2):
        '''
        local function to find the symmetric difference betweeninitialized & given set
        '''
        try:
            l1 = []

            if (len(self.s1) > len(s2)):
                set1 = self.s1
                set2 = s2
            else:
                set1 = s2
                set2 = self.s1

            for i in set1:
                flag_val_not_found = False
                for j in set2:
                    if (j == i):
                        flag_val_not_found = True

                if (flag_val_not_found == False):
                    l1.append(i)

            return set(l1)

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Symm_Diff(self, s2):
        '''
        Function to find the symmetric difference between given sets
        '''
        try:
            self.check_type(s2)

            # find the symmtric difference
            symm_diff_val = self.find_symm_diff(s2)

            return symm_diff_val

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Symm_Diff_Update(self, s2):
        '''
        Function to find the symmetric difference between given sets & update it in initialized set
        '''
        try:
            self.check_type(s2)

            # find the symmtric difference
            self.s1 = self.find_symm_diff(s2)

            return self.s1

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Do_Union(self, s2):
        '''
        Function to perform a union operation on given sets
        '''
        try:
            self.check_type(s2)

            final_set = set(list(self.s1) + list(s2))
            return final_set

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def Do_Update(self, s2):
        '''
        Function to update initialized set with given 'list' or 'set' or 'dictionary'
        Note: In case of dictionary, only 'key' values will be updated to initialized set
        '''
        try:
            l1 = []
            l1 = list(self.s1)

            if (type(s2) == set):
                l2 = list(s2)
                l1 = l1 + l2

            elif (type(s2) == list):
                l1 = l1 + s2

            elif (type(s2) == dict):
                l2 = list(s2.keys())
                l1 = l1 + l2

            else:
                raise Exception("Given input is not correct, Please enter input of type 'List', 'Set' or 'Dict'")

            self.s1 = set(l1)
            return self.s1

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

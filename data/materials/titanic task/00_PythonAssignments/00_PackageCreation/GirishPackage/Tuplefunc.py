# Write a class for the tuple, including all possible subfunctions for tuple

import logging

class MyTuple1:
    def __init__(self, tp1):
        logging.basicConfig(filename="LoggingInformation_Tuple.log", level=logging.DEBUG)
        logging.basicConfig(filename="LoggingInformation_Tuple.log", level=logging.INFO)
        logging.basicConfig(filename="LoggingInformation_Tuple.log", level=logging.WARNING)
        logging.basicConfig(filename="LoggingInformation_Tuple.log", level=logging.ERROR)

        self.tp = tp1

    def CountValue(self, val):
        try:
            FoundCount = 0
            for i in self.tp:
                if (val == i):
                    FoundCount = FoundCount + 1
            return FoundCount

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)

    def FindIndex(self, val):
        try:
            FoundIndex = -1;  # Assuming -1 as INVALID value
            for i in range(0, len(self.tp)):
                if (val == self.tp[i]):
                    FoundIndex = i
                    break

            if (FoundIndex == -1):
                err_str = val, "NOT Available in the given tuple"
                logging.info(err_str)

            return FoundIndex

        except Exception as e:
            err_str = "Exception Occured : " + str(e)
            logging.exception(err_str)
            logging.shutdown()
            raise Exception(err_str)


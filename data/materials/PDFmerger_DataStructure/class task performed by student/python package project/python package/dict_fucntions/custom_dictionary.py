import logging


class CustomDictFunctions():
	"""docstring for ClassName"""
	def __init__(self,d):
		self.d=d
		self.l=[]
		
		

	def startLogger(self,file_name):
		"""This fucntion starts the log into text file"""
		if type(file_name)==str:
			if 'txt' in file_name:
				logging.basicConfig(filename=file_name,level=logging.DEBUG,format ='%(asctime)s %(levelname)s %(message)s')
				logging.info("File created for dictionary operations")
			else:
				try:
					raise Exception("File Exception")
				except Exception as e:
					logging.basicConfig(filename="dict_log_error.txt",level=logging.DEBUG,format ='%(asctime)s %(levelname)s %(message)s' )
					logging.error("Wrong file name sent")
					return "Exception raised due to {} Please pass txt only".format(e)
		else:
			print("Pass file name in strings")
				


	def getKeys(self):
		"""This functions is used to append data to list"""
		try:
			if type(self.d)==dict:
				logging.info("keys returned successfully")
				for k in self.d:
					self.l.append(k)
				return "keys are",self.l
			else :
				raise Exception("Wrong Type")
		except Exception as e:
			
			logging.error("Exception raised")
			logging.warning("Warn displayed about wrong type passed ")
			return "Exception raised due to {} Please pass txt only".format(e)

	def getValues(self):
		"""This functions is used to reverse data in list"""
		try:
			if type(self.d)==dict:
				logging.info("Values returned successfully")
				for k in self.d:
					self.l.append(self.d[k])
				return "values are",self.l
			else :
				raise Exception("Wrong Type")
		except Exception as e:
			
			logging.error("Exception raised")
			logging.warning("Warn displayed about wrong type passed ")
			return "Exception raised due to {} Please pass txt only".format(e)

	
		
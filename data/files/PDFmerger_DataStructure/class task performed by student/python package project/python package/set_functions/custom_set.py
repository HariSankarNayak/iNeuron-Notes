import logging


class CustomSetFunctions():
	"""docstring for ClassName"""
	def __init__(self,s):
		self.s=s
		

	def startLogger(self,file_name):
		"""This fucntion starts the log into text file"""
		try:
			if type(file_name)==str:
				if 'txt' in file_name:
					logging.basicConfig(filename=file_name,level=logging.DEBUG,format ='%(asctime)s %(levelname)s %(message)s')
					logging.info("File created for tuple operations")
				else:
					try:
						raise Exception("File Exception")
					except Exception as e:
						logging.basicConfig(filename="dict_log_error.txt",level=logging.DEBUG,format ='%(asctime)s %(levelname)s %(message)s' )
						logging.error("Wrong file name sent")
						error="Exception raised due to" +e+" Please pass txt only"
						return error
			else:
				raise NameError("Pass file name in strings")
				print("Pass file name in strings")
		except NameError as ne:
			return "Exception raised due to {} Please pass list only".format(ne)
				


	def custom_discard(self,value):
		"""This functions is used to append data to list"""
		try:
			if type(self.s)==set:
				if type(value)==int:
					self.s.discard(value)
					logging.info("discard of value successfull")
					logging.info("returning set")
					return self.s
				else:
					raise TypeError("Wrong value type")
					
			else :
				raise ValueError("Wrong Type")
		except ValueError as e:
			
			logging.error("Exception raised")
			logging.warning("Warn displayed about wrong type passed ")
			return "Exception raised due to {} Please pass list only".format(e)
		except TypeError as te:
			logging.error("Exception raised")
			logging.warning("Warn displayed about collection passed ")
			return "Exception raised due to {} Please pass list only".format(te)


	


	
		
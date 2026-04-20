import logging


class CustomTupleFunctions():
	"""docstring for ClassName"""
	def __init__(self,t):
		self.t=t
		self.l=[]
		
		

	def startLogger(self,file_name):
		"""This fucntion starts the log into text file"""
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
					return "Exception raised due to {} Please pass txt only".format(e)
		else:
			print("Pass file name in strings")
				


	def getCount(self,value):
		"""This functions is used to append data to list"""
		try:
			if type(self.t)==tuple:
				#self.tuple_list=list(self.t)
				self.repeated_list=[]
				
				for i in self.t:
					if i not in self.repeated_list:
						self.repeated_list.append(i)
				return "duplicated values are",len(self.repeated_list)
				logging.info("returning count of value in a tuple")
			else :
				raise Exception("Wrong Type")
		except Exception as e:
			
			logging.error("Exception raised")
			logging.warning("Warn displayed about wrong type passed ")
			return "Exception raised due to {} Please pass txt only".format(e)

	


	
		
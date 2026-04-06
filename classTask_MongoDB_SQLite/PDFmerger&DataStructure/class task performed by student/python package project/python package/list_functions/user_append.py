import logging

class CustomListFunctions(object):
	"""docstring for ClassName"""
	def __init__(self,l):
		self.l=l
		

	def startLogger(self,file_name):
		"""This fucntion starts the log into text file"""
		if type(file_name)==str:
			if 'txt' in file_name:
				logging.basicConfig(filename=file_name,level=logging.DEBUG,format ='%(asctime)s %(levelname)s %(message)s')
				logging.info("File created")
			else:
				try:
					raise Exception("File Exception")
				except Exception as e:
					logging.basicConfig(filename="list_log_erro.txt",level=logging.DEBUG,format ='%(asctime)s %(levelname)s %(message)s' )
					logging.error("Wrong file name sent")
					error="Exception raised due to" +e+" Please pass txt only"
					return error
		else:
			print("Pass file name in strings")
				


	def append(self,value):
		"""This functions is used to append data to list"""
		try:
			if type(self.l)==list:
				self.l.append(value)
				logging.info("appended successfully")
				return self.l
			else :
				raise Exception("Wrong Type")
		except Exception as e:
			error="Exception raised due to" +e+" Please pass list only"
			logging.error("Exception raised")
			logging.warning("Warn displayed about wrong type passed ")
			return error

	def reverse_list(self):
		"""This functions is used to reverse data in list"""
		try:
			if type(self.l)==list:
				logging.info("reversing list successfully")
				return self.l[::-1]
			else :
				raise Exception("Wrong Type")
		except Exception as e:
			error="Exception raised due to" +e+" Please pass list only"
			logging.error("Exception raised")
			logging.warning("Warn displayed about wrong type passed ")
			return error


	def pop_list(self):
		"""This functions is used to pop one element from list"""
		try:
			if type(self.l)==list:
				logging.info("poping from list successfully")
				temp_list=self.l
				temp_num=temp_list.pop()
				temp_pop_index=self.l.index(temp_num)
				return "Using pop the removed element is "+self.l[temp_pop_index]
			else :
				raise Exception("Wrong Type")
		except Exception as e:
			error="Exception raised due to" +e+" Please pass list only"
			logging.error("Exception raised")
			logging.warning("Warn displayed about wrong type passed ")
			return error

		
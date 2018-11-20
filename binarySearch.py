#class to create a binary Search algorithim
class binarySearch(object):
	"""docstring for BinarySearch algorithim
	create a class defining """
	def __init__(self, arg,interval):
		self.arg = arg
		self.toTwenty=[]
		self.toForty=[]
		self.toOneThousand=[]
		self.bottom=0
		self.count=0
		self.median=0
		
		if interval==1:
			self.small_list_search()
		elif interval==2:
			self.medium_list_search()
		elif interval==10:
			self.large_list_search()
		self.dicto={'count':self.count,'length':len(self.listin),'index':self.median}
		self.binarysearch()
	def small_list_search(self):
		for i in range(1,21):
			self.toTwenty.append(i)
		self.listin=self.toTwenty
		return self.toTwenty
	def medium_list_search(self):
		for i in range(2,42,2):
			self.toForty.append(i)
		self.listin=self.toForty
		return self.toForty
	def large_list_search(self):
		for x in range(10,1010,10):
			self.toOneThousand.append(x)
		self.listin=self.toOneThousand
		return self.toOneThousand
	def binarysearch(self):
		self.length=len(self.listin)
		self.top=self.length-1
		self.median=0
		while self.bottom<=self.top:
			self.count+=1
			self.median=(self.top+self.bottom)/2
			if self.median==self.top-0.5:
				self.median=self.top
				break
			if self.median== 0.5:
				self.median=0
				break
			else:
				self.median=int(self.median)
				if self.arg==self.toTwenty[self.median]:
					break
				elif self.arg<self.toTwenty[self.median]:
					self.top=self.median
				elif self.arg>self.toTwenty[self.median]:
					self.bottom=self.median
		self.dicto={'count':self.count,'length':len(self.listin),'index':self.median}
		return self.dicto
# if __name__ == '__main__':
help=binarySearch(16,1)
print(help.binarysearch())
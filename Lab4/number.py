class Integer(object) :
	def __init__(self, number, negative):
		self.num=number
		self.negative=negative

	def display(self):
		if self.negative == "negative"
			print "-" + str(self.num)
		else:
			print "+" + str(self.num)
class NegativeInteger(object) :
	def __list__(self, number):
		super(NegativeInteger, self).__init__(number, "negative")
	def display(self):
		Integer.display(self)
		print "This is an object of the NegativeIntege class"


if __name__=="__main__":
	test1 = Integer (90, "positive")
	test2 = NegativeInteger (70)
	list1 = [ test1, test2 ]
	for x in list1 :
		x.display()
	


	test.display()
	test.display()

	print 


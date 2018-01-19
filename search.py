import sys
import baseMethods


class Search:

	baseMethod =  baseMethods.BaseMethods()

	def __init__(self):
		pass

	def main(self):

		temp = self.baseMethod.genImg()
		if temp:
			sys.exit(0)
		else:
			if self.baseMethod.img2Tz(1):
				print ('Conversion Error')
				sys.exit(0)
			r = self.baseMethod.search()
			if r[0] == 0:
				print("success")
				return [r[1]+r[2]]
			else:
				print("failure")
				return [123456]

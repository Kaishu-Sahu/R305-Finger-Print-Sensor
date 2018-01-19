import time,sys
import baseMethods


class Enroll:

	baseMethod =  baseMethods.BaseMethods()

	def __init__(self):
		pass

	def main(self,mode):
		#mode = 1 for nomal user
		#mode = 2 for authorizer
		if self.baseMethod.verifyFinger():
			print ('Verification Error')
			sys.exit(0)

		self.body2()

		resultRegModel = self.baseMethod.regModel()
		if resultRegModel == 10:
			print('Fingers do not belong to one person')
			self.body2()
		elif resultRegModel == 1:
			print('Internal Error')
			sys.exit(0)

		pg = 1
		id = 1
		if self.baseMethod.store(pg,id):
			print('Store Error')
			sys.exit(0)

		if mode == 1:
			print ("Enrolled successfully at id %d"%id)
		elif mode == 2:
			try:
				fp = open('records.txt','a')
				fp.write(str(pg)+","+str(id)+"\n")
			finally:
				fp.close()
			print("Authorizer Enrolled successfully at id %d"%id)
		else:
			print("Internal Error")


	def body(self,comment):
		print(comment)
		sys.stdout.flush()

		time.sleep(1)
		timeStamp = time.time()

		while self.baseMethod.genImg():
			if (time.time()-timeStamp) <= 120:
				time.sleep(0.1)
				print ('.'),
				sys.stdout.flush()
			else:
				break

		print('Processing')
		sys.stdout.flush()

	def body2(self):
		self.body("Put Finger")

		if self.baseMethod.img2Tz(1):
			print ('Conversion Error')
			self.body("Put Finger Again")

		self.body("Put Finger Again")

		if self.baseMethod.img2Tz(2):
			print ('Conversion Error')
			self.body("Put Finger Again")

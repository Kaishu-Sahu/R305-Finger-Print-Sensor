import enroll,search,time


class RegisterUser:

	srh = search.Search()
	enr = enroll.Enroll()

	def __init__(self):
		pass

	def main(self):
		b = False
		timeStamp = time.time()
		while (time.time()-timeStamp) <= 120:
			a = self.srh.main()
			if a[0] != 123456:
				try:
					fp = open('file.txt','r')
					for line in fp:
						arg1, arg2 = line.split(',')
						if arg1 == a[1] and arg2 == (a[2]+"\n"):
							b = True
							break
						else:
							b = False
				finally:
					fp.close()
				break
			else:
				pass

		if b:
			self.enr.main(1)

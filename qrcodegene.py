import qrcode
class Qrcode:
	def __init__(self,data):
		self.data = data
	def qr_make(self):
		qr = qrcode
		try:
					qr.make(self.data)
					qr.make("qrdemo.png")
					print("Qr code generated Successfully")
			
		except ValueError:
			print("Enter Wr data first")
		
data=input("Enter Qr data")
QR = Qrcode(data)
QR.qr_make()

			
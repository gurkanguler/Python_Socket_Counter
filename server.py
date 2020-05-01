import socket
import platform
import os



class Server:
	def __init__(self):
		os.system("color a")
		print('''
				GURKAN GULER \n
			''')
		print("Waiting....")
		self.count = 0
		while True:
			with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as self.sock:
				self.host = "127.0.0.1"
				self.port = 4444
				self.sock.bind((self.host,self.port))
				self.sock.listen()
				self.conn,self.addr = self.sock.accept()
			
				with self.conn:
					print("Connected Client",self.addr)
					self.count += 1
					print(self.count)
					while True:
						self.data = self.conn.recv(1024)
						if not self.data:
							break
						self.conn.send(self.data)


				
if __name__ == '__main__':
	Server = Server()
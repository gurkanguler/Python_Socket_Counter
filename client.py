import socket


class Client:
	def __init__(self):
		self.host = "127.0.0.1"
		self.port = 4444
		with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as self.sock:
			self.sock.connect((self.host,self.port))
			self.sock.sendall(b"Hello")
			self.data = self.sock.recv(1024)

		print(repr(self.data))



if __name__ == '__main__':
	Client = Client()
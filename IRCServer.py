import socket

class IRCServer(object):
	"""docstring for IRCServer"""
	def __init__(self, host, port):
		self.nicks = {}
		self.host = host
		self.port = port

	def runner(self):
		server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen()

    def handle_client(self, client_socket):
    	"""handle client method"""
    	data = client_socket.recv(1024).decode()

    def handle_login(self, client_socket, nick="default"):
    	"""handle login method"""
    	self.nicks[client_socket] = nick

    def handle_message(self, client_socket, message):
    	"""handle message method"""
    	return

    def send_message(self, message):
    	"""send message method"""
    	return

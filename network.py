import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '52.90.157.227'
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()

# will be not using getP
    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)

        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
# will not be using only_send
    def only_send(self,data):


            try:
                self.client.send(pickle.dumps(data))
                return self.p
            except socket.error as e:
                print(e)


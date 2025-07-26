import threading
import time

class ProcessoLamport(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.L = 0

    def evento_interno(self):
        self.L += 1
        print(f"[P{self.id}] Evento interno | L = {self.L}")

    def enviar(self, outro):
        self.L += 1
        print(f"[P{self.id}] Enviando para P{outro.id} | L = {self.L}")
        outro.receber(self.L)

    def receber(self, valor):
        self.L = max(self.L, valor) + 1
        print(f"[P{self.id}] Recebeu mensagem | L = {self.L}")

    def run(self):
        self.evento_interno()
        time.sleep(0.5)
        self.evento_interno()

if __name__ == "__main__":
    p1 = ProcessoLamport(1)
    p2 = ProcessoLamport(2)

    p1.start()
    p2.start()
    time.sleep(1)

    p1.enviar(p2)
    p2.enviar(p1)

    p1.join()
    p2.join()

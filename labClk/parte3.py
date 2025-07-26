import threading
import time
from copy import deepcopy

class ProcessoVetorial(threading.Thread):
    def __init__(self, id, n_processos):
        super().__init__()
        self.id = id
        self.n = n_processos
        self.V = [0] * n_processos

    def evento_interno(self):
        self.V[self.id] += 1
        print(f"[P{self.id}] Evento interno | V = {self.V}")

    def enviar(self, outro):
        self.V[self.id] += 1
        print(f"[P{self.id}] Enviando para P{outro.id} | V = {self.V}")
        outro.receber(deepcopy(self.V))

    def receber(self, vetor_recebido):
        for i in range(self.n):
            self.V[i] = max(self.V[i], vetor_recebido[i])
        self.V[self.id] += 1
        print(f"[P{self.id}] Recebeu mensagem | V = {self.V}")

    def run(self):
        self.evento_interno()
        time.sleep(0.4)
        self.evento_interno()

if __name__ == "__main__":
    p0 = ProcessoVetorial(0, 3)
    p1 = ProcessoVetorial(1, 3)
    p2 = ProcessoVetorial(2, 3)

    p0.start()
    p1.start()
    p2.start()

    time.sleep(1)

    p0.enviar(p1)
    time.sleep(0.2)
    p1.enviar(p2)

    p0.join()
    p1.join()
    p2.join()

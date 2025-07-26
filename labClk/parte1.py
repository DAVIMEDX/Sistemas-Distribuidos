import threading
import time

class ProcessoFisico(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        for i in range(5):
            timestamp = time.time() * 1000 #ms
            print(f"[P{self.id}] Evento {i} | Tempo físico: {timestamp:.0f} ms")
            time.sleep(0.2 + self.id * 0.1)  # simula atraso diferente por processo

# Executar
if __name__ == "__main__":
    processos = [ProcessoFisico(i) for i in range(3)]
    for p in processos:
        p.start()
    for p in processos:
        p.join()

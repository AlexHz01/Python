import threading
import time


class Hilo(threading.Thread):
    def run(self):
        print("{} Iniciado".format(self.getName()))
        time.sleep(1)
        print("{} Finalizado".format(self.getName()))


if __name__ == "__main__":
    for x in range(4):
        hilo = Hilo(name="Hilo {}".format(x + 1))
        hilo.start()
        time.sleep(.5)

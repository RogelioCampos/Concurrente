import time
import random
import threading

N = 5
TIEMPO_TOTAL = 3

class filosofo(threading.Thread):
    semaforo = threading.RLock()
    estado = []
    tenedores = []
    count=0

    def __init__(self):
        super().__init__()
        self.id=filosofo.count
        filosofo.count+=1
        filosofo.estado.append('PENSANDO')
        filosofo.tenedores.append(threading.Semaphore(0))
        print("FILOSOFO {0} - PENSANDO".format(self.id))

    def __del__(self):
        print("FILOSOFO {0} - Se para de la mesa".format(self.id))

    def derecha(self,i):
        return (i-1)%N

    def izquierda(self,i):
        return(i+1)%N

    def verificar(self,i):
        if filosofo.estado[i] == 'HAMBRIENTO' and filosofo.estado[self.izquierda(i)] != 'COMIENDO' and filosofo.estado[self.derecha(i)] != 'COMIENDO':
            filosofo.estado[i]='COMIENDO'
            filosofo.tenedores[i].release()

    def run(self):
        muerto = False
        for i in range(TIEMPO_TOTAL):
            intentos = 0
            time.sleep(random.randint(0,5))
            filosofo.estado[self.id] = 'HAMBRIENTO'
            print("FILOSOFO {} HAMBRIENTO ".format(self.id)) 
            while (not filosofo.semaforo.acquire()):
                intentos += 1
                print("FILOSOFO", self.id, "HA INTENTADO COMER", intentos, "VECES")
                if intentos >= 10:
                    muerto = True
                    break
                time.sleep(random.randint(0,2))
            if muerto:
                print("FILOSOFO", self.id, "HA MUERTO")
                break
            else:
                self.verificar(self.id)
                filosofo.semaforo.release()
                filosofo.tenedores[self.id].acquire()
                print("FILOSOFO {} COMIENDO ".format(self.id))
                time.sleep(2)
                print("FILOSOFO {} TERMINO DE COMER ".format(self.id))
                filosofo.semaforo.acquire()
                filosofo.estado[self.id] = 'PENSANDO'
                self.verificar(self.izquierda(self.id))
                self.verificar(self.derecha(self.id))
                filosofo.semaforo.release()

def main():
    lista=[]
    for i in range(N):
        lista.append(filosofo()

    for f in lista:
        f.start()

    for f in lista:
        f.join()

if __name__=="__main__":
    main()

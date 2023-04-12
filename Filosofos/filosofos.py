import sys
import threading
import time

class Semaphore(object):

    def __init__(self, initial):
        #funcion de inicio
    #el self acede a los atributos y metodos de la clase
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self): #funcion que levanta el tenedor
        with self.lock:
            self.value +=1
            self.lock.notify()

    def down(self):   #funcion que deja el tenedor
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -=1

class Chopstick(object):

    def __init__(self, number):
        self.number =number    #id del tenedor
        self.user =1          #lleva el rastreo del filosofo
        self.lock = threading.Condition(threading.Lock())
        self.taken = False 
    
    def take(self, user):          #funcion de tomar el tenedor
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write("Filosofo[%s] toma el tenedor:%s\n" %   
                            (user, self.number))  #imprime en la pantalla
            self.lock.notify_all()


    def drop(self, user):      #funcion de dejar el tenedor
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write("filosofo[%s] deja el tenedor:%s\n" % 
                            (user, self.number))
            self.lock.notify_all()


class Philosopher(threading.Thread):      #clase filosofo por medio de hilos
        
    def __init__(self, number, left, right, butler):
        threading.Thread.__init__(self)
        self.number = number           #numero de filosofo
        self.left = left
        self.right = right
        self.butler = butler

    def run(self):
        for i in range(1):
            self.butler.down()                               #empieza el servicio
            print("filosofo", self.number, "esta pensando")
            time.sleep(0.1)                                  #piensa
            self.left.take(self.number)                      #recoge el tenedor izquierdo  
            time.sleep(0.1)
            self.right.take(self.number)                     #recoge el tenedor derecho  
            print("filosofo", self.number, " esta comiendo")
            time.sleep(0.1)                                    #come
            self.right.drop(self.number)                       #deja el tenedor derecho
            self.left.drop(self.number)                        #deja el tenedor izquierdo 
            self.butler.up()                                   #termina el servicio 
        sys.stdout.write(
            "filosofo [%s] Termina de pensar y comer\n" % self.number)

def main():
    
    n = 6      #numero de filosofos y tenedores 

    butler = Semaphore(n-1)       #butler para evitar el tiempo muerto deadlock

    c = [Chopstick(i) for i in range(n)]  #lista de tenedores

    p = [Philosopher(i, c[i], c[(i+1) % n], butler) for i in range(n)]   #lista de filosofos

    for i in range(n):
        p[i].start()

if __name__ == "__main__":
    main()

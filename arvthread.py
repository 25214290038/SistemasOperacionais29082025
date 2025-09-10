# importação de biblioteca
# permite execultar varias tarefas ao mesmo tempo 
import threading 
# faz com que o código espere o tempo que for colocado, para que ele continue rodando
import time 
# estrtura da thread 
# é a função em que as threads vão rodar( nome: "thread1", número inicial: "50", numero final: "60")
def estruturaTrhead(nome, inicio, fim):
    #faz com que o código repita varias vezes, contando do começo ao fim, um número por vez 
    for i in range(inicio, fim +1):
        # mostra na tela qual thread está rodando e qual número está colocando  
        print(f"{nome} -> {i}") 
       # significa o tempo de pausa entre um número e outro, é bom para não ficar confuso na hora de rodar no terminal 
        time.sleep(1)

#cria a primeira thread que vai contar de 1 a 10 
thread1 = threading.Thread(target=estruturaTrhead, args=("thread1", 1, 10))
#cria a segunda thread que vai contar de 50 a 60 
thread2 = threading.Thread(target=estruturaTrhead, args=("thread2", 50, 60))

#execulta as duas threads ao mesmo tempo 
thread1.start() 
thread2.start()
 





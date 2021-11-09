#Ao ser chamado o objeto, ele gera uma lista com valores iguais ao seu index para representar um grafo

from collections import defaultdict
import itertools
 
class Graph:
 
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.graph = defaultdict(list)
        self.listApproved = []  #Lista que será usada para botar os melhores resultados
        self.min = nVertices # Contador do menor numero possivel a ser encontrado
 
    def addAresta(self, u, v): #função de adicionar as arestas ao grafo
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    def run(self):
        approved = [] #lista de testes aprovados
        #gerar lista de todas as possibilidades possiveis
        combinations = list(itertools.product([False,True], repeat=self.nVertices))
        #verificar lista de todas as possibilidades possiveis
        for test in combinations: 
            #passar por todos os indices
            graphValid  = True
            for u in range(self.nVertices):
                if(test[u]):
                    continue
                #essa variavel será responsavel por dizer se nesse vertice todas as suas ligações está correta
                flag = False;
                #caso a posição ja esteja False,  procurar um vertice com um True, basta apenas encontrar 1
                if(not test[u]):
                    for j in self.graph[u]: #procurar em suas ligações 
                        if(test[j]):
                           flag = True
                           break
                if(not flag): # se pelo menos uma das ligações estaja incorreta , parar o loop e testar o proximo
                    graphValid = False
                    break
                #print("flag: "+str(flag))
                
            if(graphValid):
                approved.append(test)
                if(self.min > test.count(True)):
                    self.min = test.count(True)
                
        
        self.listApproved = approved

    def showBests(self):
        print("Resultados: ")
        for i in self.listApproved:
            if(self.min == i.count(True)):
                for j in range(0,len(i)):
                    if(i[j]):
                        print(j,end= ' ')
                print()


#Exemplo 
#Deve-se botar apenas as Arestas  
 
g = Graph(7)
g.addAresta(0, 1)
g.addAresta(0, 3)
g.addAresta(1, 2)
g.addAresta(1, 6)
g.addAresta(2, 3)
g.addAresta(2, 4)
g.addAresta(3, 5)
g.addAresta(4, 5)
g.addAresta(5, 6)

g.run()
g.showBests()
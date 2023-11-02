### TPC6: Análise de dados: doença cardíaca

#Descarregue o ficheiro de dados: [diabetes_prediction_dataset.csv](./datasets/diabetes_prediction_dataset.csv.zip).

#Encontra mais informação sobre este conjunto de dados [aqui](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset).

#Crie um programa em Python, conjunto de funções, que responda às seguintes questões:
#* Crie uma função que lê a informação do ficheiro para um modelo, previamente pensado em memória;
#* Crie uma função que calcula a distribuição da doença por sexo (tenha atenção que indivíduos doentes e não doentes no dataset);
#* Crie uma função que calcula a distribuição da doença por escalões etários. Considere os seguintes escalões: [0-10], [11-24], [25-29], [30-34], [35-39], [40-44], ...
#* Crie uma função que calcula a distribuição da doença por níveis de glucose. Considere um nível igual a um intervalo de 10 unidades, comece no limite inferior e crie os níveis necessários até abranger o limite superior;
#* Crie uma função que imprime na forma de uma tabela uma distribuição;
#* Especifique um programa que ao executar apresenta as tabelas correspondentes às distribuições pedidas.

def lerficheiro(fnome):
     
     file = open (fnome, "r")
     ficheiro = []
     linhas = file.readlines()
     for linha in linhas[1:]:    #a primeira linha é título
          p = linha.split(",")
          ficheiro.append((str(p[0]), float(p[1]), int(p[2]), int(p[3]), str(p[4]), float(p[5]), float(p[6]), int(p[7]), int(p[8])))
     file.close()
     return ficheiro 


def distdoençapsexo(fnome):
     
     file1 = lerficheiro(fnome)
     h=0
     m=0
     hdiabetes=0
     mdiabetes=0
     
     for linha in file1:
          
          if linha [8] == 1:
               if linha[0] == "Male":
                    hdiabetes = hdiabetes + 1
               else:
                    mdiabetes = mdiabetes + 1
          
          else:
               if linha[0] == "Male":
                    h = h + 1
               else: 
                    m = m + 1
     
     print( hdiabetes, " homens de", h, " homens têm diabetes")
     print( mdiabetes, " mulheres de", m, " mulheres têm diabetes")

def distdoençapescaloesetarios(fnome):
     
     file2 = lerficheiro(fnome)

     escalao1 = []
     escalao2 = []
     escalao3 = []
     escalao4 = []
     escalao5 = []
     escalao6 = []
     escalao7 = []
     escalao8 = []
     escalao9 = []
     
     for linha in file2:
          if linha[8] == 1:
               if linha[1] in range (0,11):
                    escalao1.append(1)
               elif linha[1] in range(11,25):
                    escalao2.append(1)
               elif linha[1] in range(25,30):
                    escalao3.append(1)
               elif linha[1] in range(30,41):
                    escalao4.append(1)
               elif linha[1] in range(41,51):
                    escalao5.append(1)
               elif linha[1] in range(51,61):
                    escalao6.append(1)
               elif linha[1] in range(61,71):
                    escalao7.append(1)
               elif linha[1] in range(71,81):
                    escalao8.append(1)
               elif linha[1] in range(81,90):
                    escalao9.append(1)
     
     print ("Nas idades entre [0-10] anos, existem, ", len(escalao1), "doentes")
     print ("Nas idades entre [11-20] anos, existem, ", len(escalao2), "doentes")     
     print ("Nas idades entre [21-30] anos, existem, ", len(escalao3), "doentes")
     print ("Nas idades entre [31-40] anos, existem, ", len(escalao4), "doentes")
     print ("Nas idades entre [41-50] anos, existem, ", len(escalao5), "doentes")
     print ("Nas idades entre [51-60] anos, existem, ", len(escalao6), "doentes")
     print ("Nas idades entre [61-70] anos, existem, ", len(escalao7), "doentes")
     print ("Nas idades entre [71-80] anos, existem, ", len(escalao8), "doentes")
     print ("Nas idades entre [81-90] anos, existem, ", len(escalao9), "doentes")

def distdoençapglucose(fnome):

     file3 = lerficheiro(fnome)
     glucose = []
     glucosediabeticos= []

     maior = int(0)
     menor = int(100000000)

     for linha in file3:
          if int(linha[7]) > maior:
               maior = linha[7]
          if int(linha[7]) < menor:
               menor = linha[7]
     
     m = menor 
     while m <= maior:
          glucose.append(0)
          m = m + 1
     
     for linha in file3:
          if linha[8] == 1:
               p = menor 
               nglucose = int(linha[7])
               indice = int((int(nglucose)-int(p))/10)
               glucose[indice] = glucose[indice] + 1
     
     for g in glucose:
          p = menor 
          i = p + 9
          glucosediabeticos.append(("[" + str(p) +  "-" + str(i) + "] -- " + str(g) ))
          menor = menor + 10
     
     for dist in glucosediabeticos:
          print(dist)

def tabela(fnome, funçao):
          
     if funçao == 1:
          print("---------- Tabela de distribuição da doença por sexo: ---------- ")
          distdoençapsexo(fnome)
     if funçao == 2:
          print("---------- Tabela de distribuição da doença por escalão etário: ----------")
          distdoençapescaloesetarios(fnome)
     if funçao == 3:
          print("---------- Tabela de distribuição da doença por níveis de glucose: ---------- ")
          distdoençapglucose(fnome)


print ("-----MENU: ------ \n (1) Distribuição da doença por sexo \n (2) Distribuição da doença por escalão etário \n (3) Distribuição da doença por níveis de glucose \n (0) Sair")

opc = int(input("Qual a opção que deseja?"))

while opc != 0:
     if opc == 1:
          tabela("diabetes_prediction_dataset.csv", 1)
          opc = int(input("Qual a opção que deseja?"))
     if opc == 2:
          tabela("diabetes_prediction_dataset.csv", 2)
          opc = int(input("Qual a opção que deseja?"))
     if opc == 3: 
          tabela("diabetes_prediction_dataset.csv", 3)
          opc = int(input("Qual a opção que deseja?"))
          
if opc == 0:
    print("A aplicação terminou! Até à próxima!")


   
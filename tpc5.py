
#TPC5_RESOLUÇÃO

sala1= (150, [], "Twilight")
sala2 = (200, [], "Hannibal")
cinema1 = [sala1 , sala2]

def listar(cinema):
    lista=[]
    for sala in cinema:
        lista.append(sala[2])
    return lista    



def disponivel(cinema,filme,lugar):
    res= True
    cond = str("O seu lugar está disponível")
    for sala in cinema:
        if filme==sala[2]:
            if lugar in sala[1]:
                res= False
                cond = str("O seu lugar não está disponível")
    
    return cond
        


def vendebilhete(cinema,filme,lugar):

    if disponivel(cinema,filme,lugar)==str("O seu lugar está disponível"):
        
        for sala in cinema:
            if filme==sala[2]:
                sala[1].append(lugar)

    
    return cinema


def listardisponibilidades(cinema):
    l=[]
    for sala in cinema:
        info=(sala[2],sala[0]-len(sala[1]))
        l.append(info)
    return l    

def inserirsala(cinema,sala):
    if sala not in cinema:
        cinema.append(sala)
    return cinema    


Menu= print('''
        Menu:
        1. `listar( cinema )` - que lista no monitor todos os filmes que estão em exibição nas salas do cinema passado como argumento;
        2. `disponivel( cinema, filme, lugar )` - que dá como resultado **False** se o lugar lugar já estiver ocupado na sala onde o filme está a ser exibido e dará como resultado **True** se o inverso acontecer;
        3. `vendebilhete( cinema, filme, lugar )` - que dá como resultado um novo cinema resultante de acrescentar o lugar à lista dos lugares ocupados, na sala onde está a ser exibido o filme;
        4. `listardisponibilidades( cinema )` - que, para um dado cinema, lista no monitor para cada sala, o filme que está a ser exibido e o total de lugares disponíveis nessa sala (número de lugares na sala menos o número de lugares ocupados);
        5. `inserirSala( cinema, sala )` - que acrescenta uma sala nova a um cinema (devendo verificar se a sala já existe);
       '''
    )   
    


    
num=int(input('Escreva a sua opçao'))

while num != 0:

    if num==1:

        print("FILMES EM EXIBIÇÃO:")

        lista=listar(cinema1)
        for filmes in lista:
            print(filmes)

        num=int(input('Escreva a sua opçao'))
    

    if num==2:

        print("DISBONIBILIDADE DO SEU LUGAR:")

        filme=str(input('Qual é o filme que quer ver'))
        lugar=int(input('Escolha o lugar'))
        print(disponivel(cinema1,filme,lugar))
        

        num=int(input('Escreva a sua opçao'))
    
    if num==3:

        print("COMPRE O SEU BILHETE:")

        filme=str(input('Qual é o filme que quer ver'))
        lugar=int(input('Escolha o lugar'))
        print(vendebilhete(cinema1,filme,lugar))
        
        num=int(input('Escreva a sua opçao'))

    
    
    if num == 4:
        print("DISPONIBILIDADES LISTADAS:")

        print(listardisponibilidades(cinema1))

        num=int(input('Escreva a sua opçao'))

    if num == 5:

        print("INSIRA UMA NOVA SALA:")

        filme=str(input("Insira o filme"))
        num_lugares=int(input("Insira o número total de lugares"))
        num_lugVendidos = int(input("quantos lugares estão vendidos?"))
        
        
        
        sala3=(num_lugares,num_lugVendidos , filme)
        print(inserirsala(cinema1, sala3))

        num=int(input('Escreva a sua opçao'))


    

    if num == 0: 
         print("A aplicação terminou! Até à próxima!")


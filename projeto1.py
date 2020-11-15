'''1. Controle de cotas de disco. A ACME Inc., uma organização com mais de 1500 funcionários, 
está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este
 problema, o Administrador de Rede precisa saber qual o espaço em disco ocupado pelas contas dos
  usuários, e identificar os usuários com maior espaço ocupado. Através de um aplicativo baixado
   da Internet, ele conseguiu gerar o seguinte arquivo, chamado usuarios.txt:

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o primeiro campo corresponde ao login do usuário e o segundo ao espaço em disco ocupado
 pelo seu diretório home. A partir deste arquivo, você deve criar um programa que gere um relatório, 
 chamado relatório.txt, no seguinte formato:

ACME Inc.           Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

Um Kilobyte é composto por 1024 bytes. Portanto, é maior que 1 byte; Um Megabyte é composto por 1024 Kilobytes.
1    alexandre       434,99 MB            16,85%
2    anderson       1187,99 MB            46,02%
3    antonio         117,73 MB             4,56%
4    carlos           87,03 MB             3,37%
5    cesar             0,94 MB             0,04%
6    rosemary        752,88 MB            29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários,
 de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes
  deverá ser feita através de uma função separada, que será chamada pelo programa principal. 
  O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa
  principal.
Recursos adicionais: opcionalmente, desenvolva as seguintes funcionalidades:

Ordenar os usuários pelo percentual de espaço ocupado;'''

usuario = []
valores =[]
dicionario = {}
cabecalho = 'ACME Inc.           Uso do espaço em disco pelos usuarios\n------------------------------------------------------------------------\nNr.  Usuario        Espaço utilizado     % do uso\n'

def converter(valor):
    resultado = ((float(valor)/1024)/1024)
    return resultado

def percentual(espaco, total):
    try:
        esp = ((espaco/total)*100)
        return esp
    except:
        print('Não foi possivel calcular o percentual')


def principal():
    try:
        with open("projeto 1/usuarios.txt",'r') as f:
            valortotal = 0
            f = f.read()
            f = f.replace('\n',' ')
            f.strip()
            m = f.split(' ')
            #separ os valores para criar um dicionario
            for i in m:
                if i != '':
                    if i.isdigit():
                        i = converter(i)
                        i = float(i)

                        valores.append(i)
                        valortotal +=i
                    else:
                        usuario.append(i)
            
            #criacao do dicionario
            for chave, valor in zip(usuario,valores):
                dicionario[chave] = valor

            #organiza os valores em ordem de espaço utilizado e retorna dicionario organizado
            organizado = (list(dicionario.items()))
            organizado.sort(key=lambda x: x[1], reverse=True)
            dicionario.clear()
            for valor in organizado:
                dicionario[valor[0]] = valor[1]
            

        with open('projeto 1/relatorio.txt','w') as w:
            w.write(cabecalho)
            n=1
            while n < len(dicionario):
                for user,valor in zip(dicionario.keys(),dicionario.values()):
                    perc = percentual(valor,valortotal)
                    linha = str(f'{n:<5}{user:<20}{valor:<8.2f} mb {perc:>10.2f}%')
                    #print(f'{n:<5}{user:<20}{valor:<8.2f} mb {perc:>10.2f}')
                    w.write(str(linha))
                    w.write('\n')
                    n+=1
            w.write(f'\nEspaço total ocupado: {valortotal:.2f} MB\nEspaço médio ocupado: {(valortotal/(n-1)):.2f}  MB')  
    except:
        print('Não foi possivel localizar o arquivo selecionado.')

principal()


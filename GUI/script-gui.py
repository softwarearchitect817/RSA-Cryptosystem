# Grupo: Jhonata Tenório, Jorge Lucas.

# BIBLIOTECAS PARA A GUI:

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox

# BIBLIOTECAS PARA O SCRIPT RSA:

import time
import secrets
import math
import random
from random import randint

# DICIONARIOS PARA CRIPTOGRAFIA (DIC1) E DESCRIPTOGRAFIA (DIC2):
dic1 = {"a" : 2, "b" : 3, "c" : 4, "d" : 5, "e" : 6, "f" : 7, "g" : 8, "h" : 9, "i" : 10, "j" : 11,"k" : 12,
  "l" : 13, "m": 14, "n":15, "o" : 16, "p" : 17, "q": 18, "r" : 19, "s":20, "t":21, "u":22, "v":23, "w":24,"x":25,
  "y":26, "z":27, " ":28}

dic2 = {2 : "a", 3 : "b", 4 : "c", 5 : "d", 6 : "e" , 7 : "f" , 8 : "g", 9 : "h", 10 : "i", 11: "j" , 12 : "k" ,
  13 : "l", 14 : "m", 15 : "n", 16 : "o", 17 : "p", 18 : "q", 19 : "r", 20 : "s", 21: "t", 22 : "u", 23: "v", 24 : "w",
  25 : "x", 26 : "y", 27 : "z", 28 : " "}

# FUNCOES MATEMATICAS (SEM INTERAÇÃO DO USUÁRIO):

# FUNCOES DEPENDENTES DA decrypt() e encrypt():
#########################################################################################################################################
def invert(a, b):                                                        # INVERSO MULTIPLICATIVO:
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = invert(b % a, a)
        return (g, x - (b // a) * y, y)
#########################################################################################################################################
def inversom_m(a, m):                                                     # RETORNA O INVERSO MODULAR:
    g, x, y = invert(a, m)
    if g != 1:
        raise Exception('Nao existe inverso modular')
    else:
        return x % m
#########################################################################################################################################
def exp_mod_rap(list_int_pow, d, mod, exp, r):                            # EXPONENCIACAO MODULAR RAPIDA.
    if list_int_pow[-1] >= exp:                                           # CONDICAO DE PARADA.
                                                                          # (LISTA DA DECOMPOSICAO DO EXPOENTE SER PECORRIDA).
        if exp == 1:                                                      # CHECAGEM PARA EXECUTAR A FUNCAO PELA PRIMEIRA VEZ.
            r = d % mod
            if exp in list_int_pow:                                       # VERIFICA SE O EXPOENTE ESTA NA DECOMPOSICAO DO EXPOENTE.
                return r * exp_mod_rap(list_int_pow, d, mod, (exp*2), r)  # RETORNANDO A MULTIPLICACAO SUCESSIVA DOS FATORES.

        else:                                                             # ATRIBUICAO FEITA A 'r' A PARTIR DO SEGUNDO CASO EM DIANTE.
            r = (r*r) % mod 
            if exp in list_int_pow:                                       # VERIFICA SE O EXPOENTE ESTA NA DECOMPOSICAO DO EXPOENTE.
                return r * exp_mod_rap( list_int_pow, d, mod, (exp*2), r) # RETORNANDO A MULTIPLICACAO SUCESSIVA DOS FATORES.

        return exp_mod_rap(list_int_pow, d, mod, (exp*2), r)              # RETORNO DA FUNCAO SEM NENHUMA ATRIBUICAO NECESSARIA.
    
    else:
        return 1
#########################################################################################################################################
def generate_list_int(convert, list_int_pow): # GERADOR DE UMA LISTA QUE CONTEM A DECOMPOSICAO DO NUMERO BINARIO EM POTENCIAS DE BASE 2:
    j = 0                                     # POSICAO NA STRING.
    
    for i in convert:
        if i == "0":                          # SE O ALGARISMO BINARIO DA POSICAO FOR 0 SIMPLESMENTE AVANCA O DIGITO.
            j += 1                            # INCREMENTO DA POSIÇÃO.
        
        else:                                 # DIGITO == 1.
            list_int_pow.append(pow(2, j))    # ADICIONANDO A LISTA UMA POTENCIA DE BASE 2 CUJO EXPOENTE Eh A POSICAO NA STRING (NO CASO O J).
            j += 1                            # INCREMENTO DA POSIÇÃO.
#########################################################################################################################################
def int_bin(div, convert):                    # CONVERTER INTEIRO PARA BINARIO, PEGA INT E RETORNA STRING:

    if div != 1:
        convert = convert + str(div%2)
        return int_bin(div//2, convert)

    else:
        convert = convert + str(div)
        return convert                        # RETORNA UMA STRING COM O BINARIO INVERTIDO.

#########################################################################################################################################
#funcoes usadas pela funcao generate_key()
def euclides(num1, num2):                     # CALCULA O MDC.

        resto = num1 % num2

        if resto == 0:                        # CONDICAO DE RETORNO DO MDC.
            return num2 

        return euclides(num2, resto)
#########################################################################################################################################
def test_prime(n):                            # VERIFICA SE UM NUMERO E PRIMO:

    s = int(math.sqrt(n)) + 3                 # BUSCA UM DIVISOR ATE A RAIZ QUADRADA DO NUMERO EM QUESTAO. CASO NAO ENCONTRE,  ELE E PRIMO.

    if n % 2 == 0:                            # SE O NUMERO FOR PAR, ELE NAO E PRIMO.
        return False 

    for x in range(3, s, 2):                  # CICLO QUE INCREMENTA EM 2 O DIVISOR (INICIALIZADO EM 3) ATE ELE ATINGIR O LIMITE s.
        if n % x == 0:                  
            return False                      # CASO SEJA ENCONTRADO UM DIVISOR ANTES DO s O NUMERO NAO E PRIMO.

    return True                               # CASO NAO TENHA SIDO ENCONTRADO UM DIVISOR NAS CONDICOES ACIMA, O NUMERO E PRIMO.
#########################################################################################################################################
def gen_prime():                              # GERA UM NUMERO PRIMO ALEATORIO DE 32 BITS:

    n = secrets.randbits(32)                  # GERANDO NUMERO ALEATORIO QUE POSSUA 32 BITS.

    while test_prime(n) == False:             # GARANTIR QUE O NUMERO RETORNADO SEJA PRIMO.
        n = secrets.randbits(32)              # ATRIBUINDO UM NOVO NUMERO ALEATORIO n ATE QUE n SEJA PRIMO.

    return n
#########################################################################################################################################
def phi(p, q):                                # FUNÇÃO TOTIENTE DE EULER (P-1)*(Q-1):
    return (p-1)*(q-1)
#########################################################################################################################################
def co_primos(x):                             # RETORNA UM NUMERO CO-PRIMO DO NUMERO PASSADO:
    y = gen_prime()

    while euclides(x, y) !=1:                 # CICLO PARA GARANTIR A CONDICAO DE COPRIMOS (NUMEROS QUE O MDC ENTRE ELES E 1).
        y = gen_prime()                       # ENQUANTO Y NAO ATENDER ESSA CONDICAO ELE VAI SER GERADO NOVAMENTE

    return y
#########################################################################################################################################
# (INTERAÇÃO COM O USUÁRIO):
# FUNCAO QUE GERA A CHAVE PUBLICA:
def generate_key():
    p = gen_prime()
    q = gen_prime()
    while p == q:
        q = gen_prime()
    n = p*q
    tot_n = phi(p, q)
    e = co_primos(tot_n)

    # REMOVE TODOS WIDGETS DA ABA 'GERAR CHAVES':
    
    # frame_top_key1.forget()
    lb1.pack(side = BOTTOM, expand = 1)
    btn1.forget()
    btn2.forget()
    lb1.pack(side = TOP, expand = 1)
    btn3.pack(side = BOTTOM, expand = 1, pady = 30)
    # CRIA OS ARQUIVOS 'PUBLIC_KEY.TXT' E 'PRIVATE_KEY.TXT'.
    create_archive(n, e, p, q)
#########################################################################################################################################
def create_archive(n, e, p, q):
    # REMOVE TODOS WIDGETS DA TELA DE 'INSERIR CHAVES' NA ABA 'GERAR CHAVES':
    lb5.forget()
    e1.forget()
    e2.forget()
    e6.forget()
    btn4.forget()
    # EMPACOTA A LABEL INFORMATIVA E O BOTÃO PROSSEGUIR:
    
    frame_top_key1.pack(side = TOP, expand = 1)
    frame_top_key.forget()

    lb1.pack(side = TOP, expand = 1)
    btn3.pack(side = BOTTOM, pady = 1)
    btn8.pack(side = BOTTOM, pady = 10)
    
    chave_publica = ("Valores da chave publica:\nn = %d e = %d\n" %(n,e))
    chave_privada = ("Valores da chave privada:\ne = %d n = %d p = %d q = %d\n" %(e, n, p, q))
    key = open("../KEYS/public_key.txt", "w")
    key_p = open("../KEYS/private_key.txt", "w")
    key_p.write(chave_privada)
    key.write(chave_publica)
    key_p.close()
    key.close()
#########################################################################################################################################
# BOTÃO 'VALIDAR':
def validate_prime():
    # RECEBE OS VALORES INSERIDOS PELO USUÁRIO E CONVERTE PARA INTEIRO.
    p = int(e1.get())  
    q = int(e2.get())
    e = int(e6.get())
    
    # VERIFICA SE OS VALORES DE 'p'' E 'q' SÃO PRIMOS.
    if(test_prime(p) == False):
        messagebox.showerror("Erro", "p não é primo ou p <= 3\n tente outro valor")
        insert_key()

    elif(test_prime(q) == False):
        messagebox.showerror("Erro", "q não é primo ou q <= 3\ntente outro valor")
        insert_key()
        
    elif p == q:
        messagebox.showerror("Erro", "p e q são iguais")   
        insert_key()

    n = p*q
    tot_n = phi(p, q)
    
    # VERIFICA SE O VALOR DE n É UM CO-PRIMO DE 'p'' E 'q'.
    if euclides(tot_n, e) !=1:
        messagebox.showerror("Erro", "Esse número não é um co-primo")
        insert_key()
        
    # SE TUDO ESTIVER CORRETO, GERA O ARQUIVO 'PUBLIC_KEY.TXT' E 'PRIVATE_KEY.TXT' NO ARQUIVO 'KEYS'.
    if(test_prime(p) != False and test_prime(q) != False and euclides(tot_n, e) == 1):
        create_archive(n, e, p, q)
#########################################################################################################################################
## BOTÃO 'NOVA CHAVE':
def new_key():                                                               # FUNCAO QUE RETORNA A TELA INICIAL DE GERAÇÃO DE CHAVES
    lb1.forget()                                                             # REMOVE DA TELA LABEL INFORMATIVA
    btn8.forget()                                                            # REMOVE DA TELA BOTÃO NOVA CHAVE
    btn3.forget()                                                            # REMOVE DA TELA BOTÃO PROSSEGUIR

    btn1.pack(side = TOP,    padx = 4, pady = 30, expand = 0)                #EMPACOTAMENTO DO BOTÃO GERAR CHAVES
    btn2.pack(side = BOTTOM, padx = 4, pady = 1 , expand = 0)                #EMPACOTAMENTO DO BOTÃO INSERIR CHAVES

#########################################################################################################################################
## FUNÇÃO QUE LEVA PARA A ABA CRIPTOGRAFAR
def prosseguir():
    e1.forget()                                           #FORGET() TIRA DA TELA A ENTRADA DO VALOR DE 'p'
    e2.forget()                                           #FORGET() TIRA DA TELA A ENTRADA DO VALOR DE 'q'
    e6.forget()                                           #FORGET() TIRA DA TELA A ENTRADA DO VALOR DE 'e'
    lb5.forget()                                          #FORGET() TIRA DA TELA A LABEL DE INSTRUÇÃO
    btn4.forget()                                         #FORGET() TIRA DA TELA O BOTÃO VALIDAR
    tab_control.select(cript)                             #REDIRECIONA PARA A ABA CRIPTOGRAFAR
    lb1.pack(side = TOP, expand = 1)                      #EMPACOTAMENTO DA LABEL INFORMATIVA
    btn3.pack(side = BOTTOM, expand = 1, pady = 30)       #EMPACOTAMENTO DO BOTÃO PROSSEGUIR
    e7.focus()                                            #FOCUS() JÁ DEIXA SELECIONADA A ENTRADA DO VALOR DE 'n'

#########################################################################################################################################
## BOTÃO 'INSERIR CHAVES':
def insert_key():
    # RETIRA OS BOTÕES DA TELA DE ESCOLHA NA ABA 'GERAR CHAVES'.
    frame_top_key.pack(side = TOP, expand = 1)      # EMPACOTAMENTO DO FRAME SUPERIOR.
    frame_top_key1.forget() 
    btn1.forget()
    btn2.forget()
    
    lb5.pack(side = TOP)                            # EMPACOTAMENTO DA LABEL DE INSTRUÇÃO;
    e1.pack(side = TOP, expand = 1, pady = 10)      # EMPACOTAMENTO DA ENTRADE DE 'p'';
    e2.pack(side = TOP, expand = 1, pady = 10)      # EMPACOTAMENTO DA ENTRADE DE 'q';
    e6.pack(side = TOP, expand = 1, pady = 10)      # EMPACOTAMENTO DA ENTRADE DE 'e';
    e1.focus()                                      # DÁ FOCO NA ENTRADA DE 'p';
    btn4.pack(side = BOTTOM, pady = 10)             # EMPACOTAMENTO DO BOTÃO VALIDAR.
#########################################################################################################################################
def decrypt():
    # ENTRADAS DO USUARIO:
    e = int(e3.get())                # PEGANDO O VALOR DE 'e' E CONVERTENDO PARA INTEIRO;
    p = int(e4.get())                # PEGANDO O VALOR DE 'p'' E CONVERTENDO PARA INTEIRO;
    q = int(e5.get())                # PEGANDO O VALOR DE 'q' E CONVERTENDO PARA INTEIRO.

    # CALCULO DOS VALORES NECESSARIOS:
    n = p * q
    tot_n = ((p-1) * (q-1))
    d = inversom_m(e, tot_n)                          # INVERSO MULTIPLICATIVO DE 'e', FUNDAMENTAL PARA A DESCRIPTOGRAFIA.

    #manipulação do arquivo de entrada
    arquivo_cript = open("../encrypt&decryptFiles/encrypted.txt", "r")        # ABRINDO O ARQUIVO CRIPTOGRAFADO INDICADO PELO USUARIO.
    mensagem = arquivo_cript.read()                   # ATRIBUINDO O CONTEUDO DO ARQUIVO CRIPTOGRAFADO A UMA STRING.

    lista = mensagem.split(" ")                       # SEPARANDO CADA LETRA CRIPTOGRAFADA E AS SALVANDO COMO ELEMENTO DE UMA LISTA.
    
    arquivo_cript.close()                             # FECHANDO O ARQUIVO DE ENTRADA.

    #processo de descriptografia
    desc = ""                                         # STRING VAZIA QUE VAI ARMAZENAR A MENSAGEM DESCRIPTOGRAFADA.

    for item in lista:
        #objetos auxiliares
        list_int_pow = []                             # LISTA AUXILIAR QUE GUARDA DECOMPOSICAO DE BASE 2 DO EXPOENTE
        if item == '':                                # CONDICAO PRA NAO BUGAR NO ULTIMO ITEM DA LISTA QUE SEMPRE VAI SER VAZIO
            break
        x = int(item)                                 # ATRIBUI A X O INTEIRO DA LISTA QUE VAI SER DESCRIPTOGRAFADO EM UM CARACTER
        #r = (x**d) % n
        convert = int_bin(d, "")                      # CONVERTENDO EXPOENTE 'd' EM BINARIO PARA PODER INICIAR A EXPONENCIAÇÃO;
        generate_list_int(convert, list_int_pow)      # ARMAZENANDO EM UMA LISTA A DECOMPOSIÇÃO DO EXPOENTE EM POTENCIAS DE BASE 2;
        y = exp_mod_rap(list_int_pow, x, n, 1, 0)     # EXECUTANDO A EXPONENCIACAO MODULAR RAPIDA COM O EXPOENTE 'd'.
        
        desc = desc + dic2[y%n]                       # CONCATENANDO A MENSAGEM COM O CARACTER DESCRIPTOGRAFADO.

    #manipulacao do arquivo de saida
    desc = desc.upper()                               # DEIXANDO TODOS AS LETRAS DA MENSAGEM EM CAIXA ALTA.

    arquivo_descript = open("../encrypt&decryptFiles/decrypted.txt", "w")     # CRIANDO ARQUIVO .txt PARA RECEBER MENSAGEM DESCRIPTOGRAFADA.
    arquivo_descript.write(desc)                      # ESCREVENDO MENSAGEM DESCRIPTOGRAFADA NO ARQUIVO.
    arquivo_descript.close()                          # FECHANDO O ARQUIVO.

    # RETIRA TODOS WIDGETS DA ABA 'DESCRIPTOGRAFAR': 
    lb4.forget()
    e3.forget()
    e4.forget()
    e5.forget()
    btn7.forget()
    # EMPACOTA A LABEL INFORMATIVA.
    lb6.pack(side = TOP, pady = 70)
#########################################################################################################################################
def encrypt():
    # ENTRADAS PROVIDAS PELO USUARIO:
    n = int(e7.get())                                  # PEGANDO O VALOR DE 'n' DA ENTRADA E CONVERTENDO PARA INTEIRO.
    e = int(e8.get())                                  # PEGANDO O VALOR DE 'e' DA ENTRADA E CONVERTENDO PARA INTEIRO.
    mensagem  = scroll.get('1.0', END)                 # CAPTURANDO O TEXTO DIGITADO NA SCROLLEDTEXT.
    mensagem = mensagem.lower()                        # DEIXANDO AS LETRAS DA STRING EM MINUSCULO PARA NAO CONFLITAR COM OS DICIONARIOS.
    
    i = 0                                              # INTEIRO QUE REPRESENTA A POSICAO DA LETRA NA STRING.
    error = 0                                          # INTEIRO AUXILIAR PARA TRATAMENTO DE ERRO.
    criptografado = ""                                 # STRING INICIALMENTE VAZIA QUE GUARDA A MENSAGEM CRIPTOGRAFADA.
    while i < int(len(mensagem) - 1):
        list_int_pow = []                              # LISTA AUXILIAR GUARDA A DECOMPOSICAO EM BASE 2 DO EXPOENTE.
        
        try :
            x = dic1[mensagem[i]]
        except :
            error = -1
            break
        x = dic1[mensagem[i]]                          # VALOR DE DETERMINADO CARACTER ATRIBUIDO DE ACORDO COM O DICIONARIO.
        convert = int_bin(e, "")                       # CONVERTENDO O VALOR DE E (O EXPOENTE DA POTENCIACAO) EM BINARIO.
        generate_list_int(convert, list_int_pow)       # ARMAZENANDO EM "LIST_INT POW" OS VALORES NA BASE 2  QUE DECOMPOEM O VALOR 'e'.

        y = exp_mod_rap(list_int_pow, x, n, 1, 0)      # EXPONENCIACAO MODULAR RAPIDA PARA CRIPTOGRAFAR A MENSAGEM.
            
        criptografado = criptografado + str(y%n) +" "  # CONCATENANDO A LETRA CRIPTOGRAFADA NA STRING.
        i+=1

    # MANIPULANDO ARQUIVO DE SAIDA:
    if error == -1:
        messagebox.showerror("Erro", "Caractere inválido.\nApenas letras sem acentos e sem pontuações.") # BOX DE ERRO PARA CARACTERES INVÁLIDOS
    else:
        arquivo = open("../encrypt&decryptFiles/encrypted.txt", "w")             # GERANDO ARQUIVO .txt QUE GUARDARÁ O TEXTO CRIPTOGRAFADO
        arquivo.write(criptografado)                           # ESCREVENDO A MENSAGEM CRIPTOGRAFADA NO ARQUIVO.
        arquivo.close()                                        # FECHANDO O ARQUIVO.

        #RETIRA TODOS WIDGETS DA ABA CRIPTOGRAFAR 
        lb2.forget()
        e7.forget()
        e8.forget()
        scroll.forget()
        btn5.forget()
        # EMPACOTA LABEL INFORMATIVA 
        lb3.pack(side = TOP, pady = 80)
#########################################################################################################################################
###---------- INICIO DA GUI ----------###

## CONFIGURAÇÕES DO FORMATO A JANELA
window = Tk()                             #CRIAÇÃO DA JANELA PRINCIPAL
window.geometry("300x300+200+200")        #DIMENSIONAMENTO DA JANELA
window.resizable(0, 0)                    #BLOQUEIO DO REDIMENSIONAMENTO
window.title("RSA")                       #TÍTULO
window.iconbitmap("icon.ico")             #ÍCONE

## CRIAÇÃO E CONFIGURAÇÃO DAS ABAS
tab_control = ttk.Notebook(window)                  #CRIAÇÃO DA INSTÂNCIA DE ABAS
key = ttk.Frame(tab_control)                        #FRAME GERAL DA ABA GERAR CHAVES
cript = ttk.Frame(tab_control)                      #FRAME GERAL DA ABA CRIPTOGRAFAR
dcript = ttk.Frame(tab_control)                     #FRAME GERAL DA ABA DESCRIPTOGRAFAR
tab_control.add(key,text="Gerar chaves")            #ADICIONANDO A ABA GERAR CHAVES
tab_control.add(cript,text="Criptografar")          #ADICIONANDO A ABA CRIPTOGRAFAR
tab_control.add(dcript,text="Descriptografar")      #ADICIONANDO A ABA DESCRIPTOGRAFAR
tab_control.pack(expand=1, fill= BOTH)              #EMPACOTAMENTO DAS ABAS

## ABA GERAR CHAVES
# FRAMES E WIDGETS
frame_top_key = Frame(key)
frame_top_key1 = Frame(key)                                                          #FRAME SUPERIOR DA ABA
frame_bottom_key = Frame(key)                                                       #FRAME INFERIOR DA ABA
lb1 = Label(frame_top_key1, text = "Suas chaves foram validadas!\n\nOs arquivos private_key.txt e public_key.txt\nforam criados no diretório 'RSA-PROJECT/KEYS'.\nProssiga com a criptografia da sua mensagem\nclicando abaixo.") #LABEL INFORMATIVA
btn1 = Button(frame_top_key1, text="Gerar Chaves", command = generate_key, height = 1, width = 14)         #BOTÃO GERAR CHAVES
btn2 = Button(frame_top_key1, text="Inserir Chaves", command = insert_key, height = 1, width = 14)        #BOTÃO INSERIR CHAVES
lb5 = Label(frame_top_key, text = "Digite os valores de p, q e de um co-primo\na esses dois números, nessa ordem.\n*p e q devem ser diferentes e maiores que 3*") #LABEL DE INSTRUÇÃO
e1 = Entry(frame_top_key)                                                   #ENTRADA DO VALOR DE 'p'
e2 = Entry(frame_top_key)                                                   #ENTRADA DO VALOR DE 'q'
e6 = Entry(frame_top_key)                                                   #ENTRADA DO VALOR DE 'e'
btn3 = Button(frame_top_key1, text = "Prosseguir", command = prosseguir)    #BOTAO PROSSEGUIR
btn4 = Button(frame_top_key, text = "Validar", command = validate_prime)    #BOTAO VALIDAR
btn8 = Button(frame_top_key1, text = "Nova Chave", command = new_key)       #BOTAO HOME
frame_top_key1.pack(side = TOP, expand = 1)                                 #EMPACOTAMENTO DO FRAME SUPERIOR
btn1.pack(side = TOP, padx = 10, pady = 6 , expand=1)                       #EMPACOTAMENTO DO BOTÃO GERAR CHAVES
btn2.pack(side = TOP, padx = 10, pady = 6, expand=1)                        #EMPACOTAMENTO DO BOTÃO INSERIR CHAVES

## ABA CRIPTOGRAFAR
# FRAMES E WIDGETS
frame_top_cript = Frame(cript)                  #FRAME SUPERIOR DA ABA
frame_bottom_cript = Frame(cript)               #FRAME INFERIOR DA ABA
lb2 = Label(frame_top_cript, text = "Insira 'n, 'e' e sua mensagem para ser criptografada.\nObs.: Apenas letras sem acentos e pontuações.")  #LABEL DE INSTRUÇÃO
lb2.pack(side = TOP, expand = 1, pady = 2)     #EMPACOTAMENTO DA LABEL DE INSTRUÇÃO
e7 = Entry(frame_top_cript)                   #ENTRADA DO VALOR DE 'n'
e8 = Entry(frame_top_cript)                   #ENTRADA DO VALOR DE 'e'
e7.pack(side = TOP, expand = 1)                            #EMPACOTAMENTO DA ENTRADA DE 'n'
e8.pack(side = TOP, expand = 1)                            #EMPACOTAMENTO DA ENTRADA DE 'e'
scroll = scrolledtext.ScrolledText(frame_bottom_cript, width = 40, height = 8)           #WIDGET DA CAIXA DE TEXTO COM SCROLL
btn5 = Button(frame_bottom_cript, text="Criptografar", command = encrypt)       #BOTÃO CRIPTOGRAFAR
scroll.pack(side = TOP, padx = 10, pady = 7)                                   #EMPACOTAMENTO DA CAIXA E TEXTO
btn5.pack(side = BOTTOM, padx = 10, pady = 2)                                       #EMPACOTAMENTO DO BOTÃO CRIPTOGRAFAR
frame_top_cript.pack(side = TOP, expand = 1)                                    #EMPACOTAMENTO DO FRAME SUPERIOR
frame_bottom_cript.pack(side = BOTTOM, expand = 1)                              #EMPACOTAMENTO DO FRAME INFERIOR
lb3 = Label(frame_top_cript, text = "Sua mensagem já foi criptografada e o\narquivo encrypted.txt foi gerado no diretório\n'RSA-PROJECT/encrypt&DecryptFiles/'.")  #LABEL INFORMATIVA

## ABA DESCRIPTOGRAFAR
# FRAMES E WIDGETS
frame_dcript = Frame(dcript)          #FRAME DA ABA
e3 = Entry(frame_dcript)              #ENTRADA DO VALOR DE 'e'
e4 = Entry(frame_dcript)              #ENTRADA DO VALOR DE 'p'
e5 = Entry(frame_dcript)              #ENTRADA DO VALOR DE 'q'
lb4 = Label(frame_dcript, text = "Digite os valores de e, p e q nessa ordem\npara descriptografar seu arquivo.") #LABEL DE INSTRUÇÃO
lb4.pack(side = TOP, pady = 5)        #EMPACOTAMENTO DA LABEL DE INSTRUÇÃO
e3.pack(side = TOP, pady = 20)        #EMPACOTAMENTO DA ENTRADA DE 'e'
e4.pack(side = TOP, pady = 20)        #EMPACOTAMENTO DA ENTRADA DE 'p'
e5.pack(side = TOP, pady = 20)        #EMPACOTAMENTO DA ENTRADA DE 'q'
lb6 = Label(frame_dcript, text = "Seu arquivo foi descriptografado e está no diretório\n'RSA-PROJECT/encrypt&DecryptFiles/decrypted.txt'") #LABEL INFORMATIVA DE QUE O ARQUIVO FOI GERADO
btn7 = Button(frame_dcript, text="Descriptografar", command = decrypt)  #BOTÃO PARA DESCRIPTOGRAFAR O ARQUIVO
btn7.pack(side = BOTTOM, pady = 10)   #EMPACOTAMENTO DO BOTÃO DESCRIPTOGRAFAR
frame_dcript.pack()                   #EMPACOTAMENTO DO FRAME PRINCIPAL DA ABA

window.mainloop()                     #LOOP DA JANELA PRINCIPAL

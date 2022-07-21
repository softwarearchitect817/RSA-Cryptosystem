<p align="center">
  <img src="https://raw.githubusercontent.com/jhonataT/RSA-PROJECT/master/GUI/icon.ico" height="128" />
</p>

<p align="center">
  <strong> CRIPTOGRAFIA E DESCRIPTOGRAFIA RSA: </strong>
  <br/>
  <br/>
  <a href="https://github.com/JhonataT/RSA-PROJECT"><img src="https://img.shields.io/pypi/pyversions/3?style=flat-square" alt="python"></a>
</p>

Tópicos deste projeto:
=================
<!--ts-->
   * [Sobre o projeto](#Sobre)
   * [Instalação](#instalando)
   * [Como usar](#como-usar)
   * [Funcionalidades](#Funcionalidades)
<!--te-->

<a href="#Sobre"> 
  <h1>Sobre:</h1>
  <p><strong>Alunos: Jhonata Tenório e Jorge Lucas.</strong></p>
  <p>Projeto de Criptografia RSA para a nota final da disciplina de Matemárica Discreta, Universidade Federal de Alagoas.</p>
  <p><strong>O Método RSA:</strong></p>
  <p>
    RSA <strong>(Rivest-Shamir-Adleman)</strong> é um dos primeiros sistemas de criptografia de chave pública e é 
    amplamente utilizado para transmissão segura de dados. Neste sistema de criptografia, a chave
    de encriptação é pública e é diferente da chave de decriptação que é secreta (privada).
  </p>
</a>

<a href="#instalando">
  <h1>Instalando:</h1>
  <p> 
    <strong>Instale o <a href="https://git-scm.com/downloads"> GIT </a>  e o <a href="https://www.python.org/downloads/">PYTHON3.</a></strong> 
  </p>
</a>

<p>(1.0) Abra o seu terminal e digite:</p>

```cmd
> git clone https://github.com/jhonataT/RSA-PROJECT
```

<p>(1.1) Acesse o diretório do projeto:</p>

```cmd
> cd RSA-PROJECT/GUI
```
<p>(1.2) Execute o arquivo 'script-gui.py':</p>

```cmd
> python3 script-gui.py
```

<a href="#como-usar">
  <h1>Como usar:</h1>
  <p><strong>Esolha entre três opções:</strong></p>
</a>

<!--ts-->
   * [Gerar chaves](#Gerando-chaves)
   * [Encriptar](#encriptando)
   * [Desencriptar](#desencriptando)
<!--te-->

<br/>

<a href="#gerando-chaves">
  <h2><strong>Gerando chaves:</strong></h2>
  <img src="https://user-images.githubusercontent.com/51134324/102367172-357e9880-3f98-11eb-9000-4ffd81355472.PNG" />
  <img src="https://user-images.githubusercontent.com/51134324/102369641-ef770400-3f9a-11eb-9e87-f629c44059f1.PNG" />
  <img src="https://user-images.githubusercontent.com/51134324/102369161-652ea000-3f9a-11eb-972f-32c2978886bc.PNG" />
</a>

<br/>

<a href="#encriptando">
  <h2><strong>Encriptando:</strong></h2>
  <img src="https://user-images.githubusercontent.com/51134324/102373274-c9536300-3f9e-11eb-907a-ed84b89ddbb5.PNG" />
  <img src="https://user-images.githubusercontent.com/51134324/102373914-77f7a380-3f9f-11eb-871a-1d43f677204d.PNG" />
  <br/>
  <img src="https://user-images.githubusercontent.com/51134324/102370945-6eb90780-3f9c-11eb-949f-ba55df902502.PNG" />
  <br/>
  <img src="https://user-images.githubusercontent.com/51134324/102374177-cdcc4b80-3f9f-11eb-8eed-dee2261d128c.PNG" />
</a>

<a href="#desencriptando">
  <h2><strong>Desencriptando:</strong></h2>
  <img src="https://user-images.githubusercontent.com/51134324/102392479-de87bc00-3fb5-11eb-809a-7bc92dbc1bad.PNG" />
  <img src="https://user-images.githubusercontent.com/51134324/102392892-6e2d6a80-3fb6-11eb-9350-f6390f4afac3.PNG" />
  <img src="https://user-images.githubusercontent.com/51134324/102393064-a46aea00-3fb6-11eb-9a29-cd4da932b058.PNG" />
  <br/>
  <img src="https://user-images.githubusercontent.com/51134324/102399958-07ad4a00-3fc0-11eb-8283-fca38e7e31a2.PNG" />
  <img src="https://user-images.githubusercontent.com/51134324/102393314-f1e75700-3fb6-11eb-91f0-cf401353547d.PNG" />
</a>

<br/>

<a href="#Funcionalidades">
  <h1><strong>Funcionalidades:</strong></h1>
  <p><strong>Gerar chaves:</strong></p>
</a>

```python

def generate_key():
    p = gen_prime()
    q = gen_prime()
    
    while p == q:
        q = gen_prime()
        
    n = p*q
    tot_n = phi(p, q)
    e = co_primos(tot_n)
    
```
<p><strong>
    ➥ Para gerar as chaves, usamos a função 'generate_key()' com o seguinte algoritmo:
      <p>I. Usando a função: 'gen_prime()', geramos dois primos de 32 bits ('p' e 'q');</p>
      <p>II. Com 'p' e 'q', temos 'n' ('n' = 'p' * 'q');</p>
      <p>III. Com a função: 'phi(p, q)', calculamos a função totiente de Euler [ϕ(n) = (p - 1)(q - 1)];</p>
      <p>IV. Por último, iremos usar a função 'co_primos(tot_n) para achar um inteiro 'e' tal que 1 < 'e' < 'ϕ(n)', de forma que 'e' e 'ϕ(n)' sejam co-primos.</p>
 </strong></p>


<br/>
<p><strong>Encriptar:</strong></p>

```python
def encrypt():
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
        i += 1
```

<p><strong>
    ➥ Para encriptar a mensagem, usamos a função 'encrypt()' com o seguinte algoritmo:
      <p>I. Recebemos 'n', 'e' e a 'mensagem' do usuário, convertendo o conteúdo da 'mensagem' para minúsculo;</p>
      <p>II. Percorremos cada caractere da 'mensagem' e relacionamos o caractere com o inteiro correspondente no dicionário (dic1);</p>
      <p>III. Convertemos o valor de 'e' para binário e decompomos em base 2, salvando em cada posição de uma lista ('list_int_pow') o valor convertido em inteiro do bit atual;</p>
      <p>IV. Usando 'n' e 'e', da  chave pública, faremos a exponenciação modular rápida dos valores da lista ('list_int_pow') para resolver [C = T^e (mod n)], onde: C é o caractere criptografado, 'T' é o valor de cada posição da lista, 'e' e 'n' são fornecidos pelo usuário. Dessa forma, cada letra da mensagem será criptografada separadamente.</p>
      <p>V. Escrevemos o valor resultante de cada letra, concatenado com espaço " ", no arquivo encrypted.txt</p>
 </strong></p>
 
 <br/>

<p><strong>Desencriptar:</strong></p>

```python
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
```
<p><strong>
    ➥ Para desencriptar a mensagem, usamos a função 'decrypt()' com o seguinte algoritmo:
      <p>I. Recebemos 'e', 'p' e 'q' do usuário (chaves privadas);</p>
      <p>II. Achamos o inverso multiplicativo de 'e', fundamental para a descriptografia;</p>
      <p>III. Atribuimos o conteúdo do arquivo CRIPTOGRAFADO a uma string;</p>
      <p>IV. Separamos cada letra da mensagem em uma lista;</p>
      <p>V. Convertemos o expoente 'd' em binário para poder iniciar a exponenciação;</p>
      <p>VI. Armazenamos em uma lista a decomposição do expoente em potências de base 2;</p>
      <p>VII. Executamos a exponenciação modular rápida com o expoente 'd', para resolver [T = C^d (mod  n)], onde T é o caractere original, C é o caractere criptografado, 'd' é o inverso multiplicativo de 'e' e 'n' é fornecido pelo usuário.</p>
      <p>VIII. Depois de resolvido o inverso multiplicativo, resolve-se a exponenciação modular rápida e conseguimos retornar para o valor original T, que está relacioando no dicionário (dic2), então escrevemos no arquivo decrypted.txt cada caractere, formando a frase originalmente criptografada.</p>
 </strong></p>

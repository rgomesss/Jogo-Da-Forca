from random import choice
from time import sleep


palavra_secreta = ['caracol','espingarda','escola',
'cama','banheiro','celular','parede','cachorro',
'lixo','galinha','ventilador','helicóptero','foguete',
'caderno','teclado','casaco','computador','mulher',
'macaco','zebra','banana','bola','boneco','hospital',
'guarda roupa','escova de dente','boneco de neve',
'estrela','cometa','carroça','tubarão','televisão',
'abominação','calça','jaguatirica','buraco negro',
'índio','lençol','lápis','pé','ventilação','botão',
'papel','cabeça','xícara','disco voador','maçã']
  
linhas = []
letras_usadas = []
escolhe_palavras = choice(palavra_secreta).lower()
cont = 1

letras_erradas = ''
le = 0

palavra_escolhida = list(escolhe_palavras)

ganhou = False
vidas = 6
#Transforma a palavra escolhida em traços↓
for t in range(0, len(palavra_escolhida)):
  linhas.append('_')


while ganhou == False: 
  acertou = 0 
  print(f'\n♥️{vidas}️\n')
  
  print(f'Letras Erradas: {letras_erradas[:-2].upper()}\n')
  print(f"{'PALAVRA'}\n\n")
  
  for t in range(0, len(palavra_escolhida)):
    if ' ' in palavra_escolhida[t]:
      linhas[t] = '-'
    print(linhas[t].upper(), end=' ')
  print('\n')
  
  if vidas < 1:
    print(f"\n{'GAME OVER'}\n\n- Suas vidas acabaram\nA PALAVRA ERA {escolhe_palavras.upper()}")
    break
    
  #INPUT PRINCIPAL  
  letra = input('Letra: ').lower().strip()
  salVe = letra
  print('\n')
  
  #Detects
  detect_espaço = salVe.isspace()
  detect_letra = salVe.isalpha()
  
  '''Loop caso o usuário tente fechar
     o programa↓'''
  while len(salVe) > 1 or salVe == '' or detect_espaço == True or detect_letra == False:
    print('- Digite UMA letra\n')
    letra = input('Letra: ').lower().strip()
    salVe = letra
    detect_espaço = salVe.isspace()
    detect_letra = salVe.isalpha()
    print('\n')
 
  if letra == 'a':
    letra = ['a','ã','á','à','â','ä','å','æ','ª']
  elif letra == 'c':
    letra = ['c','ç','ć','č']
  elif letra == 'o':
    letra =  ['ò','o','ô','õ','ó','º','ō','ø','œ','ö']
  elif letra == 'e':
    letra = ['è','e','ê','é','ē','ę','ė','ë']
  elif letra == 'i':
    letra = ['i','ì','î','í','ī','ï','į']
  elif letra == 'u':
    letra = ['u','ú','û','ù','ū','ù','û']

   #Tranforma os traços em letras↓ 
  for t in range(0, len(palavra_escolhida)):
    if palavra_escolhida[t] in letra:
      linhas[t] = palavra_escolhida[t]
      acertou = acertou + 1
 
  #Tira vida caso a letra n esteja na palavra
  if acertou < 1 and salVe not in letras_usadas:
    print('\n' * 5)
    print(f"- A letra '{salVe.upper()}' não está na palavra \n\n{'-1♥️':^37}","\n" * 6)   
    sleep(2)
    vidas -= 1    
    letras_erradas += salVe + ', '
  else:
    print('\n' * 5)
  
  #LETRAS USADAS
  if salVe in letras_usadas:
    print(f"- A letra '{salVe.upper()}' já foi usada", "\n" * 5)
    sleep(3)
  else:  
    letras_usadas.append(salVe)
    
  '''Quando o jogador completa a palavra 
     esse if vai dar a vitória'''
  if not '_' in linhas:
    for t in range(0, len(palavra_escolhida)):
      print(linhas[t].upper(), end=' ')
    print('\n')
    print(f'PARABENS VOCÊ ACERTOU A PALAVRA: \n{escolhe_palavras.upper()}\n\n')
    ganhou = True
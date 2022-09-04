from random import choice
from time import sleep


guessed = False

#RETIRAR AS PALVRAS DA TABELA

with open('Tenmo/palavras.txt', 'r', encoding='utf=8') as list_words:
        wordiesInRaw = list_words.readlines()
        global listOfWords
        listOfWords = []
        wordsWhoutSpace =[]
        for conjunto in wordiesInRaw:
            wordsWhoutSpace += conjunto.split('\n')
        while '' in wordsWhoutSpace:
            wordsWhoutSpace.remove('')
        for conjunto in wordsWhoutSpace:
            listOfWords += conjunto.split(':')
        while '' in listOfWords:
            listOfWords.remove('')

#PUXAR PALAVRA ALEATÓRIA

def prepararTermo(listOfWords):
    termo = choice(listOfWords)
    letrasRepetidas = []
    
    for letra in termo:
        if termo.count(letra) > 1:
            letrasRepetidas.append(letra)
    
           
    return termo, letrasRepetidas
  
#RODAR O JOGO 
def runGame(termo, letrasRepetidas):
    
    global guessed
    guessed = False
    print("_  _  _  _  _")
    
    
    
    while guessed == False:
        mark, termo, appear, guessed = checkWord(input().upper(), termo, letrasRepetidas)
        print(appear) 
        print(mark)
        
    sleep(0.7)
    playAgain = input("Sensacional! Quer jogar denovo?")
    if playAgain.upper() == "S":
        terminho, letrinhasRepetidas = prepararTermo(listOfWords)
        runGame(terminho, letrinhasRepetidas)
    else: 
        print("Ok, até mais!")
#CHECAR A PALAVRA    
def checkWord(tent, termo, letrasRepetidas):
        
        tent = tent.upper()
        
        letrasQueForam = []
        marcation = ["0  ", "0  ", "0  ", "0  ", "0  "]
        positionMarcation = 0
        posTermo = 0
        mark = ""
        appear = ""
    #palavras proibidas
        naoPode = ["AAAAA", "EEEEE", "IIIII", "OOOOO", "UUUUU", "AEIOU"]
    
   
   #se for uma palavra inválida 
        while tent in naoPode or len(tent) > 5 or len(tent) < 5:
            print("Palavra inválida, tente novamente")
            terminho = termo
            letrinhasRepetidas = letrasRepetidas
            runGame(terminho, letrinhasRepetidas)
    
    
#CHECKING
    
    #Aparecimento das letras
        for letra in tent:
            appear += letra + "  "
        
    #Para letras que estão na posição certa
        for letra in tent:
            
            if letra == termo[posTermo]:
                marcation[positionMarcation] = "&  "
                letrasQueForam.append(letra)
            positionMarcation += 1
            posTermo += 1            
            
        #Adicionar as letras repetidas
            #if letra in letrasRepetidas:
                #repetidasQueForam.append(letra)
            
        
        positionMarcation = 0
        posTermo = 0
        
        
    #Para letras certas na posição errada e letras erradas
        for letra in tent:
            if marcation[positionMarcation] == "&  ":
                positionMarcation += 1
                posTermo += 1
                continue
            
            if letra in termo and letra not in letrasQueForam:
                marcation[positionMarcation] = "/  "
                letrasQueForam.append(letra)

            elif letra in termo and letrasRepetidas.count(letra) > letrasQueForam.count(letra):
                marcation[positionMarcation] = "/  "
                letrasQueForam.append(letra)
            
            else:
                marcation[positionMarcation] = "*  "
            
            positionMarcation += 1
            posTermo += 1
            

        positionMarcation = 0
        posTermo = 0

        
        
        for item in marcation:
                
            mark += item
        if mark == "&  &  &  &  &  ":
            global guessed
            guessed = True
            
        return mark, termo, appear, guessed

print("Bem vindi ao Tenmo! Agora atualizado")
sleep(0.7)
print("""
O jogo funciona da seguinte maneira:
    O símbolo "& " mostra que a letra está na posição correta.
    O símbolo " / " mostra que a letra existe, mas está na posição errada.
    O símbolo " * " indica que a letra não existe na palavra.
    """)
sleep(0.7)
print("Bom jogo e boa sorte!")

    
#RODANDO O JOGO    
terminho, letrinhasRepetidas = prepararTermo(listOfWords)
runGame(terminho, letrinhasRepetidas)
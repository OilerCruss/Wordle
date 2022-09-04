from random import choice
from time import sleep


guessed = False

#RETIRAR AS PALVRAS DA TABELA

with open('palavras.txt', 'r', encoding='utf=8') as list_words:
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
        print(termo)
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
        
        repetidasQueForam = []
        marcation = ["", "", "", "", ""]
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
        for letra in tent:
            
       
            if letra == termo[posTermo]:
                if letra in repetidasQueForam and termo.count(letra) <= repetidasQueForam.count(letra):
                    marcation[positionMarcation] = "*  "
                else:    
                    marcation[positionMarcation] = "&  "
            
            
            elif letra in termo and letra != termo[posTermo]:
                if letra in repetidasQueForam and termo.count(letra) <= repetidasQueForam.count(letra):
                    marcation[positionMarcation] = "*  "
                else:
                    marcation[positionMarcation] = "/  "
            
            else: marcation[positionMarcation] = "*  "
            
            if letra in letrasRepetidas:
                repetidasQueForam.append(letra)
                
            positionMarcation += 1
            posTermo += 1
            appear += letra + "  "

        
        
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

from random import choice
from time import sleep
class word:
    def __init__(self, word):
        self.word = word
        self.temLetraRepetida = False
        for letra in self.word:
            if self.word.count(letra) > 1:
                self.temLetraRepetida = True
                self.quantidadeRepetidas = self.word.count(letra)
                self.letra_repetida = letra
                break
            else:
                self.quantidadeRepetidas = 0
                self.letra_repetida = 0


def runGame():   
    with open('Tenmo/palavras.txt', 'r', encoding='utf=8') as list_words:
        wordiesInRaw = list_words.readlines()
        global wordsToChoose
        wordsToChoose = []
        wordsWhoutSpace =[]
        for conjunto in wordiesInRaw:
            wordsWhoutSpace += conjunto.split('\n')
        while '' in wordsWhoutSpace:
            wordsWhoutSpace.remove('')
        for conjunto in wordsWhoutSpace:
            wordsToChoose += conjunto.split(':')
        while '' in wordsToChoose:
            wordsToChoose.remove('')
    wordChoosed = word(choice(wordsToChoose))
    wordChoosed = word('TORTO')
    #print(wordChoosed.quantidadeRepetidas)
    print(wordChoosed.word)
    #print(wordChoosed.quantidadeRepetidas)
    print('_  _  _  _  _ \n')
        
   
    
    
    def checkWord(guess):
        quantRep = wordChoosed.quantidadeRepetidas
        appearLetters = ''
        mark = ''
        position = 0
        guessed_it = False
        nao_pode = ['AAAAA', 'EEEEE','IIIII', 'OOOOO', 'UUUUU', 'AEIOU']
        
        while len(guess) < 5 or len(guess) > 5 or guess.upper() in nao_pode:
            print('palavra inválida')
            print('_  _  _  _  _')
            guess = input().upper()
            checkWord(guess)
        
        
        if wordChoosed.temLetraRepetida == True:
            for letra in guess:
                if letra == wordChoosed.letra_repetida and quantRep > 0:
                    if letra == wordChoosed.word[position]:
                        mark += '&  '
                    elif letra in wordChoosed.word and letra != wordChoosed.word[position]:
                        mark += '/  '
                    quantRep -= 1
                    
                    
                elif letra != wordChoosed.letra_repetida:
                    if letra == wordChoosed.word[position] and letra not in appearLetters:
                        mark += '&  '
                    elif letra in wordChoosed.word and letra != wordChoosed.word[position] and letra not in appearLetters: 
                        mark += '/  ' 
                    else: mark += '*  '
                else:
                    mark += '*  '
                position += 1
                appearLetters += letra + '  '.upper()
        
        
        elif wordChoosed.temLetraRepetida == False:
            for letra in guess:
                if letra == wordChoosed.word[position] and letra not in appearLetters:
                        mark += '&  '
                elif letra in wordChoosed.word and letra != wordChoosed.word[position] and letra not in appearLetters: 
                        mark += '/  ' 
                else: mark += '*  '
                
                position += 1
                appearLetters += letra + '  '.upper()      
                    
                    
                                   
       
            
            
        
        
        if mark == '&  &  &  &  &  ':
            guessed_it = True
        print(appearLetters)
        print(mark)
        return guessed_it
    
    
    
    while True:
        guess = word(input().upper())
        guessed = checkWord(guess.word)
        if guessed == True:
            break
    sleep(0.7)
    print("Sensacional! quer jogar denovo? S/N")
    PlayAgain = input().upper()
    if PlayAgain == 'S':
        runGame()
            
print('Do you want to play? S/N')
WantPlay = input().upper()
if WantPlay == 'S':
    print('''Bem vindo ao Tenmo! Dessa vez melhorado ein.
    As regras são simples:''')
    print('-- O simbolo ( & ) indica que a letra está no lugar certo;\n')
    sleep(0.7)
    print('-- O símbolo ( / ) indica que a letra está na palavra, mas na posição errada;\n')
    sleep(0.7)
    print('-- O símbolo ( * ) indica uma letra que não está na palavra.\n')
    sleep(0.7)
    print('Bom jogo e boa sorte!')
    runGame()
else:
    print('Ok, até mais!')



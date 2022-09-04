from time import sleep
from random import choice
class word:
    def __init__(self,word):
        self.word = word
        self.letrasRepetidas = []
        for letra in self.word:
            if self.word.count(letra) > 1:
                self.letrasRepetidas += letra
                
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
    #wordChoosed = word('CASCA')
    #print(wordChoosed.quantidadeRepetidas)
    #print(wordChoosed.word)
    print('_  _  _  _  _ \n')
    
    
    
    def checkWord(guess):
        repetidinhas = list(wordChoosed.letrasRepetidas)
        repetidinhas_usadas = []
        position = 0
        mark = ''
        appearLetters = ''
        guessedIt = False
        
        nao_pode = ['AAAAA', 'EEEEE','IIIII', 'OOOOO', 'UUUUU', 'AEIOU']
        
        while len(guess) < 5 or len(guess) > 5 or guess.upper() in nao_pode:
            print('palavra inválida')
            print('_  _  _  _  _')
            guess = input().upper()
            checkWord(guess)
        
        
        for letra in guess:
            if letra in repetidinhas:
                if letra == wordChoosed.word[position]:
                    mark += '&  '
                elif letra in wordChoosed.word and letra!= wordChoosed.word[position]:
                    mark += '/  '
                repetidinhas.remove(letra)
                repetidinhas_usadas.append(letra)
                
            
            
            elif letra not in repetidinhas:
                if letra == wordChoosed.word[position] and letra not in repetidinhas_usadas:
                    mark += '&  '
                elif letra in wordChoosed.word and letra != wordChoosed.word[position] and letra not in repetidinhas_usadas:
                    mark += '/  '
                else: mark += '*  '
            
            else: mark += '*  '
            
            position += 1
            appearLetters += letra.upper() + '  '
        print(appearLetters)
        print(mark)
        print(repetidinhas)
        if mark =='&  &  &  &  &  ':
            guessedIt = True
        return guessedIt
                
    while True:
        guess = word(input().upper())
        guessed_it = checkWord(guess.word)
        if guessed_it == True:
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
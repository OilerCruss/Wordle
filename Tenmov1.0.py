from random import choice
from time import sleep




def runGame():
    with open ('Tenmo/palavras.txt', 'r', encoding='utf-8') as select_words:
        
        wordiesInRaw = select_words.readlines()
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
        
    tries = 0
    #word_Choosed = 'CINCO'
    word_Choosed = choice(wordsToChoose)
    #print(word_Choosed)
    
    def checking_word(wordie):
        
        position = 0
        mark = ''
        letters = ''
        global guessed_it
        guessed_it = False
        if len(wordie) < 5 or len(wordie) > 5:
            print('_  _  _  _  _  ')
            wordie = input().upper()
        for letrinha in word_Choosed:
            if word_Choosed.count(letrinha) > 1:
                quantLetter = word_Choosed.count(letrinha)
        for letra in wordie:
            if letra == word_Choosed[position]:
                mark +=  '&  '
                
            elif letra in word_Choosed and letra != word_Choosed[position]:
                mark += '/  '
                
            else:
                mark += '-  '
            position += 1
            letters += letra + '  '
            if mark == '&  &  &  &  &  ':
                guessed_it = True

            else:
                guessed_it = False
                    
            
        print(letters)
        print(mark)
        return guessed_it
    
    
    while True:
        word_try = input().upper()
        guess = checking_word(word_try)
        if guess == False:
            tries += 1
            continue
        elif guess == True:
            break
    if tries <= 2:
        sleep(0.5)
        print('\nSensacional!')
    elif tries > 2 and  tries <= 5:
        sleep(0.5)
        print("\nBoa!")
    elif tries > 5:
        sleep(0.5)
        print('\nUfa!')
    print("Você adivinhou!\nQuer jogar denovo? S/N")
    WantToPlayAgain = input().upper()
    if WantToPlayAgain == 'S':
        print('Palavra nova escolhida! Qual será?')
        print('_  _  _  _  _')
        runGame()
    elif WantToPlayAgain == 'N':
        print('ok, até mais')
    
print("Bem vindo ao Tenmo! quer jogar? S/N")
while True:
    WantToPlay = input().upper()
    if WantToPlay == "S":
        print("O jogo funciona da seguinte maneira:\n")
        sleep(1)
        print("O símbolo (&) indica que aquela letra está na palavra e na posição certa.\n")
        sleep(0.7)
        print("O símbolo (/) mostra que a letra existe, mas na posição errada.\n")
        sleep(0.7)
        print("O símbolo (-) indica que aquela letra não existe na palavra.\n")
        sleep(0.7)
        print("Bom jogo e boa sorte!\n")
        print("\n_  _  _  _  _  ")
    
        runGame()
        break
    elif WantToPlay == "N":
        print("Ok, até mais!")
        break
    
    else:
        print('Forma inválida, tente novamente.')

        
          
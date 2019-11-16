def RockPaperScissor():
    playerScore1= 0
    playerScore2= 0
    while True:
        player1 = str(input('Choose wether [rock,paper,scissor]: '))
        player2 = str(input('Choose wether [rock,paper,scissor]: '))
        if player1 == 'rock' and player2 == 'scissor':
            print('player 1 wins')
            playerScore1+=1
        elif player1 == 'scissor' and player2 == 'paper':
            print('player 1 wins')
            playerScore1+=1
        elif player1 == 'paper' and player2 == 'rock':
            print('player 1 wins')
            playerScore1+=1
        elif player2 == 'rock' and player1 == 'scissor':
            print('player 2 wins')
            playerScore2+=1
        elif player2 == 'scissor' and player1 == 'paper':
            print('player 2 wins')
            playerScore2+=1
        elif player2 == 'paper' and player1 == 'rock':
            print('player 2 wins')
            playerScore2+=1
        elif player1 == 'rock' and player2 == 'rock':
            print('Draw')
        elif player1 == 'scissor' and player2 == 'scissor':
            print('Draw')
        elif player1 == 'paper' and player2 == 'paper':
            print('Draw')
        else:
            print('wrong input')

        print('Player 1 score: ',playerScore1)
        print('Player 2 score: ', playerScore2)
        exitGame = str(input('Type \'exit\' if you want to exit: '))
        if exitGame != 'exit':
            continue
        elif exitGame == 'exit':
            break
        
        print('Player 1 score: ',playerScore1)
        print('Player 2 score: ', playerScore2)


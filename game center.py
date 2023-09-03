print("enter your name")
name=input()
print(name+"!"+ "welcome to game centre")

while True:
    print('enter your choice\n 1.tic -toc\n 2.rock\n 3.quiz\n 4.snake game\n other choice to exit ')
    ch=int(input())
    if ch==1:
        squares = [' ']*9
        players = 'XO'
        board = '''
          0   1   2
          {0} | {1} | {2}
         -----------
        3 {3} |{4}  | {5} 5
         -----------
          {6} | {7} | {8}
         6   7   8
        '''
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontals
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # verticals
            (0, 4, 8), (2, 4, 6)             # diagonals
        ]

        def check_win(player):
            for a, b, c in win_conditions:
                if {squares[a], squares[b], squares[c]} == {player}:
                    return True

        while True:
            print(board.format(*squares))
            if check_win(players[1]):
                print(f'{players[1]} is the winner!')
                break
            if ' ' not in squares:
                print('Cats game!')
                break
            move = input(f'{players[0]} to move [0-8] > ')
            if not move.isdigit() or not 0 <= int(move) <= 8 or squares[int(move)] != ' ':
                print('Invalid move!')
                continue
            squares[int(move)], players = players[0], players[::-1]
    elif ch==2:
        choices=['rock','paper','scissors']
        player1=False
        player2=False
        while True:
            player1=input("player1 enter rock,Paper or  Scissors?").capitalize()
            player2=input("player2 enter rock,Paper or  Scissors?").capitalize()
            if player1==player2:
                print("tie!")
            elif player1 == "Rock":
                 if player2 == "Paper":
                    print("player1 You lose!", player2, "covers", player1)
                    print("player2 wins")
                 else:
                    print("player1 You win!", player1, "smashes", player2)
                    print("player2 you lose")
            elif player1 == "Paper":
                if player2 == "Scissors":
                   print("player1 You lose!", player2, "cut", player1)
                   print("player2 you win")
                else:
                   print("player1 You win!", player1, "covers", player2)
                   print("player2 you lose")
            elif player1 == "Scissors":
                if player2 == "Rock":
                   print("player1 You lose...", player2, "smashes", player1)
                   print("player2 you won")
                else:
                    print("player1 You win!", player1, "cut",player2)
                    print("player2 you lose")
                    break
    elif ch==3:
        print(" Welcome To My Quiz Game \n Interesting Game to Play")
        Player = input(" Do you want to play the game? \n" )
        if Player.lower() != 'yes':
           print("Good Bye")
           quit()  

        name_player = input("Enter Your Name: ")

        print("Let's Start the Game :) ",name_player)

        score = 0

        answer = input(' What is CPU stands for? \n ')
        if answer.lower() == 'central processing unit':
            print("Correct")
            score += 1
        else:
            print('Wrong')
 
        answer = input(' What is GPU stands for? \n ')
        if answer.lower() == 'graphical processing unit':
            print("Correct")
            score += 1
        else:
            print('Wrong')

        answer = input(' What is RAM stands for? \n ')
        if answer.lower() == 'random access memory':
           print("Correct")
           score += 1
        else:
            print('Wrong')

        answer = input(' What is ROM stands for? \n ')
        if answer.lower() == 'read only memory':
           print("Correct")
           score += 1
        else:
           print('Wrong')

        answer = input(' Mouse is an input device or output device? \n ')
        if answer.lower() == 'input device':
            print("Correct")
            score += 1
        else:
            print('Wrong')
    
        print("You got the " + str(score)+ " correct answers")
        print("You got the " + str((score/5) *100)+"% ")
    elif ch==4:
        from random import randrange
        from turtle import *

        from freegames import square, vector

        food = vector(0, 0)
        snake = [vector(10, 0)]
        aim = vector(0, -10)


        def change(x, y):
            """Change snake direction."""
            aim.x = x
            aim.y = y


        def inside(head):
            """Return True if head inside boundaries."""
            return -200 < head.x < 190 and -200 < head.y < 190


        def move():
            """Move snake forward one segment."""
            head = snake[-1].copy()
            head.move(aim)

            if not inside(head) or head in snake:
                square(head.x, head.y, 9, 'red')
                update()
                return

            snake.append(head)

            if head == food:
                print('Snake:', len(snake))
                food.x = randrange(-15, 15) * 10
                food.y = randrange(-15, 15) * 10
            else:
                snake.pop(0)

            clear()

            for body in snake:
                square(body.x, body.y, 9, 'black')

            square(food.x, food.y, 9, 'green')
            update()
            ontimer(move, 100)


        setup(420, 420, 370, 0)
        hideturtle()
        tracer(False)
        listen()
        onkey(lambda: change(10, 0), 'Right')
        onkey(lambda: change(-10, 0), 'Left')
        onkey(lambda: change(0, 10), 'Up')
        onkey(lambda: change(0, -10), 'Down')
        move()
        done()

    else:
        exit
            

     

import turtle as t
import random
import time

def turtle_race():
    WIDTH, HEIGHT = 700, 600
    COLORS=["blue", "white", "green", "pink", "yellow", "orange", "purple", "red", "turquoise", "cyan"]


    def _init_turtle(colors):
        screen = t.Screen()
        screen.setup(WIDTH, HEIGHT)
        screen.title("Turtle Racing")
        screen.clear()
        screen.bgcolor("black")
        

        rect = t.Turtle()
        rect.color("black")
        rect.fillcolor("light blue")

        rect.speed(0)
        rect.penup()
        rect.goto(-WIDTH//2,HEIGHT//2-30)
        rect.pendown()

        l = WIDTH
        w = 30

        # drawing first side
        rect.begin_fill()
        rect.forward(l) # Forward turtle by l units
        rect.left(90) # Turn turtle by 90 degree
        rect.forward(w) 
        rect.left(90) 
        rect.forward(l) 
        rect.left(90)
        rect.forward(w) 
        rect.left(90) 
        rect.end_fill()

        write = t.Turtle()
        write.hideturtle()
        write.penup()
        write.setpos(0,HEIGHT//2-40)
        write.pendown()

        
        write.pensize(5)
        write.color('Red')
        style = ('Courier', 30, 'italic')
        write.write('FINISH!', font=style, align='center')
    
     
        #drawing tracks
        """
        space_x =  WIDTH// len(colors)
        for i, color in enumerate(colors):
            player = t.Turtle()
            player.hideturtle()
            player.speed(0)
            player.color("black")
            player.left(90)
            player.penup()
            player.setpos(-WIDTH//2 +(i+1)* space_x, -HEIGHT//2 +20)
            player.pendown()
            player.forward(HEIGHT-50)

             """
    #winning scenery
        
    def win_sit(num):
        write = t.Turtle()
        write.hideturtle()
        write.penup()
        
        write.pendown()

        
        write.pensize(5)
        write.color('Red')
        style = ('Courier', 30, 'italic')
        sentence = "Player no "+ str(num) + "  WON!"
        write.write(sentence, font=style, align='center')
    
    num = 10
    """ def player_no():
        while True:
            num_plr = input("Enter the no of players?(2-10) : ")
            if num_plr.isdigit():
                num= int(num_plr)
                if 1<num<11:
                    return num
                    break
                else:
                    print("Please enter a number between 2 to 10")
                    
            else:
                print("Enter a number! ")
 """
    
    def create_player(colors):
        players = []
        space_x =  WIDTH// (len(colors)+1)

        
        for i, color in enumerate(colors):
            player = t.Turtle()
            player.shape("turtle")
            player.color(color)
            player.left(90)
            player.penup()
            player.setpos(-WIDTH//2 +(i+1)* space_x, -HEIGHT//2 +20)
            player.pendown()
            players.append(player)

        return players

    def race(colors):
        players = create_player(colors)

        while True:
            for player in players:
                distance = random.randrange(1,20)
                player.forward(distance)

                x, y=player.pos()
                if y>= HEIGHT//2 -35:
                    return colors[players.index(player)], players.index(player)+1
    racers= 10
    #racers= player_no()
 



    random.shuffle(COLORS)
    colors = COLORS[:racers]

    _init_turtle(colors) 

    winner = race(colors)
    winner_color = winner[0]
    winner_no = winner[1]
    print("The winner is player no ", winner_no, " with color :", winner_color)
    win_sit(winner_no)
    return winner_no

    time.sleep(5)







# BET Game
def BET_GAME(beter_no):
    def deposit(beter_no):
        dep_amount_list=[]
        for i in range(beter_no):
            while True:
                print("For ", beter_name[i], ": ")
                deposit_amount= input("Enter the amount you want to deposit, $")
                if deposit_amount.isdigit():
                    deposit_amount= int(deposit_amount)
                    if deposit_amount<10:
                        print("Deposit has to greater than $10")
                        
                    else:
                        print("You succesfully deposited $",deposit_amount)
                        dep_amount_list.append(deposit_amount)
                        break
                else:
                    print("Enter amount in digits")
        return dep_amount_list

    def bet_no(beter_no):
        bet_no_list=[]
        for i in range(beter_no):
            while True:
                print("For ", beter_name[i], ": ")
                guess_input = input("Enter the player number you want to bet :")

                if guess_input.isdigit():
                    guess_input= int(guess_input)
                    if 1<=guess_input<=10:
                        print("You betted on player no ", guess_input)
                        bet_no_list.append(guess_input)
                        break
                    else:
                        print("SELECT THE PLAYER FROM 1 to 10, (1-10)")
                        
                else:
                    print("Enter player no in digits 1 to 10")
        return bet_no_list

    def bet_amount(balance, beter_no):
        bet_amount_list=[]
        for i in range(beter_no):
            while True:
                print("For ", beter_name[i], ": ")
                bet_amount= input("Enter the amount you want to bet, $")
                if bet_amount.isdigit():
                    bet_amount= int(bet_amount)
                    if 0<bet_amount<=balance[i]: 
                        print("You betted  $", bet_amount)
                        bet_amount_list.append(bet_amount)
                        break
                    else:
                        print("Your balance is $", balance[i], ". You don't have sufficient balance.")
                        
                else:
                    print("Enter bet amount in digits")

        return bet_amount_list
 
    def game(balance):
        guess_list= bet_no(beter_no)
        amount_list=bet_amount(balance, beter_no)
        player_won= turtle_race() 
    
        current_list = [0] * beter_no
        
        for i in range(beter_no):
            if player_won==guess_list[i]:
                current_list[i] += 2*amount_list[i]
                print("Congrates ", beter_name[i], ". You have won $", 2*amount_list[i])
                
            else:
                current_list[i] -= amount_list[i]
                print("Bad luck!,  ",beter_name[i], ". You lost $", amount_list[i])
                
        return current_list



    def play_again(balance):
        while True:
            ply_agn_inp=input("To play again PRESS Y, to stop PRESS N (Y/N) : ").lower()
            
            if ply_agn_inp=="n":
                for i in range(beter_no):
                    print("Thank you for playing.", beter_name[i], ", your balance is $", balance[i])
                
                break
            elif ply_agn_inp=="y":
                dep_new_list=[]
                for i in range(beter_no):
                    while True:
                        if balance[i]<10:
                            print(beter_name[i], " You don't have sufficient balance to play. Deposit and Play.")

                        deposit_amount_new= input("Enter the amount you want to deposit: $")
                        
                        if deposit_amount_new.isdigit():
                            
                            deposit_amount_new= int(deposit_amount_new)
                            balance[i] += deposit_amount_new
                            print(beter_name[i],"You succesfully deposited $",deposit_amount_new)
                            print(beter_name[i],"Your current balance is $", balance[i])
                            
                            
                            if balance[i]<10:
                                pass
                            else:
                                break
                bet_money_current=game(balance)
                for i in range(beter_no):
                    balance[i] += bet_money_current[i]    
                    print(beter_name[i], ", Your balance is $", balance[i])
                    
                        
            else:
                print("Enter a valid input")
                pass
        return balance
            

    #for 1st round
    balance=[0]*beter_no
    dep_money_ini= deposit(beter_no)
    for i in range(beter_no):
        balance[i] += dep_money_ini[i]

    bet_money =game(balance)
    for i in range(beter_no):
        balance[i] +=bet_money[i]

    for i in range(beter_no):
     print(beter_name[i], ", Your balance $", balance[i])


    while True:   

        balance= play_again(balance)
        
        ply_agn_inp=input("PRESS q to quit : ").lower()
        if ply_agn_inp=="q":
            break


#Rules and player input

print("WELCOME TO TURTLE RACE. YOU CAN BET AND DOUBLE THE MONEY YOU BET. \n There are 8 players and you can bet in any one of them. You can play the bet as a single or group game")

beter_no= int(input("Enter the no of betters(1-4) : "))
beter_name=[]
for i in range(beter_no):
    print("Enter the name of beter no ", i+1)
    name= input(" ").upper()
    beter_name.append(name)



BET_GAME(beter_no)
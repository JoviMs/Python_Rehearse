from textwrap import fill
from tkinter import *
from tkinter import font
from turtle import left

from space_invaders.game_objects import enemy

root = Tk()
root.geometry("600x450")
root.title("space invaders")
canvas = Canvas(root, height=600, width=400, bg='black', highlightthickness=0)
canvas.pack()

#game variables
player_speed = 10
bullet_speed = -15 #movind up
enemy_speed = 2
enemy_direction = 1 #+1 right, -1 left

#list holding the action made by enemies or bullet,keep track
bullets = []
enemies = []

#tracking scores
score = 0
score_label = Label(root, text=f"Score: {score}", font=("Helvetica", 15), bg= 'black', fg='white')
score_label.pack()

#creating player
player = canvas.create_rectangle(275, 360, 325, 380, fill='yellow')

#movement player
def move_player(event):
    x = 0
    #moving left
    if event.keysym == "Left" and canvas.coords(player)[0] > 0:
        x = -player_speed
    elif event.keysym == "Right" and canvas.coords(player)[2] < 600:
        x = player_speed   
    canvas.move(player, x, 0)      

#binding the keyboard
root.bind("<Left>", move_player)
root.bind("<Right>", move_player)  

#creting bullet
def fire_bullet():
    bullet = canvas.create_rectangle(canvas.coords(player)[0] + 22, 350, canvas.coords(player)[2] - 22, 340, fill='red')
    bullets.append(bullet)

root.bind("<space>", lambda event: fire_bullet())    


#creating enemies
def create_enemies():
    for i in range (8):
        for j in range (5):
            enemy = canvas.create_rectangle(50+j*60, 50+i*30, 80+j*60, 80+i*30, fill='green')
            enemies.append(enemy)

#create enemies
create_enemies()

#move_bullet
def move_bullets():
    for bullet in bullets:
        canvas.move(bullet, 0, bullet_speed)
        if canvas.coords(bullet)[1] < 0:
            canvas.delete(bullet)
            bullets.remove(bullet)

#moving enemies
def move_enemies():
    global enemy_direction
    edge_reach = False

    for enemy in enemies:
        canvas.move(enemy, enemy_speed * enemy_direction, 0)
        #getting direction
        x1,y1,x2,y2 = canvas.coords(enemy)
#checking eneemy reach edge
        if x2 >= 400 or x1 <= 0:
            edge_reach = True
            #if edge reach, move enemy down and different direction
    if edge_reach:
        enemy_direction *= -1
                #move enemies down
        for enemy in enemies:
            canvas.move(enemy, 0, 20)


def check_collision():
    global score
    for bullet in bullets:
        bullet_coords = canvas.coords(bullet)
#get enemieas
        for enemy in enemies:
            enemy_coords = canvas.coords(enemy)
        #check if bullet and enemy overlap
        #x1,y1,x2,y2
            if (bullet_coords[2] > enemy_coords[0] and bullet_coords[0] < enemy_coords[2] and
                bullet_coords[3] > enemy_coords[1] and bullet_coords[1] < enemy_coords[3]):
           #remove bullet and enemy collsion
                    canvas.delete(bullet)
                    canvas.delete(enemy)
           #remove from list
                    bullets.remove(bullet)
                    enemies.remove(enemy)
           #update scores

                    score += 10
                    score_label.config(text=f"Score: {score}")
                    break
               


#game loop
def game_loop():
    move_enemies()
    move_bullets()
    check_collision()
#check if enemy reach player(ganeover)
    for enemy in enemies:
        if canvas.coords(enemy)[3] >= 360:
            canvas.create_text(300,200, text='GAME OVER', fill='white', font=("Helvetica", 15))
            return

    #set game speed
    root.after(50, game_loop) #delay

game_loop()
root.mainloop()
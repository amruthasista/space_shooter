import pygame
import random
import sys

#initialize pygame
pygame.init()

#set screen up
WIDTH,HEIGHT=600,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Shooter')

#colours
WHITE=(255,255,255)
RED=(255,0,0)

#clock
clock=pygame.time.Clock()
FPS=60

#load spaceship
player_img=pygame.Surface((50,40))
player_img.fill(WHITE)
player_x=WIDTH//2-25
player_y=HEIGHT-60
player_speed=5

#bullet
bullet_img=pygame.Surface((5,10))
bullet_img.fill(RED)
bullets=[]
bullet_speed=7

#enemy
enemy_img=pygame.Surface((40,30))
enemy_img.fill((0,255,0))
enemies=[]
enemy_speed=3
enemy_spawn_delay=30
enemy_timer=0

#score
score=0
font=pygame.font.SysFont(None,30)

#function to draw text
def draw_text(text,x,y):
    img=font.render(text,True,WHITE)
    screen.blit(img,(x,y))

#main loop
running=True
while running:
    clock.tick(FPS)
    screen.fill((0,0,0))

    #events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

#keys
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x>0:
        player_x-=player_speed
    if keys[pygame.K_RIGHT] and player_x<WIDTH-50:
        player_x+=player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets)<5:
            bullets.append([player_x+22,player_y])

    #update bullets
    for bullet in bullets[:]:
        bullet[1]-=bullet_speed
        if bullet[1]<0:
            bullets.remove(bullet)

    #spawn enemies
    enemy_timer+=1
    if enemy_timer>enemy_spawn_delay:
        enemy_x=random.randint(0,WIDTH-40)
        enemies.append([enemy_x,0])
        enemy_timer=0

    #update enemies
    for enemy in enemies[:]:
        enemy[1]+=enemy_speed
        if enemy[1]>HEIGHT:
            enemies.remove(enemy)

    #collision detection
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (
                bullet[0]in range(enemy[0],enemy[0]+40)
                and bullet[1]in range(enemy[1],enemy[1]+30)
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score+=1
                break

    #draw player
    screen.blit(player_img,(player_x,player_y))

    #draw bullets
    for bullet in bullets:
        screen.blit(bullet_img,(bullet[0],bullet[1]))

    #draw enemies
    for enemy in enemies:
        screen.blit(enemy_img,(enemy[0],enemy[1]))

    #draw score
    draw_text(f"Score:{score}",10,10)

    pygame.display.update()

pygame.quit()
sys.exit()
import pygame
import math
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Floating Balls")
display_width = 1400
display_height = 800
won = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Our Game')
nn = 2

rB = [] #радиус
mB = [] #масса
xB = [] #координата x
yB = [] #координата y
aB = [] #направление
vB = [] #скорость
cB = [] #color

for i in range(nn + 1):
    rB.append(50 * 1)
    mB.append(rB[i] ** 2)
    xB.append(i * 400)
    yB.append(display_height // 2)
    aB.append(i * math.pi /3)
    vB.append (2)
    cB.append(0)

cB[1] = (255, 0, 0)
cB[2] = (0, 255, 0)

var = True
while var:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var = False

    won.fill((0, 0, 0))

    for i in range(1, nn + 1):
        xB[i] += vB[i] * math.cos(aB[i])
        yB[i] += vB[i] * math.sin(aB[i])
        pygame.draw.circle(won, cB[i], (xB[i], yB[i]), rB[i])

    pygame.time.delay(10)
    pygame.display.update()

    #проверка на столкновение stenami
    for i in range(1, nn +1):
        if xB[i] <= rB[i] and (aB[i] > math.pi / 2 or aB[1] < -math.pi / 2):
            aB[i] = math.pi - aB[i]
        if xB[i] >= display_width -rB[i] and (aB[i] > math.pi / 2 or aB[i] < -math.pi / 2):
            aB[i] = math.pi - aB[i]
        if yB[i] <= rB[i] and (aB[i] < 0 and aB[i] > -math.pi):
            aB[i] = -aB[i]
        if yB[i] >= display_height - rB[i] and (aB[i] > 0 and aB[i] < math.pi):
            aB[i] = -aB[i]
        while aB[i] > math.pi: aB[i] -= 2* math.pi
        while aB[i] < - math.pi: aB[i] +=2 * math.pi
    #stolknovenie s bals
    for i in range(1, nn + 1):
        for j in range(i + 1, nn + 1):
            #rasstoyanie meshdu balls:
            Rast = ((xB[i] - xB[j]) ** 2 + (yB[i] - yB[j]) ** 2) ** 0.5
            if Rast <= rB[i] + rB[j]:
                xB1new = xB[i] + vB[i] * math.cos(aB[i])
                yBn1ew = yB[i] + vB[i] * math.sin(aB[i])
                xB2new = xB[j] + vB[j] * math.cos(aB[i])
                yB2new = xB[j] + vB[j] * math.cos(aB[i])

                RastNew = ((xB1new - xB2new) **2 + (yBn1ew - yB2new) **2) **0.5
                if Rast > RastNew:
                    BB = math.atan((yB[j] - yB[i])/(xB[j] - xB[i]))
                    if (xB[j] - xB[i]) < 0:
                        BB += math.pi
                        while BB > math.pi / 2: BB -= 2 * math.pi
                        while BB < - math.pi / 2: BB += 2 * math.pi
                    W1 = aB[i] - BB
                    W2 = aB[j] - BB

                    Vw1 = vB[i] * math.cos(W1)
                    Vw2 = vB[j] * math.cos(W2)
                    Vwt1 = vB[j] * math.sin(W1)
                    Vwt2 = vB[j] * math.sin(W2)

                    Vw1 = (2 * mB[j] * vB[j] * math.cos(W2)) + (mB[i] - mB[j] * vB[i] * math.cos(W1)) / (mB[i] + mB[j])
                    Vw2 = (2 * mB[i] * vB[i] * math.cos(W1)) + (mB[j] - mB[i] * vB[j] * math.cos(W2)) / (mB[i] + mB[j])

                    vB[i] = (Vw1** 2 + Vwt1 **2)**0.5
                    vB[j] = (Vw2** 2 + Vwt2 **2)**0.5

                    W1 = math.atan(Vwt1/Vw1)
                    if Vw1 <0: W1 += math.pi
                    W2 = math.atan(Vwt2/Vw2)
                    if Vw2 <0: W2 += math.pi

                    aB[i] = BB +W1
                    while aB[i] > math.pi : aB[i] -=2 * math.pi
                    while aB[i] < - math.pi : aB[i] +=2 * math.pi
                    aB[j] = BB + W2
                    while aB[j] > math.pi : aB[j] -=2 * math.pi
                    while aB[j] < - math.pi : aB[j] +=2 * math.pi



pygame.quit()

#def event_handler():
 #   for event in pygame.event.get():
  #      if event.type == QUIT or (
   #         event.type == KEYDOWN and (
    #        event.key == K_ESCAPE or
     #       event.key == K_q
      #      )):
       #     pygame.quit()
        #    quit()
#while True:
 #   event_handler()
  #  pygame.display.update()
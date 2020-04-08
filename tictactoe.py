import pygame as pg
pg.init()
dis = pg.display.set_mode((600, 300))
pg.display.update()
pg.display.set_caption('TicTacToe')
game_over = False
pg.draw.line(dis, (255, 255, 255), (200, 0), (200, 300), 2)
pg.draw.line(dis, (255, 255, 255), (400, 0), (400, 300), 2)
pg.draw.line(dis, (255, 255, 255), (0, 100), (600, 100), 2)
pg.draw.line(dis, (255, 255, 255), (0, 200), (600,200), 2)
pg.display.update()
chance=1
font = pg.font.SysFont("comicsansms", 72)
text = font.render("X", True, (255, 0, 0))
text1 = font.render("O", True, (255, 0, 0))
marked={}
while not game_over:
    for x in pg.event.get():
        if x.type == pg.QUIT:
            game_over = True
            break
        if x.type==pg.MOUSEBUTTONUP:
            pos0,pos1=pg.mouse.get_pos()
            idx=(pos0//200,pos1//100)
            if idx not in marked:
                marked[idx]=1
                if chance:
                    dis.blit(text1,(idx[0]*200+70,idx[1]*100))
                else:
                    dis.blit(text,(idx[0]*200+70,idx[1]*100))
                chance=not chance
            pg.display.update()
            print(chance,marked)
pg.quit()
quit()
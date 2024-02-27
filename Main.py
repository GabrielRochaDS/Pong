from PPlay.window import *
from PPlay.sprite import *
from pplay.keyboard import Keyboard


#criando as imagens e a janela
janela = Window(720, 560)
janela.set_title("Gabriel Rocha - Pong")
ball = Sprite("Game_assets/ball.png", 1)
restart = Sprite("Game_assets/restart.png")
mouse = Window.get_mouse()

#posicionando a bolinha no centro
ball.set_position(janela.width/2 - ball.width/2,janela.height/2 - ball.height/2)
pad1 = Sprite("Game_assets/pad1.png", 1)
pad2 = Sprite("Game_assets/pad1.png", 1)
#posicionando os pads
pad1.set_position(20,(janela.height-pad1.height)/2)
pad2.set_position(janela.width-pad1.width-20,(janela.height-pad1.height)/2)
teclado = Window.get_keyboard()
#pontuação 1 e pontuação 2
pt1 = 0
pt2 = 0
#icone de restart
restart.set_position(janela.width/2-restart.width/2, janela.height/2 - restart.height/2 + 2*ball.height)
#movimentos do pad e bola
movimentopad = 500
movimentox = 0
movimentoy = 0


while(True):
    #fisica da bolinha somente no eixo y
    if ball.y <= 0 or ball.y >= (janela.height - ball.height):
        movimentoy = - movimentoy
        ball.y = ball.y + movimentoy/125                          #movimento empurrando a bolinha para impedir dela sair
    ball.y = ball.y + movimentoy * janela.delta_time()
    ball.x = ball.x + movimentox * janela.delta_time()
    
    #movendo os pads com imput do teclado
    if(teclado.key_pressed("W") and (pad1.y >=0)):
        pad1.y = pad1.y + (-movimentopad*janela.delta_time())
    elif(teclado.key_pressed("S") and (pad1.y <= janela.height -pad1.height)):
        pad1.y = pad1.y + movimentopad*janela.delta_time()
    elif(teclado.key_pressed("UP") and (pad1.y >=0)):
        pad1.y = pad1.y + (-movimentopad*janela.delta_time())
    elif(teclado.key_pressed("DOWN") and (pad1.y <= janela.height -pad1.height)):
        pad1.y = pad1.y + movimentopad*janela.delta_time()
    # Ia do pad    
    if ball.y -36 < (pad2.y + pad2.height/2) and movimentox>0:
        pad2.y = pad2.y + (-movimentopad*janela.delta_time())
    if ball.y +36 > (pad2.y + pad2.height/2) and movimentox>0:
        pad2.y = pad2.y + (movimentopad*janela.delta_time())

    #colisão bolinha e pad1
    if(ball.collided(pad1)) and ball.x > pad1.x:
        movimentox = -movimentox
        ball.x = ball.x + movimentox/500
        #movimento da bolinha de acordo com a posição de impacto com o pad /// modificação pessoal do Pong
    
    #colisão bolinha e pad2
    if(ball.collided(pad2)) and ball.x  < pad2.x:
        movimentox = -movimentox
        ball.x = ball.x + movimentox/500
        
    
    #reposicionando a bolinha no centro quando o jogo acaba 
    if(ball.x+ball.width+40<0 or ball.x-40>janela.width):
        if (ball.x<0):
            pt2+=1
        elif (ball.x>janela.width):
            pt1+=1
        ball.set_position(janela.width/2 - ball.width/2,janela.height/2 - ball.height/2)
        movimentox = 0
        movimentoy = 0
    
    
    #jogo continua quando a tecla de reinicio é apertada
    if(teclado.key_pressed("enter") and movimentox == 0):
        jogo_comecou = False
        movimentox = 500
        movimentoy = 500

    #desenhando as imagens
    janela.set_background_color((0, 0, 0))
    if movimentox==0 and movimentoy==0:
        restart.draw()

    janela.draw_text(str(pt1)+" X "+str(pt2), (janela.width/2.21), 10, size=30, color=(255,255,255))
    pad1.draw()
    pad2.draw()
    ball.draw()
    janela.update()
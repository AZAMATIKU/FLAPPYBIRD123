import pygame, random

pygame.init()

window = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

#звгружаем картинки
fon = pygame.image.load('images/background.png')
base = pygame.image.load('images/base.png')
bird = pygame.image.load('images/bluebird.png')
bird_rect = bird.get_rect(center = (50 ,256))
pipe = pygame.image.load('images/pipe.png')
pipe_flip = pygame.transform.flip(pipe, False, True)
message = pygame.image.load('images/message.png')
message_rect = message.get_rect(center = (144,256))


#загружаем звуки
die = pygame.mixer.Sound('sounds/die.wav')
hit = pygame.mixer.Sound('sounds/hit.wav')
wing = pygame.mixer.Sound('sounds/wing.wav')
point = pygame.mixer.Sound('sounds/point.wav')

pygame.mixer.music.load('sounds/.mp3')
pygame.mixer.music.play()
#ПЕРЕМЕННЫЕ
base_x = 0
gravity = 0.2
speed = 0   
pipe_x = 300
pipe_y = 350
game_active = False
score = 0


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            quit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE and game_active:
                wing.play()
                speed = 0
                speed -= 5
            if i.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_x = 300
                speed = 0
                bird_rect.center = (50 ,256)
                score = 0

    window.blit(fon, (0,0))
    if game_active:
        #птичка
        bird_flip = pygame.transform.rotozoom(bird, -speed*4.5, 1)
        window.blit(bird_flip, bird_rect)
        speed += gravity
        bird_rect.centery += speed

        #трубы
        pipe_rect = pipe.get_rect(midtop = (pipe_x,pipe_y))
        window.blit(pipe, pipe_rect)
        
        

        pipe_flip_rect = pipe_flip.get_rect(midbottom = (pipe_x, pipe_y - 150))
        window.blit(pipe_flip,pipe_flip_rect)

        pipe_x -= 2
        if pipe_x <= -50:
            pipe_x = 300
            pipe_y = random.randint(200,400)

        #проверка столкновений
        if bird_rect.colliderect(pipe_rect) or bird_rect.colliderect(pipe_flip_rect):
            game_active = False
            hit.play()
        if bird_rect.top <= 0 or bird_rect.bottom >= 450:
            game_active = False
            die.play()
        if pipe_rect.centerx == 50:
            score += 1
            point.play()
            

               
    else:
        window.blit(message, message_rect)

    font =pygame.font.Font('04B_19.TTF', 40)
    text = font.render(str(score), True, (255,255,255))
    window.blit(text, (130,30))



    #отрисовка пола
    window.blit(base, (base_x ,450))
    base_x -= 1
    if base_x <= -30:
        base_x = 0
    

    

    pygame.display.update()
    clock.tick(120)
    


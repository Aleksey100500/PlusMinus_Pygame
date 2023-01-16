import pygame
import sys

def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0:
        return 'Piece'
    return False

pygame.init()
size_block = 200 # размер блока
margin = 30 # размер отступа в свободных местах
width = heigth = size_block * 3 + margin * 4 # 3 блока + 4 отступа = размер нашего окна в игре

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-нолики")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)] # массив заполненный нулями, один 0 оначает, что клетка пустая
query = 0 # 1 2 3 4 5
game_over = False

while True:
    for event in pygame.event.get(): # цикл обработки событий
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos() # берем позицию нажатия кнопки мыши на квадрат
            col = x_mouse // (size_block + margin)
            row = y_mouse// (size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)
            

    if not game_over:
        for row in range(3): # вложенный цикл
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white

                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 5,y + 5), (x + size_block - 5, y + size_block - 5), 3)
                    pygame.draw.line(screen, white, (x + size_block - 5,y + 5), (x + 5, y + size_block - 5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block / 2 - 3, 3)
    
    if (query - 1)% 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(black) # закрашиваем окно целиком черным цветом
        font = pygame.font.SysFont('stxingkai', 80) # создаем шрифт
        text1 = font.render(game_over, True, white) # шрифт будет содержать текст game_over - либо о, либо piece
        text_rect = text1.get_rect() # узнаем его координаты
        text_x = screen.get_width() / 2 - text_rect.width / 2   # эта и строчка ниже находят центр нашего окна, чтобы текст располагался ровно по центру
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y]) # прикрепляет текст по найденным координатам
    pygame.display.update()
# Khai báo các thư viện
import pygame
import random
import time

# Kích cỡ của cửa sổ game khi chạy
window_x = 720
window_y = 480

# Tốc độ của rắn
snake_speed = 12

# Định nghĩa các màu sắc
green = pygame.Color(3, 171, 12)
orange = pygame.Color(247, 114, 5)
pink = pygame.Color(240, 170, 234)
white = pygame.Color(255, 255, 255)

# Khởi tạo pygame
pygame.init()

# Khởi tạo cửa sổ game
pygame.display.set_caption('Green Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

# Bộ điều khiển FPS giúp theo dõi thời gian
fps = pygame.time.Clock()

# Vị trí mặc định của Rắn
snake_position = [70, 270]

# Mặc định chiều dài của rắn là 3
snake_body = [[70,270], [60,270], [50,270]]
            
# Vị trí thức ăn
food_position = [random.randrange(12, (window_x//10)) * 10,
                random.randrange(3, (window_y//10)) * 10]
        
produce_food = True

# Mặc định hướng đi lúc ban đầu của con rắn
# Bên Phải
direction = 'RIGHT'
change_to = direction

# Điểm số lúc ban đầu
score = 0

# Chức năng hiển thị điểm số
def show_score(choice, color, font, size):

    # Thiết lập phông chữ cho thông báo điểm
    score_font = pygame.font.SysFont(font, size)
    
    # Viết dòng thông báo điểm
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # Tạo khối hcn cho điểm
    score_rect = score_surface.get_rect()
    
    # Hiển thị điểm
    game_window.blit(score_surface, score_rect)

# Hàm kết thúc game
def game_over():
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                    pygame.quit()   
                    quit()

# Hàm main
while True:
    
    # Xử lý sự kiện của các phím di chuyển
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Hướng di chuyển hiện tại và hướng phím input không đc đối nhau
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Hướng di chuyển ứng với vị trí mới của rắn
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Rắn sẽ lớn thêm 1 khi ăn thức ăn
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        produce_food = False

    else:
        snake_body.pop()
        
    if not produce_food:
        while True:
            food_position = [random.randrange(12, (window_x//10)) * 10,
                        random.randrange(3, (window_y//10)) * 10]
            if food_position[0] != snake_position[0] or food_position[1] != snake_position[1]:
                break

        
    produce_food = True
    game_window.fill(pink)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                        pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, orange, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

    # Kết thúc game nếu chạm vào 4 cạnh của cửa sổ
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()

    # Kết thúc game nếu rắn chạm vào chính nó
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Hiển thị và cập nhật điểm số ở góc trái trên màn hình
    show_score(1, white, 'Jumble', 40)

    # Cập nhật lại nội dung toàn màn hình game
    pygame.display.flip()

    # Thiết lập tốc độ rắn thông qua thời gian chuyển khung hình 
    fps.tick(snake_speed)

import pygame
import time
import random

pygame.init()

orange = pygame.Color(247, 114, 5)
game= pygame.display.set_mode((720,480))
game.fill((255,255,255))

x = [[120,50], [110,50], [100,50]]

for pos in x:   
    pygame.draw.rect(game, orange, pygame.Rect(pos[0],pos[1],10,10))


# Kích cỡ của cửa sổ game khi chạy
window_x = 720
window_y = 480

# Định nghĩa các màu sắc
green = pygame.Color(3, 171, 12)
orange = pygame.Color(247, 114, 5)
pink = pygame.Color(240, 170, 234)

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
        
game_window.fill(pink)

for pos in snake_body:
    pygame.draw.rect(game_window, green,
                        pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, orange, pygame.Rect(
        food_position[0], food_position[1], 10, 10))

# Cập nhật lại nội dung toàn màn hình game
pygame.display.flip()

time.sleep(5)
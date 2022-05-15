# Khai báo các thư viện
import pygame
import random
import time

# Kích cỡ của cửa sổ game khi chạy
window_x = 720
window_y = 480

# Định nghĩa các màu sắc
green = pygame.Color(3, 171, 12)
orange = pygame.Color(247, 114, 5)
pink = pygame.Color(240, 170, 234)

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
snake_body = [[70, 270], [60, 270], [50, 270]]

# Vị trí thức ăn
food_position = [random.randrange(12, (window_x // 10)) * 10,
                 random.randrange(3, (window_y // 10)) * 10]

# Mặc định hướng đi lúc ban đầu của con rắn
# Bên Phải
direction = 'RIGHT'

# Hàm main
while True:

    if direction == 'RIGHT':
        snake_position[0] += 10



    # Cập nhật lại nội dung toàn màn hình game
    pygame.display.flip()

    # Thiết lập tốc độ rắn thông qua thời gian chuyển khung hình 
    fps.tick(12)

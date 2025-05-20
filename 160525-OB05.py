import pygame
import random
import os
import sys

# Настройки
WIDTH, HEIGHT = 1600, 1000
F   PS = 60

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Космический шутер")
clock = pygame.time.Clock()

# Цвета (для заглушек)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Путь к папке с ассетами
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

def load_image(name, scale=1):
    """Загрузка изображения с обработкой ошибок"""
    try:
        image = pygame.image.load(os.path.join(ASSETS_DIR, name))
        if scale != 1:
            size = (int(image.get_width() * scale), int(image.get_height() * scale))
            image = pygame.transform.scale(image, size)
        return image.convert_alpha()
    except Exception as e:
        print(f"Ошибка загрузки {name}: {e}")
        # Создаём заглушку
        surf = pygame.Surface((50, 50), pygame.SRCALPHA)
        color = RED if "enemy" in name else (0, 255, 0) if "player" in name else (0, 0, 255)
        surf.fill(color)
        return surf

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("player_ship.png", 0.5)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed = 8
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            Bullet(self.rect.centerx, self.rect.top)

# Класс врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("enemy_ship.png", 0.4)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 5)

# Класс пуль
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image("bullet.png", 0.3)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
        all_sprites.add(self)
        bullets.add(self)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

# Загрузка фона
try:
    background = load_image("space_bg.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except:
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(BLACK)

# Создание групп спрайтов
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Создание игрока
player = Player()
all_sprites.add(player)

# Создание врагов
for _ in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Счётчик очков
score = 0
font = pygame.font.SysFont('Arial', 28)

# Игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Обновление
    all_sprites.update()

    # Проверка столкновений
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for _ in hits:
        score += 10
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    if pygame.sprite.spritecollide(player, enemies, False):
        running = False

    # Отрисовка
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    screen.blit(font.render(f"Очки: {score}", True, WHITE), (10, 10))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
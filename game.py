import pygame
import os
pygame.init()
ширина = 800
высота = 600
окно = pygame.display.set_mode((ширина,высота),pygame.FULLSCREEN)
папка_кадров = "главное_меню"
главное_меню_фон = []
for i in range(0,59):
  путь = os.path.join(папка_кадров,f"frame_{i}_delay-0.03s.gif")
  главное_меню_фон_изображение = pygame.image.load(путь)
  главное_меню_фон_размер = pygame.transform.scale(главное_меню_фон_изображение,(ширина,высота))
  главное_меню_фон.append(главное_меню_фон_изображение)
номер_кадра = 0 
таймер = pygame.time.get_ticks()
скорость_анимации = 100
главное_меню_фон_работает = True
while главное_меню_фон_работает:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      главное_меню_фон_работает = False
    if pygame.time.get_ticks() - таймер > скорость_анимации:
      таймер = pygame.time.get_ticks()
      номер_кадра = (номер_кадра + 1) % len(гланое_меню_фон)
  окно.fill((0,0,0))
  окно.blit(главное_меню_фон[номер_кадра],(0,0))
  pygame.display.update()
pygame.quit()
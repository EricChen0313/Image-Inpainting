import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import torch
import pygame
import sys
from evaluation import EvaluateSingle
from net import PConvUNet
from util.io import load_ckpt

pygame.init()
width, height = 512, 512
size = (256, 256)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mask Creator")
background_image = pygame.image.load('input.jpg')
background_image = pygame.transform.scale(background_image, (512, 512))
black = (0, 0, 0)
white = (255, 255, 255)
lines = []
DRAW = False
last_pos = (0, 0)
pen_width = 5
device = torch.device('cpu')
model = PConvUNet().to(device)
load_ckpt('1000000.pth', [('model', model)])
model.eval()

print("Press S To Save the Mask.")
print("Default Pen Size is :  5")
screen.blit(background_image, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:      # PRESSED X
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: # IF PRESSED 
            if event.key == pygame.K_s:    # PRESSED S
                white_background = pygame.Surface((width, height))
                white_background.fill(white)

                for line in lines:
                    pygame.draw.line(white_background, black, line[0], line[1], line[2])

                pygame.image.save(white_background, "Mask.jpg")
                print("Mask Saved.")
                pygame.quit()
                EvaluateSingle(model, size, 'input.jpg', 'Mask.jpg', device)
                sys.exit()
            elif event.key == pygame.K_d:
                pen_width += 5
                print(f"Current Pen Size is : {pen_width}")
            elif event.key == pygame.K_a:
                pen_width = max(1, pen_width - 5)
                print(f"Current Pen Size is : {pen_width}")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            DRAW = True

        elif event.type == pygame.MOUSEBUTTONUP:
            DRAW = False
            last_pos = (0, 0)

        elif event.type == pygame.MOUSEMOTION and DRAW:
            current_pos = pygame.mouse.get_pos()
            if last_pos != (0, 0):
                pygame.draw.line(screen, black, last_pos, current_pos, pen_width)
                pygame.display.flip()
                lines.append((last_pos, current_pos, pen_width))
            last_pos = current_pos

    pygame.display.flip()

'''
Author:
	Charles
Function:
	상자 미는 사람
'''
	Author:
		Charles
	Function:
		상자 미는 사람
	닉네임:
		Charles의 피카츄
	'''
import os
import pygame
from config import Config
	

	

'''
Function:
	상자를 미는 사람
'''
class pusherSprite(pygame.sprite.Sprite):
	def __init__(self, col, row):
		pygame.sprite.Sprite.__init__(self)
		self.image_path = os.path.join(Config.get('resources_path'), Config.get('imgfolder'), 'player.png')
		self.image = pygame.image.load(self.image_path).convert()
		color = self.image.get_at((0, 0))
		self.image.set_colorkey(color, pygame.RLEACCEL)
		self.rect = self.image.get_rect()
		self.col = col
		self.row = row
	'''이동'''
	def move(self, direction, is_test=False):
		# 테스트 모드는 아날로그 이동을 대표함
		if is_test:
			if direction == 'up':
				return self.col, self.row - 1
			elif direction == 'down':
				return self.col, self.row + 1
			elif direction == 'left':
				return self.col - 1, self.row
			elif direction == 'right':
				return self.col + 1, self.row
		else:
			if direction == 'up':
				self.row -= 1
			elif direction == 'down':
				self.row += 1
			elif direction == 'left':
				self.col -= 1
			elif direction == 'right':
				self.col += 1
	'''인물을 게임에 그림'''
	def draw(self, screen):
		self.rect.x = self.rect.width * self.col
		self.rect.y = self.rect.height * self.row
		screen.blit(self.image, self.rect)
	

	

'''
Function:
	상자를 미는 사람 요소
'''
class elementSprite(pygame.sprite.Sprite):
	def __init__(self, sprite_name, col, row):
		pygame.sprite.Sprite.__init__(self)
		# 도입box.png/target.png/wall.png
		self.image_path = os.path.join(Config.get('resources_path'), Config.get('imgfolder'), sprite_name)
		self.image = pygame.image.load(self.image_path).convert()
		color = self.image.get_at((0, 0))
		self.image.set_colorkey(color, pygame.RLEACCEL)
		self.rect = self.image.get_rect()
		# 사람 유형
		self.sprite_type = sprite_name.split('.')[0]
			# 사람 위치
		self.col = col
		self.row = row
	'''게임 요소를 게임에 그림'''
	def draw(self, screen):
		self.rect.x = self.rect.width * self.col
		self.rect.y = self.rect.height * self.row
		screen.blit(self.image, self.rect)
	'''모바일 게임 원소'''
	def move(self, direction, is_test=False):
		if self.sprite_type == 'box':
			# 테스트 모드는 아날로그 이동을 대표함
			if is_test:
				if direction == 'up':
					return self.col, self.row - 1
				elif direction == 'down':
					return self.col, self.row + 1
				elif direction == 'left':
					return self.col - 1, self.row
				elif direction == 'right':
					return self.col + 1, self.row
			else:
				if direction == 'up':
					self.row -= 1
				elif direction == 'down':
					self.row += 1
				elif direction == 'left':
					self.col -= 1
				elif direction == 'right':
					self.col += 1


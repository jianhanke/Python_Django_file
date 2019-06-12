import sys
import pygame

from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_settings=Settings()  #实例化，设置类 
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion") 
	play_button=Button(ai_settings,screen,"Play")
	stats=GameStats(ai_settings)
	sb=Scoreboard(ai_settings,screen,stats)
	ship=Ship(ai_settings,screen)
	bullets=Group()
	aliens=Group() 
	gf.create_fleet(ai_settings,screen,aliens,ship)
	
	while True:  
			gf.ckeck_event(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb)
			if stats.game_active:
				ship.update()
				gf.update_bullets(ai_settings,screen,ship,aliens,bullets,sb,stats)
				gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets,sb)
			gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button,sb)	
run_game()
  
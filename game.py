"""
Chapitre 11.3

Fonctions pour simuler un combat.
"""


import random
import time
import utils
from character import *
from magician import *
class Spell(Weapon):
	def __init__(self,name, power, min_level, mana_cost):
		super().__init__(name,power,min_level)
		self.mana = mana_cost
fire_ball = Spell("Fire Ball", 55, 11,22)
ice_spike = Spell("Ice Spike", 55, 11,17)
dagger = Weapon("Crucifix Dagger", 12, 0)
class Mages(Character):
	def __init__(self,name, max_hp, attack, defense, level, mana_pool, intelligence, use_spell, mp_left, spells,melee):
		super().__init__(name, max_hp, attack, defense, level)
		self.mana_p = mana_pool
		self.int = intelligence
		self.use_spell = use_spell
		self.mp_left = mp_left
		self.spell = spells
		self.melee = melee
mage_1 = Mages("Tolfdir",50,75,150,20, 80, 25, 25, 80, fire_ball,dagger)
mage_2 = Mages("Savos Aren",50,75,150,20,80, 25, 25, 80, ice_spike,dagger)

def deal_damage(attacker, defender):
	rng = (random.randint(85, 100)) / 100
	if random.randint(1,16) == 16:
		crit = 1.5
	elif random.randint(1,8) == 8:
		crit = 1.5
	else:
		crit =1
	modifier = crit * rng

	if random.randint(23,30) > attacker.use_spell:
		damage = int(((((((2*attacker.level+attacker.int)/5)+2)*attacker.spell.power) *1/50)+2)*modifier)
		print(attacker.name + " dealt " + str(int(damage)) + " damage with " + str(attacker.spell.name))
		print("\t" + defender.name + " has " + str(int(defender.max_hp - damage)) + " HP left.")
		print("\n")
	else:
		damage = int((((((2 * attacker.level / 5) + 2) * attacker.weapon.power * (attacker.attack / defender.defense)) / 50) + 2) * modifier)
		print(attacker.name + " dealt " + str(int(damage)) + " damage with " + str(attacker.melee.name))
		print("\t" + defender.name + " has " + str(int(defender.max_hp - damage)) + " HP left.")
		print("\n")
	defender.max_hp -= damage


def run_battle(c1, c2):
	print("Warriors, begin! \n")
	c=0
	if random.randint(1,2) ==1:
		while c1.max_hp >=0:
			if c2.max_hp >= 0:
				deal_damage(c1,c2)
				deal_damage(c2,c1)
				c+=1
				if c1.max_hp <= 0:
					print(c1.name + " died in " + str(c) + " turns")
					break
				elif c2.max_hp <= 0:
					print(c2.name + " died in " + str(c) + " turns")
					break
	else:
		while c1.max_hp > 0 or c2.max_hp > 0:
			if c2.max_hp >= 0:
				deal_damage(c2,c1)
				deal_damage(c1,c2)
				c+=1
				if c1.max_hp <= 0:
					print(c1.name + " died in " + str(c) + " turns")
					break
				elif c2.max_hp <= 0:
					print(c2.name + " died in " + str(c) + " turns")
					break

if __name__ == "__main__":
	# deal_damage(mage_1,mage_2)
	run_battle(mage_1,mage_2)
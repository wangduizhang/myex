#!/usr/bin/python
#_*_coding:utf-8_*_
#面向对象编程
class Spell(object):
	def __init__(self, incantation, name):
		self.name = name
		self.incantation = incantation

	def __str__(self):
		return self.name + ' ' + self.incantation + '\n' + self.getDescription()
		  
	def getDescription(self):
		return 'No description'

	def execute(self):
		print self.incantation    


class Accio(Spell):
	def __init__(self):
		Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
	def __init__(self):
		Spell.__init__(self, 'Confundo', 'Confundus Charm')

	def getDescription(self):
		return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
	print spell

spell = Accio()
spell.execute()
print ('- - ') * 10
studySpell(spell)
print ('- - ') * 10
studySpell(Confundo())


#如何修改accio,使它输出：
'''
Summoning Charm Accio
This charm summons an object to the caster, potentially over a significant distance.
'''
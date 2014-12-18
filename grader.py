from __future__ import division
import re

extra_credit = {"hw1": [], "hw2": [], "hw3": [], "hw4": [], "hw5": [], "hw6": ["1"], "hw7": [], "hw8": ["3.e"], "hw9": [], "hw10": ["7.c"], "hw11": [], "hw12": ["9.e", "9.f", "10"], "hw13": ["8.a", "8.b", "8.c", "8.d"], "hw14": ["9.i", "9.j", "10.a", "10.b", "10.c", "10.d", "10.e", "10.f"]}
max_scores = [250, 210, 220, 350, 140, 220, 250, 300, 350, 390, 460, 310, 250, 380, 300]
raw_max = sum(max_scores)
# Three modes:
	# calculates each homework as percent, weighted equally
	# calculate raw score, drop homework with lowest raw score, have extra credit be in raw
	# calculate raw score, drop homework with lowest percent, add extra credit to raw

class Homework:
	def __init__(self, name):
		self.score = 0
		self.max_score = 0
		self.extra = 0
		self.name = name

	def add_extra(self, score):
		self.extra += score

	def add_score(self, score):
		self.score += score
		self.max_score += 10

	def set_zero(self, max):
		self.max_score = max

	def get_percent(self):
		return self.score/self.max_score

	def get_extra_percent(self):
		return (self.extra + self.score)/self.max_score

	def get_raw(self):
		return self.score

	def get_max_raw(self):
		return self.max_score

	def get_extra(self):
		return self.extra

	def get_total_raw(self):
		return self.extra + self.score

	def __repr__(self):
		return self.name + ": " + str(self.score) + "/" + str(self.max_score) + " + " + str(self.extra)

def calculate():
	homeworks = []

	reg = re.compile('#Problem (\d\d?\.?\w*):\s(\d\d?)')

	for i in range(1, 16):
		name = "hw"+str(i)

		hw = Homework(name)
		homeworks.append(hw)

		try:
			fi = open(name+"_grades.txt", "r")
		except:
			hw.set_zero(max_scores[i - 1])
			continue

		for line in fi:
			m = reg.match(line)

			if not m:
				#print line
				continue

			if not m.group(1) in extra_credit[name]:
				hw.add_score(int(m.group(2)))
			else:
				hw.add_extra(int(m.group(2)))

	for h in homeworks:
		print(h)

	hw15 = homeworks.pop()

	#method one
	hw_method_one = sorted(homeworks, key=lambda hw: hw.get_percent())
	hw_method_one.reverse()
	hw_method_one.pop()
	final_percent = sum([h.get_extra_percent()*(1/13) for h in hw_method_one])
	final_percent += hw15.get_percent()*(1/13)
	print("method one: " + str(final_percent))

	#method two
	hw_method_two = sorted(homeworks, key=lambda hw: hw.get_raw())
	hw_method_two.reverse()
	temp = hw_method_two.pop()
	final_percent = sum([h.get_total_raw() for h in hw_method_two])/(raw_max - temp.get_max_raw())
	print("method two: " + str(final_percent))

	#method three
	hw_method_three = sorted(homeworks, key=lambda hw: hw.get_percent())
	hw_method_three.reverse()
	temp = hw_method_three.pop()
	final_percent = sum([h.get_total_raw() for h in hw_method_three])/(raw_max - temp.get_max_raw())
	print("method three: " + str(final_percent))

calculate()
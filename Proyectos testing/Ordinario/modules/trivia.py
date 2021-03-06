import enum

class Difficulty(str, enum.Enum):
	easy = "EASY",
	medium = "MEDIUM",
	hard = "HARD"

class Category:
	def __init__(self, name, id = None):
		self.name = name
		self.__id = id

	@property
	def id(self):
		return self.__id


class Player:
	def __init__(self, name, id = None):
		self.name = name
		self.__id = id

	@property
	def id(self):
		return self.__id

class Question:
	def __init__(self, **attr):
		self.question = attr.get("question", "")
		self.answers = attr.get("answers", [])
		self.correct_answer = attr.get("correct_answer", "")
		self.is_correct = attr.get("is_correct", False)

class Match:
	def __init__(self, questions, category, difficulty = Difficulty.medium):
		self.duration = 0
		self.index = 0
		self.player = None
		self.difficulty = difficulty
		self.category = category
		self.questions = questions

	def get_score(self): # pts assigned by difficulty
		score_pts = {
			Difficulty.easy: 1,
			Difficulty.medium: 1.5,
			Difficulty.hard: 2
		}

		qc = len([q for q in self.questions if q.is_correct])
		
		if qc >= 7: # apply multiplier
			qc = int((qc - 7) * score_pts[self.difficulty]) + 7

		return qc

class PlayerStatistics:
	def __init__(self, **stats):
		self.wins				= stats.get("wins", 0)
		self.games_played		= stats.get("games_played", 0)
		self.time_played		= stats.get("time_played", 0)
		self.ranking			= stats.get("ranking", 0)
		self.best_categories	= stats.get("best_categories", [])
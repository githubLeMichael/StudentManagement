class Student:
    def __init__(self, id, fullname, birthdate, sex, score_math, score_english, score_literature):
        self._id = id
        self._fullname = fullname
        self._birthdate = birthdate
        self._sex = sex
        self._scoremath = score_math
        self._scoreenglish = score_english
        self._scoreliterature = score_literature
        self._scoreavg = 0
        self._rankscore = ""
        
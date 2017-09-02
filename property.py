class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer!')
        if value < 0  or value >100:
            raise ValueError('Score must between 0~100!')
        self._score = value


class Stu(object):

    @property      #turn a getter method to attribute
    def score(self):
        return self._score

    @score.setter  # @property builds another setter decorator
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer')
        if value <0 or value >100:
            raise ValueError('Score must between 0~100')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth
    

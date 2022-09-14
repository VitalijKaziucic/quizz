from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, DateTime
from sqlalchemy.orm import declarative_base, relationship

db = "sqlite:///quizzes.db"
engine = create_engine(db, echo=False)
Base = declarative_base()


class Quizzes(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    question = relationship("Questions")
    game = relationship("QuizzGame")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    quizzes_id = Column(Integer, ForeignKey("quizzes.id"))
    possible_answers = relationship("PossibleAnswers")
    answers = relationship("Answers")
    pl_answers = relationship("PlayerAnswers")

    def __init__(self, question):
        self.question = question

    def __repr__(self):
        return f"{self.question}"


class PossibleAnswers(Base):
    __tablename__ = "possible_answers"
    id = Column(Integer, primary_key=True)
    answer = Column(String)
    questions_id = Column(Integer, ForeignKey("questions.id"))

    def __init__(self, answer):
        self.answer = answer

    def __repr__(self):
        return f"{self.answer}"


class Answers(Base):
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    answer = Column(String)
    questions_id = Column(Integer, ForeignKey("questions.id"))

    def __init__(self, answer):
        self.answer = answer

    def __repr__(self):
        return f"{self.answer}"


class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    game = relationship("QuizzGame")

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"


class QuizzGame(Base):
    __tablename__ = "quizz_game"
    id = Column(Integer, primary_key=True)
    datetime_ = Column(DateTime)
    player_id = Column(Integer, ForeignKey("player.id"))
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    pl_answer = relationship("PlayerAnswers")
    score = relationship("Score")

    def __init__(self, datetime_, quiz_id):
        self.datetime_ = datetime_
        self.quiz_id = quiz_id

    def __repr__(self):
        return f"{self.quiz_id} {self.datetime_}"


class PlayerAnswers(Base):
    __tablename__ = "player_answers"
    id = Column(Integer, primary_key=True)
    player_answer = Column(String)
    game_id = Column(Integer, ForeignKey("quizz_game.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))

    def __init__(self, player_answer, question_id):
        self.player_answer = player_answer
        self.question_id = question_id

    def __repr__(self):
        return f"{self.player_answer}"


class Score(Base):
    __tablename__ = "score"
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    game_id = Column(Integer, ForeignKey("quizz_game.id"))

    def __init__(self, score):
        self.score = score

    def __repr__(self):
        return f"{self.score}"


Base.metadata.create_all(engine)

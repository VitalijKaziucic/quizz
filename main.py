from sqlalchemy.exc import NoResultFound
from models import engine, Quizzes, QuizzGame, Questions, PossibleAnswers, Answers, Player, PlayerAnswers, Score
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from datetime import datetime
from random import shuffle

Session = sessionmaker(bind=engine)
session = Session()


# new_quizz = Quizzes("Lengvas IQ testas")
# new_quizz.question.append(Questions("Kiek vyrų reikia norint iškasti pusę duobės?"))
# new_quizz.question.append(Questions("Kokiais metais buvo įkurta NASA?"))
# new_quizz.question.append(Questions("Špinatuose yra daug:"))
# new_quizz.question.append(Questions("Kiek mėnesių per metus turi 28 dienas?"))
# new_quizz.question.append(Questions("Kiek nulių turi 1 milijonas?"))
# new_quizz.question.append(Questions("Kiek žemynų yra Žemėje?"))
# new_quizz.question.append(Questions("Kas buvo pirmas Lietuvos prezidentas?"))
# new_quizz.question.append(Questions("Kuris iš šių gamina medų?"))
# new_quizz.question.append(Questions("Kas buvo pirmasis žmogus mėnulyje?"))
# new_quizz.question.append(Questions("0 padauginus iš bet kurio skaičiaus, gaunamas rezultatas _."))
# session.add(new_quizz)
# session.commit()
#
# res = session.query(Questions).get(1)
# res.possible_answers.append(PossibleAnswers("10"))
# res.possible_answers.append(PossibleAnswers("1"))
# res.possible_answers.append(PossibleAnswers("0 tu negali iškasti pusės duobės"))
# res.possible_answers.append(PossibleAnswers("Nepakanka informacijos"))
# res.possible_answers.append(PossibleAnswers("2"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(2)
# res.possible_answers.append(PossibleAnswers("2009"))
# res.possible_answers.append(PossibleAnswers("1948"))
# res.possible_answers.append(PossibleAnswers("1960"))
# res.possible_answers.append(PossibleAnswers("1823"))
# res.possible_answers.append(PossibleAnswers("1958"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(3)
# res.possible_answers.append(PossibleAnswers("Vitamino C"))
# res.possible_answers.append(PossibleAnswers("Geležies"))
# res.possible_answers.append(PossibleAnswers("Biotino"))
# res.possible_answers.append(PossibleAnswers("Nė vienas iš aukščiau paminėtų"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(4)
# res.possible_answers.append(PossibleAnswers("1"))
# res.possible_answers.append(PossibleAnswers("3"))
# res.possible_answers.append(PossibleAnswers("4"))
# res.possible_answers.append(PossibleAnswers("1, bet ne kasmet, o kartą per 4 metus."))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(5)
# res.possible_answers.append(PossibleAnswers("6"))
# res.possible_answers.append(PossibleAnswers("5"))
# res.possible_answers.append(PossibleAnswers("3"))
# res.possible_answers.append(PossibleAnswers("4"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(6)
# res.possible_answers.append(PossibleAnswers("20"))
# res.possible_answers.append(PossibleAnswers("7"))
# res.possible_answers.append(PossibleAnswers("15"))
# res.possible_answers.append(PossibleAnswers("Virš 100"))
# res.possible_answers.append(PossibleAnswers("50"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(7)
# res.possible_answers.append(PossibleAnswers("Valdas Adamkus"))
# res.possible_answers.append(PossibleAnswers("Rolandas Paksas"))
# res.possible_answers.append(PossibleAnswers("Algirdas Brazauskas"))
# res.possible_answers.append(PossibleAnswers("Gitanas Nausėda"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(8)
# res.possible_answers.append(PossibleAnswers("Vapsva"))
# res.possible_answers.append(PossibleAnswers("Bitė"))
# res.possible_answers.append(PossibleAnswers("Širšė"))
# res.possible_answers.append(PossibleAnswers("Skraidanti skruzdėlė"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(9)
# res.possible_answers.append(PossibleAnswers("Lance’as Armstrongas"))
# res.possible_answers.append(PossibleAnswers("Džordžas Vašingtonas"))
# res.possible_answers.append(PossibleAnswers("Neilas Armstrongas"))
# res.possible_answers.append(PossibleAnswers("Mano mama"))
# res.possible_answers.append(PossibleAnswers("Aš"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(10)
# res.possible_answers.append(PossibleAnswers("0"))
# res.possible_answers.append(PossibleAnswers("Tas pats numeris"))
# res.possible_answers.append(PossibleAnswers("1"))
# res.possible_answers.append(PossibleAnswers("Neapibrėžtas"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(1)
# res.answers.append(Answers("0 tu negali iškasti pusės duobės"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(2)
# res.answers.append(Answers("1958"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(3)
# res.answers.append(Answers("Geležies"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(4)
# res.answers.append(Answers("1"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(5)
# res.answers.append(Answers("6"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(6)
# res.answers.append(Answers("7"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(7)
# res.answers.append(Answers("Algirdas Brazauskas"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(8)
# res.answers.append(Answers("Bitė"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(9)
# res.answers.append(Answers("Neilas Armstrongas"))
# session.add(res)
# session.commit()
#
# res = session.query(Questions).get(10)
# res.answers.append(Answers("0"))
# session.add(res)
# session.commit()

def get_player(name):
    try:
        return session.query(Player).filter(Player.name == name).one()
    except NoResultFound:
        return False


def existing_player():
    name = input("Nurodykite žaidėjo vardą: ").title().strip()
    if result := get_player(name):
        return result
    print("Žaidėjas nerastas, būsite nukreiptas susikurti naują žaidėją.")
    return add_player()


def add_player():
    name = input("Nurodykite naujo žaidėjo vardą: ").title().strip()
    if not get_player(name):
        print("Žaidėjas sėkmingai užregistruotas.")
        return Player(name)

    print("Nurodytas vardas jau užimtas, pasirinkite kitą.")
    return add_player()


def new_game():
    start_menu = ("Naujas žaidėjas", "Registruotas žaidėjas", "TOP 10", "Išeiti")
    for i, m in enumerate(start_menu, 1):
        print(i, m)
    while 1:
        user_choice = input("Nurodykite punktą: ")
        if user_choice == "1":
            return add_player()
        elif user_choice == "2":
            return existing_player()
        elif user_choice == "3":
            get_top10()
            return False
        elif user_choice == "4":
            print("Viso Gero")
            return -1
        else:
            print("Neteisingas pasirinkimas, bandykite dar kartą.")
            continue


def get_player_answers(game_id):
    res = session.query(QuizzGame.id, QuizzGame.datetime_, Player, Questions, PlayerAnswers, Answers)
    res = res.join(Player, PlayerAnswers, Questions, Answers).filter(QuizzGame.id == game_id)
    print(tabulate(res,
                   headers=["GameId", "DateTime", "PlayerName", "Question", "PlayerAnswer", "Answer"]))


def validate_user_input(answer_ls):
    msg = "Tokio pasirinkimo nėra, bandykite dar kartą."
    while True:
        user_input = input("Jūsų pasirinkimas: ")
        try:
            user_input = int(user_input)
        except ValueError:
            print(msg)
            continue
        else:
            if user_input <= 0 or user_input > len(answer_ls):
                print(msg)
                continue
            else:
                return user_input


def get_top10():
    res = session.query(QuizzGame.quiz_id,
                        QuizzGame.datetime_,
                        Player, Score).join(Player, Score).order_by(Score.score.desc()).limit(10)
    print(tabulate(res, headers=["QuizId", "DateTime", "PlayerName", "Score"]))


def game():
    now = datetime.now()
    result = 0
    while 1:
        player = new_game()
        if player == -1:
            break
        elif player:
            print("Sveiki, pasirinkite Viktorinos tematiką!")
            quizzes = session.query(Quizzes).all()
            for quiz in quizzes:
                print(quiz.id, quiz)
            quiz_theme = validate_user_input(quizzes)
            new_quiz = QuizzGame(datetime_=now, quiz_id=quiz_theme)
            player.game.append(new_quiz)
            session.add(player)
            questions = session.query(Questions).filter_by(quizzes_id=int(quiz_theme)).all()
            shuffle(questions)
            for i_, question in enumerate(questions, 1):
                print(i_, question)
                answers = session.query(PossibleAnswers).filter_by(questions_id=question.id).all()
                shuffle(answers)
                for i, ans in enumerate(answers, 1):
                    print(" ", i, ans)
                usr_answer = answers[validate_user_input(answers) - 1]
                if str(usr_answer) == str(session.query(Answers).filter(Answers.questions_id == question.id).one()):
                    result += 1
                new_quiz.pl_answer.append(PlayerAnswers(str(usr_answer), question.id))
            new_quiz.score.append(Score(int(result)))
            session.add(new_quiz)
            session.commit()
            print(f"Sėkmingai atsakėte į {result}/{len(questions)} klausimus.")
            get_player_answers(new_quiz.id)
            result = 0
        else:
            continue


if __name__ == "__main__":
    game()

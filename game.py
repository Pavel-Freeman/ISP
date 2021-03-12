from random import randint
import logging

logging.basicConfig(level=logging.INFO)


def choose_one_player(magic_number, user_number, attempt):
    while user_number != magic_number:
        user_number = int(input("Ваше число? : "))
        if user_number < magic_number:
            logging.info("Ваше число меньше, чем магическое.")
            attempt += 1
        elif user_number > magic_number:
            logging.info("Ваше число больше, чем магическое.")
            attempt += 1
        elif user_number > 100 or user_number < 1:
            logging.info("Ваше число не подходит в диапазон")
    return attempt


def choose_two_player(magic_number, user_number, attempt):
    user_number2 = 0
    while user_number != magic_number or user_number2 != magic_number:
        user_number = int(input("Ходит игрок 1. Ваше число? : "))
        if user_number < magic_number:
            logging.info("Ваше число меньше, чем магическое.")
            attempt += 1
            step = 2
        if user_number > magic_number:
            logging.info("Ваше число больше, чем магическое.")
            attempt += 1
            step = 2
        if user_number > 100 or user_number < 1:
            logging.info("Ваше число не подходит в диапазон")
            step = 2

        if user_number == magic_number:
            break

        user_number2 = int(input("Ходит игрок 2. Ваше число? : "))
        if user_number2 < magic_number:
            logging.info("Ваше число меньше, чем магическое.")
            attempt += 1
            step = 1
        if user_number2 > magic_number:
            logging.info("Ваше число больше, чем магическое.")
            attempt += 1
            step = 1
        if user_number2 > 100 or user_number2 < 1:
            logging.info("Ваше число не подходит в диапазон")
            step = 1

        if user_number2 == magic_number:
            break
    return attempt


def main():
    logging.info(
        "Игра загадает число от 1 до 100, а вы должны его отгадать!"
    )

    magic_number = randint(1, 100)
    user_number = 0
    attempt = 0
    step = 1

    players = int(input("Введите количество игроков (от 1 до 2) : "))

    if players == 1:
        attempt = choose_one_player(magic_number, user_number, attempt)

    if players == 2:
        attempt = choose_two_player(magic_number, user_number, attempt)

    attempt += 1
    if players == 1:
        logging.info("Ура! Вы отгадали число!")
        logging.info("Правильный ответ - %s", str(magic_number))
        logging.info("Вы угадали это число с %s-й попытки.", str(attempt))
    if players == 2:
        if step == 1:
            logging.info("Поздравляю, игрок 1! Вы выиграли!")
            logging.info("Правильный ответ - %s", str(magic_number))
            logging.info("Вы угадали это число с %s -й попытки.", str(attempt))
        elif step == 2:
            logging.info("Поздравляю, игрок 2! Вы выиграли!")
            logging.info("Правильный ответ - %s", str(magic_number))
            logging.info("Вы угадали это число с %s -й попытки.", str(attempt))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.error("Error")

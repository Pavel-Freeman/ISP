from random import randint
import logging
logging.basicConfig(level=logging.INFO)

def main():
    logging.info("Вас приветствует игра GuessTheNumber. Она загадает число от 1 до 100, а вы должны его отгадать!")
    
    mag = randint(1, 100)
    user = 0
    Attempt = 0
    xod = 1
    
    pla = int(input("Введите количество игроков (от 1 до 2) : "))
    
    if pla == 1 :
        while user != mag :
            user = int(input("Ваше число? : "))
            if user < mag :
                logging.info('Ваше число меньше, чем магическое.')
                Attempt += 1
            elif user > mag :
                logging.info("Ваше число больше, чем магическое.")
                Attempt += 1
            elif user > 100 or user < 1:
                logging.info("Ваше число не подходит в диапазон")
    
    if pla == 2 :
        user2 = 0
        while user != mag or user2 != mag:
            user = int(input("Ходит игрок 1. Ваше число? : "))
            if user < mag :
                logging.info("Ваше число меньше, чем магическое.")
                Attempt += 1
                xod = 2
            if user > mag :
                logging.info("Ваше число больше, чем магическое.")
                Attempt += 1
                xod = 2
            if user > 100 or user < 1:
                logging.info("Ваше число не подходит в диапазон")
                xod = 2
    
            if user==mag:
                break
    
            user2 = int(input("Ходит игрок 2. Ваше число? : "))
            if user2 < mag :
                logging.info("Ваше число меньше, чем магическое.")
                Attempt += 1
                xod = 1
            if user2 > mag:
                logging.info("Ваше число больше, чем магическое.")
                Attempt += 1
                xod = 1
            if user2 > 100 or user2 < 1:
                logging.info("Ваше число не подходит в диапазон")
                xod = 1
    
            if user2==mag:
                break
    
            
    
    Attempt += 1
    if pla == 1 :
        logging.info("Ура! Вы отгадали число!")
        logging.info("Правильный ответ - " + str(mag))
        logging.info("Вы угадали это число с " + str(Attempt) + "-й попытки.")
    if pla == 2:
        if xod == 1 :
            logging.info("Поздравляю, игрок 1! Вы выиграли!")
            logging.info("Правильный ответ - " + str(mag))
            logging.info("Вы угадали это число с " + str(Attempt) + "-й попытки.")
        elif xod == 2 :
            logging.info("Поздравляю, игрок 2! Вы выиграли!")
            logging.info("Правильный ответ - " + str(mag))
            logging.info("Вы угадали это число с " + str(Attempt) + "-й попытки.")
if __name__ == '__main__':            
        main()
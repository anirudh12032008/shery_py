import pygame
import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
prize_money = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
questions = [
    ["What is the capital of India?", "A. New Delhi", "B. Mumbai", "C. Bangalore", "D. Kolkata", "A"],
    ["Which planet is closest to the Sun?", "A. Venus", "B. Earth", "C. Mars", "D. Mercury", "D"],
    ["What is the largest mammal in the world?", "A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Lion", "C"],
    ["What is the symbol for the element oxygen?", "A. O", "B. Ox", "C. Oxg", "D. O2", "A"],
    ["Who wrote 'Harry Potter' series?", "A. J.R.R. Tolkien", "B. J.K. Rowling", "C. George Orwell", "D. Charles Dickens", "B"],
    ["What is the national flower of Japan?", "A. Rose", "B. Sunflower", "C. Sakura (Cherry Blossom)", "D. Tulip", "C"],
    ["What is the largest planet in our solar system?", "A. Earth", "B. Mars", "C. Jupiter", "D. Saturn", "C"],
    ["Which gas do plants release during photosynthesis?", "A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen", "A"],
    ["In which year did Christopher Columbus discover America?", "A. 1492", "B. 1776", "C. 1066", "D. 1515", "A"],
    ["Who is known as the 'Father of Modern Physics'?", "A. Isaac Newton", "B. Galileo Galilei", "C. Albert Einstein", "D. Johannes Kepler", "C"],
    ["What is the chemical symbol for silver?", "A. S", "B. Si", "C. Ag", "D. Al", "C"],
    ["Which novel opens with the line, 'It was the best of times, it was the worst of times'?", "A. War and Peace", "B. Pride and Prejudice", "C. Moby-Dick", "D. A Tale of Two Cities", "D"],
    ["Who painted the Mona Lisa?", "A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Michelangelo", "B"],
    ["What is the currency of Australia?", "A. Euro", "B. Yen", "C. Dollar", "D. Peso", "C"],
    ["Which gas makes soda fizzy?", "A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Helium", "C"],
    ["Who is the author of '1984'?", "A. F. Scott Fitzgerald", "B. George Orwell", "C. Aldous Huxley", "D. Ernest Hemingway", "B"],
]


# Playing the sounds
def play_sound(sound_file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


def play():
    play_sound('intro.mp3')
    qnum = 0
    money = 0
    print('Welcome to KBC')
    time.sleep(10)
    while qnum<14:
        play_sound('que.mp3')
        time.sleep(2)
        print(f'Question number {qnum+1} for {prize_money[qnum]} Rs \n {questions[qnum][0]}\n {questions[qnum][1]}\t {questions[qnum][2]}\n {questions[qnum][3]} \t {questions[qnum][4]}')
        user = input('Please Enter A, B, C or D')
        if user==questions[qnum][5]:
            print(f'Congratulations you won {prize_money[qnum]} Rs \n')
            money = prize_money[qnum]
            qnum += 1
        else:
            print(f'Oh NO this is the wrong answer the correct answer is {questions[qnum][5]} \n You won {money} Rs \n Thank You for playing')
            break

play()

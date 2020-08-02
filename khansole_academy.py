"""
File: khansole_academy.py
-------------------------
** The description of this program is summarized/paraphrased from the assignment provided
in Stanford's Code in Place class offered in 2020 **
The program generates addition problems for the user and takes in their input. If
the integer that the user inputs equals the answer to the addition problem then the
user is notified and gets another question. If the user's answer is incorrect then
they are notified and they get another addition question. The program keeps track
of how many in a row the user has gotten correct and stops asking questions after the
third correct response.
"""

import random

# defines minimum two digit number as 10
num_min = 10
# defines maximum two digit number as 99
num_max = 99
# defines the number of correct questions to stop the loop
num_correct = 3

def main():
    # selects a random integer from between num_min (10) and num_max (99)
    # and assigns it to variable num1
    num1 = random.randint(num_min, num_max)
    # selects a random integer from between num_min (10) and num_max (99)
    # and assigns it to variable num2
    num2 = random.randint(num_min, num_max)
    # assigns sum of num1 and num2 to variable answer
    answer = num1 + num2
    # converts answer to a string
    total = answer
    # asks user for input to question what is sum of num1 and num2
    q_correct_in_a_row = 0
    # when user has not gotten 3 questions correct in a row, keeps asking questions
    while q_correct_in_a_row != num_correct:
        user_question = print("What is " + str(num1) + "+" + str(num2) + "?")
        user_answer = float(input("Your answer is: "))
        # if user inputs a number matching total, the number correct increases by 1
        if user_answer == total:
            q_correct_in_a_row = q_correct_in_a_row + 1
            print("Correct. You have gotten "+str(q_correct_in_a_row)+" correct.")
            # restarts loop after user has entered input that matches previous total
            # and assigns new values to num1, num2, answer and total
            num1 = random.randint(num_min, num_max)
            num2 = random.randint(num_min, num_max)
            answer = num1 + num2
            total = answer
        # if user gets an answer incorrect the counter of correct questions in a row restarts
        else:
            q_correct_in_a_row = 0
            print("Incorrect! The expected answer is "+str(total)+"")
            # restarts loop after user has entered input that does not match previous total
            # and assigns new values to num1, num2, answer and total
            num1 = random.randint(num_min, num_max)
            num2 = random.randint(num_min, num_max)
            answer = num1 + num2
            total = answer
    # when 3 questions have been answered correctly in a row prints congratulations message,
    # stops asking questions
        if q_correct_in_a_row == num_correct:
            print("Congratulations! You have gotten 3 correct in a row.")

if __name__ == '__main__':
    main()
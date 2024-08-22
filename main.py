import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_questions = 10


def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    problem = str(left) + " " + operator + " " + str(right)
    solution = eval(problem)
    return problem, solution


count = 1
correct_answers = 0
wrong_answers = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(total_questions):
    problem, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + " " + problem + " = ")
        if guess == str(answer):
            break
        wrong_answers += 1

end_time = time.time()
total_time = round(end_time - start_time,1)

print("----------------------")
print(f"Well done! You fininshed in {total_time} seconds. In total you had {wrong_answers} wrong answers.")

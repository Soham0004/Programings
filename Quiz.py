import random
questions = [
    "What is the capital of France?",
    "What is the highest mountain in the world?",
    "What is the largest ocean?",
    "What is the most populous country in the world?",
    "What is the smallest planet in our solar system?",
    "What is the chemical symbol for gold?",
    "What is the name of the current president of the United States?",
    "What is the name of the first person to walk on the moon?",
    "What is the longest river in the world?",
    "What is the largest country in the world by land area?"
]
answers = [
    "Paris",
    "Mount Everest",
    "Pacific Ocean",
    "China",
    "Mercury",
    "Au",
    "Joe Biden",
    "Neil Armstrong",
    "Nile River",
    "Russia"
]
score = 0
selected_questions = random.sample(range(len(questions)), 4)
for i in selected_questions:
    answer = input(questions[i] + " ")
    if answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is", answers[i])
print("You got", score, "out of 4 questions correct.")

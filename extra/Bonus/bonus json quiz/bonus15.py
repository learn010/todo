import json

with open("questions.json") as questions:
    content = questions.read()

data = json.loads(content)

score = 0
for q in data:
    print(q["question_text"])
    for index, alt in enumerate(q["answers"]):
        print(f" {index +1} - {alt}.")
    user_choice = int(input("enter your answer: "))
    q["user_choice"] = user_choice


for index, question in enumerate(data):
    if user_choice == q['answers']:
        score += 1
        result = "correct answer"
    else:
        result = "Wrong answer"

    message = f"{index+1} - {result}, you answered {question['user_choice']}, the correct answer is" \
              f" {question['correct_answer_key']}"
    print(message)

print(f"you answered {score} answers correctly out of the possible {len(data)}")


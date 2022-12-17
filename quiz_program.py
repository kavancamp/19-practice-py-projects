#dictionary that stores questions and answers
#variable tracks the score of the player
#loop through the dictionary using the key value pairs   

quiz = {
  "question1": {
    "question": "What is the capital of France?",
    "answer": "Paris"
  },
  "question2": {
    "question": "What is the capital of Germany?",
    "answer": "Berlin"
  },
  "question3": {
    "question": "What is the capital of Italy?",
    "answer": "Rome"
  },
  "question4": {
    "question": "What is the capital of Spain?",
    "answer": "Madrid"
  },"question5": {
    "question": "What is the capital of Portugal?",
    "answer": "Lisbon"
  },"question6": {
    "question": "What is the capital of Switzerland?",
    "answer": "Bern"
  },"question7": {
    "question": "What is the capital of Austria?",
    "answer": "Vienna"
  },
}

score = 0

for key, value in quiz.items():
  print(value['question'])
  answer = input("Answer? ")

  if answer.lower() == value['answer'].lower():
    print("Correct")
    score = score + 1
    print("Your score is: " + str(score))
    print("")
    print("")

  else: 
    print("Invalid!")
    print("Your answer is: " + value['answer'])
    print("Your score is: " + str(score))
    print("")
    print("")

print("You got " + str(score) + " out of 7 questions coreectly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")
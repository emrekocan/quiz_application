# Quiz Program

This Python program is a simple quiz game that allows users to answer multiple-choice questions. It consists of two main classes: `Question` and `Quiz`.

## Question Class

The `Question` class is responsible for creating individual questions. Each question has text, a list of choices, and the correct answer.

### Methods

- `__init__(self, text, choices, answer)`: Initializes a question with the provided text, choices, and correct answer.
- `checkAnswer(self, answer)`: Checks if the given answer is correct.

## Quiz Class

The `Quiz` class manages a set of questions and keeps track of the user's score and progress in the quiz.

### Methods

- `__init__(self, questions)`: Initializes the quiz with a list of questions.
- `getQuestion(self)`: Returns the current question.
- `displayQuestion(self)`: Displays the current question and handles user input.
- `guess(self, answer)`: Checks the user's answer and updates the score and question index.
- `loadQuestion(self)`: Loads the next question or shows the final score if all questions are answered.
- `showScore(self)`: Displays the final score.
- `displayProgress(self)`: Displays the current question number and total questions.

## Usage

To use the quiz program, create instances of the `Question` class and add them to a list. Then, create an instance of the `Quiz` class with the list of questions and call the `loadQuestion` method to start the quiz.

```python
q1 = Question('What is the best programming language?', ['C#', 'Python', 'JavaScript'], 'Python')
q2 = Question('Which programming language is the most popular?', ['C#', 'Python', 'JavaScript'], 'Python')
q3 = Question('Which programming language is the most lucrative?', ['C#', 'Python', 'JavaScript'], 'Python')

questions = [q1, q2, q3]
quiz = Quiz(questions)
quiz.loadQuestion()

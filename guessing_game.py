class GuessingGame:
    """Create a class for for game that takes in user input and returns if they guessed correct number"""

    def __init__(self, answer):
        self.answer = answer
        self.guess_result= None

    def guess(self, user_guess):
        if user_guess < self.answer:
            self.guess_result = "low"
        elif user_guess > self.answer:
            self.guess_result = "high"
        else: 
            self.guess_result = "correct"
        return self.guess_result
    
    def solved(self):
        return self.guess_result == "correct"

answer = GuessingGame(10)
print(answer.solved())   # False

print(answer.guess(5))   # 'low'
print(answer.guess(20))  # 'high'
print(answer.solved())   # False

print(answer.guess(10))  # 'correct'
print(answer.solved())   # True
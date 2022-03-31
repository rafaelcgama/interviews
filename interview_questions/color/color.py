### 1 Dimmer  3 bulbs in sequence
# 1 dimmer | 10w | 20w | 30w
# 5        | 0   | 0   | 0
# 10       | 5   | 10  | 15
# 15       | 10  | 20  | 30


def bulbs(arr):
    if sum(arr) == len(arr):
        return 0

    total = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            total += 1
            for j in range(i, len(arr)):
                arr[j] = 1 if arr[j] == 0 else 0

    return total


def bulbs2(arr):
    if sum(arr) == len(arr):
        return 0

    total, flipped = 0, False
    for a in arr:
        if a == 0 and not flipped:
            flipped, total = True, total + 1

        elif a == 1 and flipped:
            flipped, total = False, total + 1

    return total

def bulbSwitch(n):
    bulbs = [0] * n
    for i in range(1, len(bulbs) + 1):
        j = i
        while j <= len(bulbs) + 1:
            bulbs[j - 1] = not bulbs[j - 1]
            j += j

    return sum(bulbs)


class Paint:
    def __init__(self, n):
        self.grid = [[0] * 10 for _ in range(n)]
        self.main_state = []
        self.undo_state = []

    def draw_pixel(self, x, y, new_color):
        self.main_state.append({
            'pos': (x, y),
            'old_color': self.grid[x][y],
            'new_color': new_color
        })
        self.grid[x][y] = new_color
        self.undo_state.clear()

    def undo(self):
        assert len(self.main_state), "Cannot undo anymore"

        self.undo_state += [self.main_state.pop()]
        x, y = self.undo_state[-1]['pos']
        self.grid[x][y] = self.undo_state[-1]['old_color']

    def redo(self):
        assert len(self.undo_state), "Cannot redo anymore"

        new_state = self.undo_state.pop()
        x, y = new_state['pos']
        self.grid[x][y] = new_state['new_color']


## SYSTEM DESIGN
"""
Questions: Design Problem
Historically we have had a HealthHistory model which contains all the information we ask a user about their health to help customize their genetics report. It was “one’ mega-table with columns reflecting what we asked our users.


Everytime we wanted to add a new field it involved
 Adding a new column to the database
 Running a migration
 Adding a new front-end to render/ask the question.

Objective: We want to build a platform that removes these engineering costs to add questions we want to collect from our users.



Goals:

Supporting different types of question types: Select choice, multiple select, text field
One UI engine for rendering questions
We want to ask a collection of questions to users. 

Consider data layer, API’s, and Front-end. Feel free to choose a spot to start here


Data Model 

Quiz
Id 
Name text
List of questions 

Quiz_Question 
Quiz_Question
Id (Quiz) 
Id (Question)


Question
Question_text text
Type_question FK (Question_Type)
Options 

Question Type
id
Question_type_text

User 
Id	
Name 

Answers
id
- user (User)
- question (Quiz_Question)
- answer_text [text]
- answer_select  [text]
- answer_multiple [list of text]




APIs

/api/users/:id/answer
	POST {
			Quiz_Question:
			Answer_text: 

}

/api/quiz
	Get {
		Id: Quiz_id
}


	response:
		{
			Name: quiz 1,
			List_quesitons: [ 
{
	Question name:
	Type_question:
	Options:
}
…





Question 1:
type: free text
question_text: what is your name
Question 2:
type: select
question_text: which symptoms are you feeling
options: headache, fever, sore throat
"""

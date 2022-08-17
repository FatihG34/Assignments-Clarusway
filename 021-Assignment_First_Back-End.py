# BASEBALL GAME


# You are keeping score for a baseball game with strange rules. The game consist of several rounds, where the scores of past rounds may affect future rounds' scores.

# At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

# An integer x - Record a new score of x,
# "+" - Record a new score that is the sum of the previous scores. It is guaranteed there will always be two previous scores.
# "D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
# "C" - Invalidate the pevious score, removing it from the record. It is guaranteed there will always be a previous score.
# Return the sum of all the scores on the record.

# Example 1:

# Input: ops = ["5", "2", "C", "D", "+"]
# Output: 30
# Explanation:

# "5" - Add 5 to the record, record is now[5],
# "2" - Add 2 to the record, record is now[5, 2],
# "C" - Invalidate and remove the previous score, record is now[5],
# "D" - Add 2 * 5 = 10 to the record, record is now[5, 10],
# "+" - Add 5 + 10 = 15 to the record, record is now[5, 10, 15],
# The total sum is 5 + 10 + 15 = 30.

def baseball_score(a_list):
    score_list = []
    for i in a_list:
        try:
            score_list.append(int(i))
        except:
            if i == 'D' and i != a_list[0]:
                score_list.append(2 * score_list[-1])
            elif i == 'C' and i != a_list[0]:
                score_list.pop()
            elif i == '+' and i != a_list[0] and (score_list[-1] or score_list[-1] == 0) and (score_list[-2] or score_list[-2] == 0):
                score_list.append(score_list[-1] + score_list[-2])
            else:
                return 'Somethings went wrong'
    return sum(score_list)


first_score_list = ["5", "2", "C", "D", "+"]
baseball_score(first_score_list)

# Output : 30


ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
baseball_score(ops)

# OutPut : 27

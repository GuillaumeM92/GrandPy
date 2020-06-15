import re
from flask import request
from utils.stopwords import stopwords

def get_question():
    question = request.get_json()
    return question["user_input_value"]

def parse(question):
    answer = []

    lowered_question = question.lower()   # remove capital letters

    remove_dash = lowered_question.replace("-", " ").replace("'", " ")   # replace - and ' symbols with space

    stripped_question = re.sub(r'[^\w\s]', '', remove_dash)   # only keep alphanumerical characters

    split_question = stripped_question.split(' ')   # split on space

    for word in split_question:   # check if the words are in the stopwords list
        if word in stopwords:
            pass
        else:
            answer.append(word)   # if not, add to the answer

    answer_string = " ".join(answer)   # convert answer to a string

    return(answer_string)

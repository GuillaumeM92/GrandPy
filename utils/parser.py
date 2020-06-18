import re
from flask import request, jsonify
from utils.stopwords import stopwords


def parse(question):
    answer = []

    try:
        lowered_question = question.lower()   # remove capital letters

        # replace - and ' symbols with space
        remove_dash = lowered_question.replace("-", " ").replace("'", " ")

        # only keep alphanumerical characters
        stripped_question = re.sub(r'[^\w\s]', '', remove_dash)

        split_question = stripped_question.split(' ')   # split on space

        for word in split_question:   # check if the words are in the stopwords list
            if word in stopwords:
                pass
            else:
                answer.append(word)   # if not, add to the answer

        answer_string = " ".join(answer)   # convert answer to a string

        if answer_string == "":
            return("ignore")

        else:
            return(answer_string)

    except Exception as e:
        return ("An exception occured while parsing the question.", e)

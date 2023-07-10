from chatbot import say
import wolframalpha

def Wolfram(query,voice):
    api_key = "LR33QE-LUP5Q99YK4"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        Answer = next(requested.results).text
        return Answer
    except:
        say("Sorry sir but the value is not answerable!",voice)


def calc(query,voice):
    Term = str(query)
    Term = Term.replace("kira", " ")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divide", "/")
    Term = Term.replace("multiply", "*")

    Final = str(Term)

    try:
        result = Wolfram(Final,voice)
        say(result,voice)

    except:
        say("Sorry sir the query is not ansewerable!",voice)
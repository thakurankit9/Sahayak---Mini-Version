# Response file for Sahayak
from data import education
from data import health
from data import emergency
from data import wifi
def give_answer(problem, category):
    if category == "education":
        for word in education:
            if word in problem:
                return education[word]
    elif category == "health":
        for word in health:
            if word in problem:
                return health[word]
    elif category == "emergency":
        for word in emergency:
            if word in problem:
                return emergency[word]
    elif category == "wifi":
        for word in wifi:
            if word in problem:
                return wifi[word]
    return "Sorry, I could not understand your problem."
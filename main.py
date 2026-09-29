# Main file for Sahayak 
from category import find_category
from response import give_answer
print("===================================")
print("       WELCOME TO SAHAYAK ")
print(" Student and Community Assistant")
print("===================================")
while True:
    problem = input("\nEnter your problem: ")
    problem = problem.lower()
    if problem == "exit":
        print("Thank you for using Sahayak!")
        break
    category = find_category(problem)
    print("\nCategory:", category)
    answer = give_answer(problem, category)
    print("Sahayak :", answer)
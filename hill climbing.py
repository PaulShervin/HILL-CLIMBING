import random
import string

def generate_random_solution(answer):
    l = len(answer)
    return [random.choice(string.printable) for _ in range(l)]

def evaluate(solution, answer):
    print(solution)
    target = list(answer)
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s) - ord(t))
    return diff

def mutate_solution(solution):
    new_solution = list(solution)  # make a copy
    ind = random.randint(0, len(solution) - 1)
    new_solution[ind] = random.choice(string.printable)
    return new_solution

def SimpleHillClimbing():
    answer = "Artificial Intelligence"
    best = generate_random_solution(answer)
    best_score = evaluate(best, answer)
    
    while True:
        print("Score:", best_score, "Solution:", "".join(best))
        if best_score == 0:
            break
        new_solution = mutate_solution(best)
        score = evaluate(new_solution, answer)
        
        if score < best_score:
            best = new_solution
            best_score = score

SimpleHillClimbing()

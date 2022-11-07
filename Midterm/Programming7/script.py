import random
# this line of code makes it so that calls to random always produce the same
# successive values so that the examples below always produce the same results
random.seed(7)
def lottery(limit, guess, prize):   # largest number, list of guesses, max amount that can be won
    random_numbers = []
    while len(random_numbers) < len(guess):
        random_num = random.randint(1, limit)
        if not random_num in random_numbers:
            random_numbers.append(random_num)
    count_correct_guesses = 0
    for i in range(len(guess)):
        if guess[i] in random_numbers:
            count_correct_guesses += 1
    # For an exact match, the whole prize is paid out. 
    # If one number differs, half of the prize is paid out.
    # If two numbers differ, a quarter of the prize is paid out
    # and so on. If none of the numbers match, the prize money is 0.
    random_nums_set = set(random_numbers)
    guess_set = set(guess)
    querschnitt = random_nums_set & guess_set
    payout = prize * (0.5)**(len(guess)-len(querschnitt))
    if(len(guess)-len(querschnitt) == len(guess)):
        payout = 0
    return (sorted(random_numbers), len(querschnitt), payout)

print( lottery(52, [4, 8, 15, 16, 23, 42], 1000000) ) # 2 matching
print( lottery(3, [1, 2, 3], 1000000) )               # inevitable perfect match
print( lottery(10000, [1, 2, 3], 1000000) )           # zero matching
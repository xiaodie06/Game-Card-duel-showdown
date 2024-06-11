import random

NUM_DECK = 1

def main():
# Create a deck of play cards at random order
    cards = random_card(NUM_DECK)
    print(cards)
# Give the cards to play 1 and play 2
    play1 = []
    play2 = []
    for i in range(len(cards)):
        if i%2 == 1:
            play2.append(cards[i])
        else:
            play1.append(cards[i])
    print(play1)
    print(play2)

#Compare the number
    num1 = 0
    num2 = 0
    for i in range(len(play1)):
        print("This is round ", str(i), ".")
        if play1[i]==play2[i]:
            print("Player One and Player Two reached a draw.")
        elif play1[i]>play2[i]:
            print("Play One won!")
            num1 += 2
        else:
            print("Play Two won!")
            num2 += 2
        print("Now Play One has", str(num1), "cards.")
        print("Now Play Two has", str(num2), "cards.")
        print("")
    if num1>num2:
        print("Play One won the game! Congratulations!")
    else:
        print("play Two won the game!")

def random_card(NUM_DECK):
    random_card = []
    for i in range(13):
        random_card.append (i+1)
    random_card *= 4
    random.shuffle(random_card)
    return(random_card)


if __name__ == '__main__':
    main()
VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score= 0
    ace_count = 0
    if len(hand)>5:
        return "Invalid"
    for card in hand:
        if card in VALID_CARDS:
            if card in ['Jack', 'Queen', 'King']:
                score +=10
            elif card == "Ace":
                ace_count +=1
            else:
                score += card
        else:
            return "Invalid"
    if ace_count >1:
        score += (ace_count-1)
    if ace_count:
        if score + 11 <=21:
            score+=11
        else:
            score+=1
    if score > 21:
        return "Bust"
    return score
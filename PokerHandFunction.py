def findPokerHand(hand):

    ranks =[]
    suits = []

    for card in hand:
        if len(card)==2:
            rank = card[0]
            suit = card[1]
        if len(card)==3:
            rank = card[0:2]
            suit = card[2]

        if rank == 'A':
            rank = 14
        if rank == 'K':
            rank = 13
        if rank == 'Q':
            rank = 12
        if rank == 'J':
            rank = 11
        rank = int(rank)
        ranks.append(rank)
        suits.append(suit)

    ranks = sorted(ranks)

    # for royal flush, straight flush and flush
    if suits.count(suits[0])==5:
        if ranks == [10,11,12,13,14] :
            output = "Royal Flush"


        elif ranks[0]+4==ranks[1]+3==ranks[2]+2==ranks[3]+1==ranks[4] or ranks == [2, 3, 4, 5, 14]:
            output = "Straight Flush"

        else:
            output = "Flush"


    elif ranks.count(ranks[0])==4 or ranks.count(ranks[1])==4:
        output="Four of a Kind"


    elif ranks.count(ranks[0])==3 or ranks.count(ranks[1])==3 or ranks.count(ranks[2])==3:
        if len(set(ranks))==2:
            output="Full House"

        else:
            output="Three of a Kind"


    elif ranks[0]+4==ranks[1]+3==ranks[2]+2==ranks[3]+1==ranks[4] or ranks == [2, 3, 4, 5, 14]:
        output="Straight"


    elif len(set(ranks))==3:
        output="Two Pair"


    elif len(set(ranks))==4:
        output="Pair"


    else:
        output="High Card"

    print(hand,output)
    return output


if __name__=="__main__":
    findPokerHand(["KH", "AH", "QH", "JH", "10H"])  # Royal Flush
    findPokerHand(["QC", "JC", "10C", "9C", "8C"])  # Straight Flush
    findPokerHand(["5C", "5S", "5H", "5D", "QH"])  # Four of a Kind
    findPokerHand(["2H", "2D", "2S", "10H", "10C"])  # Full House
    findPokerHand(["2D", "KD", "7D", "6D", "5D"])  # Flush
    findPokerHand(["JC", "10H", "9C", "8C", "7D"])  # Straight
    findPokerHand(["10H", "10C", "10D", "2D", "5S"])  # Three of a Kind
    findPokerHand(["KD", "KH", "5C", "5S", "6D"])  # Two Pair
    findPokerHand(["2D", "2S", "9C", "KD", "10C"])  # Pair
    findPokerHand(["KD", "5H", "2D", "10C", "JH"])  # High Card
from colorama import just_fix_windows_console, Fore
just_fix_windows_console()

def hit(current_hand, hand_value, deck, hit_choice = 1):
    hand_value_copy = hand_value.copy()
    card_drawn = deck[0]
    current_hand.append(card_drawn)
    if (hit_choice == 1):
        print(Fore.BLUE + "You decide to Hit.")
    print(Fore.BLUE + "You drew", card_drawn, end=". ")
    deck.pop(0)
    if not hand_value:
        try:
            hand_value.add(int(card_drawn[0]))
        except ValueError:
            if card_drawn[0] in "XJQK":
                hand_value.add(10)
            else:
                hand_value.add(11)
                hand_value.add(1)
    else:
        to_add = set()
        to_remove = set()
        
        try:
            card_value = int(card_drawn[0])
            for value in hand_value_copy:
                new_value = value + card_value
                if new_value <= 21:
                    to_add.add(new_value)
                to_remove.add(value)
        except ValueError:
            if card_drawn[0] in "XJQK":
                card_value = 10
                for value in hand_value_copy:
                    new_value = value + card_value
                    if new_value <= 21:
                        to_add.add(new_value)
                    to_remove.add(value)
            else:
                for value in hand_value_copy:
                    if value + 10 <= 21:
                        to_add.add(value + 11)
                    to_add.add(value + 1)
                    to_remove.add(value)
        
        hand_value.update(to_add)
        hand_value.difference_update(to_remove)
    
    if len(hand_value) == 0:
        hand_value.add(new_value)
        print(Fore.BLUE + "Current hand value(s): ", end="")
        for value in hand_value:
            print(value,end=" ")
        print()
        return -1
    
    print(Fore.BLUE + "Current hand value(s): ", end="")
    for value in hand_value:
        print(value,end=" ")
    print()
    if 21 in hand_value:
        return 1
    return 0

def dealer_hit(current_hand, hand_value, deck):
    hand_value_copy = hand_value.copy()
    card_drawn = deck[0]
    current_hand.append(card_drawn)
    print(Fore.YELLOW + "Dealer drew", card_drawn, end=". ")
    deck.pop(0)
    if not hand_value:
        try:
            hand_value.add(int(card_drawn[0]))
        except ValueError:
            if card_drawn[0] in "XJQK":
                hand_value.add(10)
            else:
                hand_value.add(11)
                hand_value.add(1)
    else:
        to_add = set()
        to_remove = set()
        
        try:
            card_value = int(card_drawn[0])
            for value in hand_value_copy:
                new_value = value + card_value
                if new_value <= 21:
                    to_add.add(new_value)
                to_remove.add(value)
        except ValueError:
            if card_drawn[0] in "XJQK":
                card_value = 10
                for value in hand_value_copy:
                    new_value = value + card_value
                    if new_value <= 21:
                        to_add.add(new_value)
                    to_remove.add(value)
            else:
                for value in hand_value_copy:
                    if value + 11 <= 21:
                        to_add.add(value + 11)
                    to_add.add(value + 1)
                    to_remove.add(value)
        
        hand_value.update(to_add)
        hand_value.difference_update(to_remove)
    
    if len(hand_value) == 0:
        hand_value.add(new_value)
        print(Fore.YELLOW + "Dealer hand value(s): ", end="")
        for value in hand_value:
            print(value,end=" ")
        print()
        return -1
    
    print(Fore.YELLOW + "Dealer hand value(s): ", end="")
    for value in hand_value:
        print(value,end=" ")
    print()
    if 21 in hand_value:
        return 1
    return 0

def stand(hand_value):
    max_hand = max([x for x in hand_value if x <= 21]) if [x for x in hand_value if x <= 21] else max(hand_value)
    print(Fore.BLUE + "You decide to Stand. Your hand value is ", max_hand, ".", sep="")
    return max_hand

def dealer_17(dealer_hand, dealer_value, max_hand, deck):
    while True:
        dealer_mx = dealer_hit(dealer_hand, dealer_value, deck)
        if dealer_mx == 1:
            return 21
        elif dealer_mx == -1:
            return -1
        else:
            dealer_validmx =  max(dealer_value)
            if dealer_validmx > max_hand or dealer_validmx == max_hand and dealer_validmx >= 17 or dealer_validmx >= 17 and len(dealer_value) == 1:
                return dealer_validmx
                


def deal(current_hand, dealer_hand, hand_value, dealer_value, deck):
    hit(current_hand, hand_value, deck, hit_choice=0)
    dealer_hit(dealer_hand, dealer_value, deck)
    return hit(current_hand, hand_value, deck, hit_choice=0)



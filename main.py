from deck_functions import deck_generation, shuffle_deck
from blackjack_functions import hit, stand, deal, dealer_17
from colorama import just_fix_windows_console, Fore
just_fix_windows_console()

def main():
    deck = deck_generation()
    shuffle_deck(deck)

    current_hand = []
    hand_value = set()
    dealer_hand = []
    dealer_value = set()
    hit_res = deal(current_hand, dealer_hand, hand_value, dealer_value, deck)
    max_hand = 0
    if hit_res == 1:
        print(Fore.MAGENTA + "BLACKJACK!")
        max_hand = 21
    else:
        while True:
            choice = input(Fore.WHITE + "Would you like to Hit (H/h) or Stand (S/s)? ")
            if choice in "hH":
                hit_res = hit(current_hand, hand_value, deck)
                if hit_res == -1:
                    print(Fore.RED + "You bust out! You lost!")
                    break
                elif hit_res == 1:
                    print(Fore.MAGENTA + "BLACKJACK!")
                    max_hand = 21
                    break
            elif choice in "sS":
                max_hand = stand(hand_value)
                break
    if hit_res != -1:
        max_dealer = dealer_17(dealer_hand, dealer_value, max_hand, deck)
        if max_hand > max_dealer:
            print(Fore.GREEN + "You won!")
        elif max_hand < max_dealer:
            print(Fore.RED + "You lost!")
        else:
            print(Fore.CYAN + "It's a stale draw!")
if __name__ == "__main__":
    main()
import card_reader


def print_card_id_callback(card):
    print("CARD ID: " + str(card))

if __name__ == "__main__":
    while True:
        print("Bring TAG closer...")
        print("")
        card_reader.read_card(print_card_id_callback)
 
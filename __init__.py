
from aqt import mw
from aqt.utils import showInfo
from aqt import gui_hooks


# The history of cards seen
card_history = []


def add_seen_card(reviewer, card, ease):
    """
    Adds a seen card to the `card_history` list

    Args:
        reviewer (aqt.reviewer.Reviewer)
        card (Card)
        ease (int)
    """

    card_history.append(card)

    showInfo(str(len(card_history)))

gui_hooks.reviewer_did_answer_card.append(add_seen_card)

def clear_card_history():
    """
    Clear the card history when the user exits the deck.  This saves a lot of memory.
    """

    card_history.clear()
    showInfo(str(len(card_history)))

gui_hooks.reviewer_will_end.append(clear_card_history)
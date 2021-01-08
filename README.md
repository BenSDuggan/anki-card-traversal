# Anki Card Traversal

An Anki add-on allowing traversal of previously seen cards.


## Install

Install aqt:

```
pip install aqt
```

## How it work

1) Hook (`gui_hooks.reviewer_did_answer_card`) captures every card that is seen
2) When the arrow key is used it goes back one card

x) When deck is exited (`gui_hooks.reviewer_will_end`), clear `card_history`.
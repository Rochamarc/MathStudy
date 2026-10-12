def update_cards(dd: dict, user_hand: list[str]) -> dict:
    """
    """

    for card in user_hand:
        dd[card] += 1

    return dd


def check_hand(your_hand: list) -> int:
    """
    Check a hand for:
    "Exodia the Forbidden One"
    "Left Arm of the Forbidden One"
    "Left Leg of the Forbidden One"
    "Right Arm of the Forbidden One"
    "Right Leg of the Forbidden One"

    Parameters
    ----------
    your_hand: list
        A list of five cards from the user's deck

    Returns
    -------
    cont : int
        If value is equal to five, you win the duel. max: 5
    """

    winning_hand = [
        "Exodia the Forbidden One",
        "Left Arm of the Forbidden One",
        "Left Leg of the Forbidden One",
        "Right Arm of the Forbidden One",
        "Right Leg of the Forbidden One"
    ]

    cont = 0
    for i in your_hand:

        if i in winning_hand:
            cont += 1

    return cont
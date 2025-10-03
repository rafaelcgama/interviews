from typing import List
from collections import defaultdict


def assess_risk(transactions: List[dict]) -> List[str]:
    AMT_MED = 5000 * 100
    AMT_HIGH = 10000 * 100
    SPEND_MED = 10000 * 100
    SPEND_HIGH = 20000 * 100

    total_spend = {}
    card_used = defaultdict(set)

    def compare_risk(a, b):
        order = {
            "low": 0,
            "medium": 1,
            "high": 2
        }
        return a if order[a] >= order[b] else b

    ratings = []

    for tx in transactions:
        user_id = tx.get("user_id")
        card_id = tx.get("card_id")
        amount = tx.get("amount_us_cents")

        # Update total spend and card used for user in each transaction iteration
        total_spend[user_id] = total_spend.get(user_id, 0) + amount
        card_used[user_id].add(card_id)

        # start at low, then raise as rules trigger
        risk = 'low'

        if amount > AMT_MED:
            risk = compare_risk(risk, 'medium')

        if amount > AMT_HIGH:
            risk = compare_risk(risk, 'high')

        if total_spend[user_id] > SPEND_MED:
            risk = compare_risk(risk, 'medium')

        if total_spend[user_id] > SPEND_HIGH:
            risk = compare_risk(risk, 'high')

        card_count = len(card_used[user_id])
        if card_count > 1:
            risk = compare_risk(risk, 'medium')

        if card_count > 2:
            risk = compare_risk(risk, 'high')

        ratings.append(risk)

    return ratings


if __name__ == "__main__":
    transactions = [
        {"id": 1, "user_id": 1, "amount_us_cents": 200000, "card_id": 1},
        {"id": 2, "user_id": 1, "amount_us_cents": 600000, "card_id": 1},
        {"id": 3, "user_id": 1, "amount_us_cents": 1100000, "card_id": 1},
        {"id": 4, "user_id": 2, "amount_us_cents": 1, "card_id": 2},
        {"id": 5, "user_id": 2, "amount_us_cents": 1, "card_id": 3},
        {"id": 6, "user_id": 2, "amount_us_cents": 1, "card_id": 4}
    ]

    result = {
        "risk_ratings": [
            "low",
            "medium",
            "high",
            "low",
            "medium",
            "high"
        ]
    }

    print(assess_risk(transactions) == result["risk_ratings"])

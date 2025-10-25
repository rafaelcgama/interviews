from typing import List, Dict
from collections import defaultdict

# Thresholds in cents (for clarity and easy adjustment)
THRESHOLDS = {
    "AMT_MED": 5_000 * 100,
    "AMT_HIGH": 10_000 * 100,
    "SPEND_MED": 10_000 * 100,
    "SPEND_HIGH": 20_000 * 100,
    "NUM_CARDS_MED": 1,
    "NUM_CARDS_HIGH": 2
}

# Risk ranking (higher = riskier)
RISK_LEVELS = {"low": 0, "medium": 1, "high": 2}


def get_higher_risk(a: str, b: str) -> str:
    """Return the higher of two risk levels."""
    return a if RISK_LEVELS[a] >= RISK_LEVELS[b] else b


def assess_risk(transactions: List[Dict], thresholds: Dict = THRESHOLDS) -> List[str]:
    """Assess risk level for each transaction based on thresholds."""
    total_spend = defaultdict(int)
    cards_used = defaultdict(set)
    ratings = []

    for tx in transactions:
        user_id = tx["user_id"]
        card_id = tx["card_id"]
        amount = tx["amount_us_cents"]

        # Update user tracking
        total_spend[user_id] += amount
        cards_used[user_id].add(card_id)
        card_count = len(cards_used[user_id])

        # Default risk
        risk = "low"

        # High-risk triggers (precedence) -> Once labeled as such, move on with the iteration
        if (
                amount > thresholds["AMT_HIGH"]
                or total_spend[user_id] > thresholds["SPEND_HIGH"]
                or card_count > thresholds["NUM_CARDS_HIGH"]
        ):
            ratings.append("high")
            continue

        # Medium-risk triggers
        if (
                amount > thresholds["AMT_MED"]
                or total_spend[user_id] > thresholds["SPEND_MED"]
                or card_count > thresholds["NUM_CARDS_MED"]
        ):
            risk = get_higher_risk(risk, "medium")

        ratings.append(risk)

    return ratings


if __name__ == "__main__":
    transactions = [
        {"id": 1, "user_id": 1, "amount_us_cents": 200_000, "card_id": 1},
        {"id": 2, "user_id": 1, "amount_us_cents": 600_000, "card_id": 1},
        {"id": 3, "user_id": 1, "amount_us_cents": 1_100_000, "card_id": 1},
        {"id": 4, "user_id": 2, "amount_us_cents": 1, "card_id": 2},
        {"id": 5, "user_id": 2, "amount_us_cents": 1, "card_id": 3},
        {"id": 6, "user_id": 2, "amount_us_cents": 1, "card_id": 4},
    ]

    # Expected output for quick comparison
    expected_results = {
        "risk_ratings": ["low", "medium", "high", "low", "medium", "high"]
    }

    result = assess_risk(transactions)
    assert result == expected_results["risk_ratings"], f"❌ Expected {expected_results['risk_ratings']}, got {result}"
    print("✅ Test passed!")

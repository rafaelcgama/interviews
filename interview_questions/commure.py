import csv
import requests
from typing import Any
from datetime import date, timedelta

API_BASE = "https://lichess.org/api"


def format_date_human(d: date) -> str:
    """
    Format `date(YYYY, M, D)` → "Month D" without leading zero.
    """
    return d.strftime("%B %d").lstrip("0")


def get_top_classical_users(count: int, variant: str) -> list[str]:
    resp = requests.get(f"{API_BASE}/player/top/{count}/{variant}")
    resp.raise_for_status()
    return [player["username"] for player in resp.json()['users']]


def get_player_rating_history(user: str) -> Any | None:
    resp = requests.get(url=f"{API_BASE}/user/{user}/rating-history")
    resp.raise_for_status()

    for variant in resp.json():
        if variant['name'].lower() == 'classical':
            return variant['points']
    return 0


def find_starting_rating(normalized_records: dict[date, int], start_date: date) -> int:
    """
    Find the latest rating on or before `start_date`.
    If none exists, use the earliest available rating.
    """
    # all record-dates ≤ start_date
    dates_before_start_date = [d for d in normalized_records.keys() if d <= start_date]
    if dates_before_start_date:
        return normalized_records[max(dates_before_start_date)]
    # fallback to the very first record
    return normalized_records[min(normalized_records.keys())]


def generate_daily_ratings(records: list[list[int]], period_days: int = 30, end_date: date | None = None) -> dict[
    date, int]:
    """
    Given a list of records [year, month, day, rating], returns a dict
    mapping each date in the last `period_days` ending at `end` (inclusive)
    to the player's rating on that day, carrying forward the last known rating.

    records: List of [year, month, day, rating]
    period_days: Number of days to go back from `end`
    end_date: A datetime.date; defaults to None
    """
    # 1. Normalize records into a dict: date -> rating
    normalized_records = {
        date(year, month + 1, day): rating  # Api says January == 0 so +1 must be added to months
        for year, month, day, rating in records
    }

    # 2. Define range
    if not end_date:
        end_date = date.today()
    start_date = end_date - timedelta(days=period_days - 1)

    # 3. finds starting rating
    last_rating = find_starting_rating(normalized_records, start_date)

    # 4. Build daily ratings in one pass
    daily = {}
    for day in (start_date + timedelta(days=i) for i in range(period_days)):
        if day in normalized_records:
            last_rating = normalized_records[day]
        daily[day] = last_rating

    return daily


def print_top_50_classical_players() -> None:
    top_50_classical_users = get_top_classical_users(50, 'classical')
    print("\nTop 50 Classical Players:")
    for user in top_50_classical_users:
        print(user)


def print_last_30_day_rating_for_top_player(end_date: date, variant: str = 'classical') -> None:
    top_player = get_top_classical_users(1, variant)[0]
    top_player_rating_history = get_player_rating_history(top_player)
    last_30 = generate_daily_ratings(top_player_rating_history, 30, end_date)

    formatted = {format_date_human(d): r for d, r in last_30.items()}
    reversed_formatted = dict(reversed(list(formatted.items())))  # Python 3.7+ preserves insertion order
    print((top_player, reversed_formatted))


def generate_rating_csv_for_top_50_classical_players(end_date: date, variant: str = 'classical',
                                                     period_days: int = 30) -> None:
    users = get_top_classical_users(50, variant)
    start_date = end_date - timedelta(days=period_days - 1)

    # Header: username + formatted dates in ascending order
    date_list = [start_date + timedelta(days=i) for i in range(period_days)]
    header = ["username"] + [d.strftime("%Y-%m-%d") for d in date_list]  # Customized date format for the header

    filename = 'top_50_classical_players_ratings.csv'
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for user in users:
            print(f"Generating ratings for {user}...")
            history = get_player_rating_history(user)
            daily = generate_daily_ratings(history, period_days)
            row = [user] + [daily[d] for d in date_list]
            writer.writerow(row)

    print(f"{filename} created.")


if __name__ == "__main__":
    END_DATE = date.today()
    VARIANT = 'classical'

    # Task 1
    print_top_50_classical_players()

    # Task 2
    print_last_30_day_rating_for_top_player(END_DATE, VARIANT)

    # Task 3
    generate_rating_csv_for_top_50_classical_players(END_DATE, VARIANT)

import datetime
import calendar


def bill_for(month, active_subscription, users):
    # your code here!
    if not users or not active_subscription:
        return 0.00

    total = 0.00
    month_datetime = datetime.datetime.strptime(month, '%Y-%m').date()
    rate = active_subscription['monthly_price_in_dollars']
    for user in users:
        start_date = user['activated_on']
        end_date = last_day_of_month(datetime.date.today()) if user['deactivated_on'] is None else user[
            'deactivated_on']

        start_day_bill = first_day_of_month(month_datetime)
        end_day_bill = last_day_of_month(month_datetime)

        if month < start_date.strftime("%Y-%m") or month > end_date.strftime("%Y-%m"):
            continue

        if month == start_date.strftime("%Y-%m"):
            start_day_bill = start_date

        if month == end_date.strftime("%Y-%m"):
            end_day_bill = end_date

        total += pro_rated(month_datetime, start_day_bill, end_day_bill, rate)

    return round(total, 2)


def pro_rated(month, start_day, end_day, rate):
    num_days_month = (next_day(last_day_of_month(month)) - first_day_of_month(month)).days
    num_days_used = (next_day(end_day) - start_day).days

    return (num_days_used * rate) / num_days_month


####################
# Helper functions #
####################

def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:

    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)


def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:

    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)


def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:

    Input type: datetime.date
    Output type: datetime.date
    """
    return date + datetime.timedelta(days=1)

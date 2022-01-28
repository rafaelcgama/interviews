import pandas as pd
import datetime
import calendar


def bill_for(month, active_subscription, users):
    # your code here!
    if not users or not active_subscription:
        return 0.00

    total = 0.00
    rate = active_subscription['monthly_price_in_dollars']
    for user in users:
        start_date = user['activated_on']
        end_date = last_day_of_month(datetime.date.today()) if user['deactivated_on'] is None else user[
            'deactivated_on']

        df_user_subscribed_range = get_range(start_date, end_date)

        total += pro_rate(month, df_user_subscribed_range, rate)

    return round(total, 2)


def get_range(start, end):
    df = pd.DataFrame({
        'month': pd.date_range(start, end),
        'day': 1
    })
    df['month'] = df['month'].apply(lambda x: x.strftime("%Y-%m"))
    return df.groupby(by='month')['day'].sum()


def pro_rate(month, user_range, rate):
    month_datetime = datetime.datetime.strptime(month, '%Y-%m').date()
    num_days_month = (next_day(last_day_of_month(month_datetime)) - first_day_of_month(month_datetime)).days
    num_days_used = user_range[month] if month in user_range else 0

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

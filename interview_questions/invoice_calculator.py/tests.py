import datetime
import unittest
from solution import bill_for

user_signed_up = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2019, 1, 10),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

user_deactivated = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 1, 4),
        'deactivated_on': datetime.date(2018, 12, 4),
        'customer_id': 1,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2019, 1, 1),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

constant_users = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

activated_deactivated_same_month = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2019, 1, 4),
        'deactivated_on': datetime.date(2019, 1, 20),
        'customer_id': 1,
    }
]

invoice_limited_range = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2019, 1, 4),
        'deactivated_on': datetime.date(2019, 1, 20),
        'customer_id': 1,
    }
]

new_plan = {
    'id': 1,
    'customer_id': 1,
    'monthly_price_in_dollars': 4
}

no_users = []

no_plan = None


class Test(unittest.TestCase):
    def test_works_when_the_customer_has_no_active_users_during_the_month(self):
        self.assertAlmostEqual(bill_for('2019-01', new_plan, no_users), 0.00, delta=0.01)

    def test_works_when_everything_stays_the_same_for_a_month(self):
        self.assertAlmostEqual(bill_for('2019-01', new_plan, constant_users), 8.00, delta=0.01)

    def test_works_when_a_user_is_activated_during_the_month(self):
        self.assertAlmostEqual(bill_for('2019-01', new_plan, user_signed_up), 10.84, delta=0.01)

    def test_works_when_there_is_no_plan(self):
        self.assertAlmostEqual(bill_for('2019-01', no_plan, user_signed_up), 0.00, delta=0.01)

    def test_works_when_a_user_is_deactivated_during_the_month(self):
        self.assertAlmostEqual(bill_for('2019-01', new_plan, user_deactivated), 8.00, delta=0.01)

    def test_works_when_a_user_is_activated_and_deactivated_during_same_month(self):
        self.assertAlmostEqual(bill_for('2019-01', new_plan, activated_deactivated_same_month), 6.19, delta=0.01)

    def test_works_when_a_month_is_before_user_range(self):
        self.assertAlmostEqual(bill_for('2018-01', new_plan, invoice_limited_range), 0.00, delta=0.01)

    def test_works_when_a_month_is_after_user_range(self):
        self.assertAlmostEqual(bill_for('2021-01', new_plan, invoice_limited_range), 0.00, delta=0.01)

import unittest
from app import app

VALID = {
    'V':'N','C':'700','D':'0','MDP':'10000','MMI':'5000',
    'TMFR':'25','MBR':'35','MMA':'200000','MMR':'6','JN':'0',
    'PPF':'Y','LPF':'N','FN':'7','BCH7':'4','BCH13DC':'2',
    'BCH13DS':'4','OC':'1'
}

class LoanValidationTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_valid_request(self):
        response = self.client.post('/', data=VALID)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Loan Recommendation', response.get_json())

    def test_missing_field(self):
        data = dict(VALID)
        data.pop('C')
        self.assertEqual(self.client.post('/', data=data).status_code, 400)

    def test_zero_mortgage(self):
        data = dict(VALID, MMA='0')
        self.assertEqual(self.client.post('/', data=data).status_code, 400)

    def test_invalid_credit_score(self):
        data = dict(VALID, C='not-a-number')
        self.assertEqual(self.client.post('/', data=data).status_code, 400)

    def test_infinite_loan_amount(self):
        data = dict(VALID, MMA='inf')
        self.assertEqual(self.client.post('/', data=data).status_code, 400)

if __name__ == '__main__':
    unittest.main()

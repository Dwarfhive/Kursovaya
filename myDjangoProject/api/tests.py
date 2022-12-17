from django.test import TestCase
from rest_framework.test import APITestCase

class diagTests(APITestCase):
    def test_diag_correct(self):
        url="/api/3/3/1_2_3_4_5_6_7_8_9"
        responce=self.client.get(url)
        self.assertEqual(responce.data,{
            "cols":3,
            "rows":3,
            "args":"1_2_3_4_5_6_7_8_9",
            "result": "[[1 0 0]\n [0 5 0]\n [0 0 9]]",
        })

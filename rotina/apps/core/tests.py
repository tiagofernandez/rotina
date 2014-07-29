from datetime import datetime
from django.test import TestCase

from rotina.apps.core.models import Routine

class RoutineTestCase(TestCase):

    def test_generate_code(self):
        code = Routine.generate_code()
        self.assertIsNotNone(code)
        code_length = len(code)
        self.assertTrue(code_length >= 6 and code_length <= 10)

    def test_next_occurrence(self):
        routine = Routine(cron='0 12 * * MON-FRI')
        next_occurrence = routine.next_occurrence(base=datetime(2014, 5, 29, 18, 0))
        self.assertEquals(next_occurrence, datetime(2014, 5, 30, 12, 0))

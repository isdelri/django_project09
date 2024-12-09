# Test for the polling app.and

from django.test import TestCase
from .models import Poll


class PollTestCase(TestCase):
    def setUp(self):
        Poll.objects.create(title="Sample Poll", score=0)

    def test_poll_score(self):
        poll = Poll.objects.get(title="Sample Poll")
        self.assertEqual(poll.score, 0)

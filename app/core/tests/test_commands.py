import unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTests(TestCase):
    def test_wait_for_db_ready(self):
        """test waiting for db when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
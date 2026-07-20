"""  this tests all files"""

from django.test import SimpleTestCase
from .cal import add
class Test_cal(SimpleTestCase):
    def test_cal(self):
        res=add(5,10)
        
        assert res==15
         
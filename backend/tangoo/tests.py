from django.test import TestCase
from .models import Tangoo


# Create your tests here.
def create_tangoo(arg1, arg2, arg3):
    return Tangoo.objects.create(phrase_ja=arg1, phrase_en=arg2, word_en=arg3)


class TangooTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_tangoo("日本語は難しい", "Japanese is difficult", "Japanese")

    def test_tangoo_content(self):
        tangoo = Tangoo.objects.get(id=1)
        self.assertEquals(tangoo.word_en, 'Japanese')
        self.assertEquals(tangoo.phrase_en, 'Japanese is difficult')
        self.assertEquals(tangoo.phrase_ja, '日本語は難しい')

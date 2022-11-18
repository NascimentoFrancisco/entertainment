from django.test import TestCase
from django.utils import timezone
from accounts.models import User
from entertainment.models import Entertainment

class TestsEntertainment(TestCase):

    def setUp(self):
        
        self.user = User.objects.create_user(
            name = 'Usuario teste',
            email = 'teste@gmail.com',
            password = 'Teste@0'
        )
        
        self.entertainment = Entertainment.objects.create(
            
            user = self.user,
            title = 'Teste de criação',
            type = 'teste',
            status = False,
            review = 'Testando o model',
            end_date = timezone.now()
        )
        
        return super().setUp()

    def test_create_entertainment_correct(self):

        self.assertEqual(self.entertainment.title,'Teste de criação')
        self.assertEqual(self.entertainment.type,'teste')
        self.assertFalse(self.entertainment.status)
        self.assertEqual(self.entertainment.review,'Testando o model')
        self.assertEqual(self.entertainment.end_date.day,timezone.now().date().day)
        
    def test_update_status_entertainment(self):

        self.entertainment.status = False
        self.entertainment.save()

        self.assertFalse(self.entertainment.status)
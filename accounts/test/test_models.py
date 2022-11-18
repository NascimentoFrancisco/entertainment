from django.test import TestCase
from accounts.models import User


class TesteModelsUser(TestCase):

    
    def setUp(self):
        self.user = User.objects.create_user(
            name = 'Usuario teste',
            email = 'teste@gmail.com',
            password = 'Teste@0'
        )
        
        return super().setUp()
    
    def test_create_user_correct(self):
        
        self.assertEqual(self.user.name,'Usuario teste')
        self.assertEqual(self.user.email,'teste@gmail.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)    

    def test_change_email_and_name_user(self):
               
        self.user.name = 'Usuario teste1'
        self.user.email = 'teste1@gmail.com'
        
        self.user.save()

        self.assertEqual(self.user.name,'Usuario teste1')
        self.assertEqual(self.user.email,'teste1@gmail.com')
        
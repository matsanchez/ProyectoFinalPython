import os
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

#Realizamos un testeo del funcionamiento para el CRUD del Post, donde configuramos datos test para recrear el funcionamiento de crear un Post.

class PostModelTest(TestCase):
    #Este metodo propio de Django, se ejecuta antes de cada prueba, se configura para que tenga el estado necesario para las pruebas
    #Se creo un diccionario para Post y un usuario para la prueba
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.post_data = {
            'title': 'Test Title',
            'subtitle': 'Test Subtitle',
            'body': 'Test Body',
            'author': self.user,
            'image': 'posts/test_image.jpg', 
        }

    #Creamos un Post
    def test_post_creation(self):
        post = Post.objects.create(**self.post_data)
        self.assertEqual(post.title, 'Test Title')
        self.assertEqual(post.subtitle, 'Test Subtitle')
        self.assertEqual(post.body, 'Test Body')
        self.assertEqual(post.author, self.user)
        self.assertEqual(str(post), 'Test Title Test Subtitle')

    def test_default_date(self):
        post = Post.objects.create(**self.post_data)
        self.assertIsNotNone(post.date)

    def test_image_upload_to(self):
        post = Post.objects.create(**self.post_data)
        self.assertEqual(post.image.field.upload_to, 'posts/')

    #Testea que que la ruta de imagen corresponda al Post
    # Compara las rutas, se tuvo que normalizar las barras diagonales invertidas
    def test_image_path(self):
        post = Post.objects.create(**self.post_data)
        expected_path = os.path.join('posts', 'test_image.jpg')
        actual_path = os.path.normpath(post.image.name)
        self.assertEqual(actual_path, expected_path)


    #Testeamos el CRUD de editar el Post
    def test_post_update(self):
        post = Post.objects.create(**self.post_data)
        new_data = {
            'title': 'Updated Title',
            'subtitle': 'Updated Subtitle',
            'body': 'Updated Body Content',
        }
        for key, value in new_data.items():
            setattr(post, key, value)
        post.save()

        updated_post = Post.objects.get(pk=post.pk)
        self.assertEqual(updated_post.title, 'Updated Title')
        self.assertEqual(updated_post.subtitle, 'Updated Subtitle')
        self.assertEqual(updated_post.body, 'Updated Body Content')


    #Crud DELETE del Post
    def test_post_deletion(self):
        post = Post.objects.create(**self.post_data)
        post_id = post.id
        post.delete()

        with self.assertRaises(Post.DoesNotExist):
            deleted_post = Post.objects.get(pk=post_id)

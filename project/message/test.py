from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post
from .models import Comments

#Recreamos el funcionamiento de los comentarios en un Post


class CommentsModelTest(TestCase):

    #Generamos con el metodo setUP, un usuario, post y comentario

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.post = Post.objects.create(
            title='Test Titulo',
            subtitle='Test Subtitulo',
            body='Test Mensaje',
            author=self.user,
            image='posts/test_image.jpg',
        )
        self.comment_data = {
            'post': self.post,
            'body': 'Test Comentario',
            'author': self.user,
        }

    #Este metodo verifica la representacion de cadena que devuelva el mensaje de el nombre del usuario
    #Si modificamos el "Test Comentario testuser" nos daria invalido el test. Lo mismo aplica para cualquier informacion del setUp.
    def test_str_method(self):
        comment = Comments.objects.create(**self.comment_data)
        self.assertEqual(str(comment), 'Test Comentario testuser')

    def test_comment_creation(self):
        comment = Comments.objects.create(**self.comment_data)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.body, 'Test Comentario')
        self.assertEqual(comment.author, self.user)
        self.assertIsNotNone(comment.date)
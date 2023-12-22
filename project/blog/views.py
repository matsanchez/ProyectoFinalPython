from django.shortcuts import redirect
from django.contrib import messages
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, FormView, View
from django.views.generic.detail import SingleObjectMixin
from message.forms import MessagePostForm
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

# Create your views here.
class ListPost(ListView):
    model= Post
    template_name = 'blog/list_post.html'
    context_object_name = 'posts'


class DetailPost(DetailView):
    model= Post
    template_name='blog/detail_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessagePostForm()
        return context


class PostCommentFormView(LoginRequiredMixin,SingleObjectMixin, FormView):
    template_name='blog/detail_post.html'
    form_class = MessagePostForm
    model = Post
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args,**kwargs)
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.post = self.object
        f.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('blog:detail_post', kwargs={'pk': self.object.id}) + '#comments-section'


class DetailPostView(View):
    def get(self, request, *args, **kwargs):
        view = DetailPost.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostCommentFormView.as_view()
        return view(request, *args, **kwargs)
    

class CreatePost(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    form_class = PostForm
    login_url = reverse_lazy('account:login')

    def test_func(self):
        # Este método se llama para determinar si el usuario pasa la prueba.
        # Devuelve True si el usuario puede acceder, False de lo contrario.
        return not self.request.user.is_authenticated
    
    def post(self, request, *args, **kwargs):
        logged_in_user = request.user
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = logged_in_user
            new_post.save()
            pk = new_post.id
            messages.add_message(request=request, level=messages.SUCCESS, message="¡Post Creado Exitosamente!")
        return redirect(f'/blog/pages/{pk}')
    

class EditPostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','subtitle', 'body', 'image']
    template_name = 'blog/edit_post.html'
    login_url = reverse_lazy('account:login')

    def post(self, request, *args, **kwargs):
        messages.add_message(self.request,level=messages.SUCCESS, message="¡El post fue editado correctamente!")
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail_post', kwargs={'pk':pk})
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

class DeletePostView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list_post')
    login_url = reverse_lazy('account:login')
    
    def test_func(self):
        messages.add_message(self.request,level=messages.INFO, message="¡El Post fue eliminado Correctamente!")
        post = self.get_object()
        return self.request.user == post.author




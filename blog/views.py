from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from rest_framework import generics
from .serializers import PostSerializer, CommentSerializer

def lista_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/lista_post.html', context)

def exibe_post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.all()
    context = {'post': post, 'comments': comments}
    return render(request, 'blog/exibe_post.html', context)

def criar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(lista_posts)
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'blog/criar_post.html', context)

def adicionar_comentario(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(exibe_post, post_id)
    else:
        form = CommentForm()
    context = {'post': post, 'form': form, 'comments': comments}
    return render(request, 'blog/exibe_post.html', context)

# View responsavel por listar e criar Posts
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# View responsavel por detalhar, atualizar e apagar um post especifico
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# View responsavel por listar e criar Comments
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# View responsavel por detalhar, atualizar e apagar um comment especifico
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
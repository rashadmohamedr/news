from django.views.generic import ListView,DetailView,UpdateView,DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Article 
# Create your views here.
class ArticleListView(LoginRequiredMixin, ListView):
    model=Article
    template_name="article_list.html"
    context_object_name="articles"

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model=Article
    template_name="article_detail.html"
    
class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Article
    template_name="article_edit.html"
    fields=(
        "title",
        "body"
    )
    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user #type: ignore
    
class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Article
    template_name="article_delete.html"
    success_url=reverse_lazy("article_list")
    def test_func(self) -> bool | None:
        return self.get_object().author == self.request.user #type: ignore
    
    
class ArticleCreateView(LoginRequiredMixin, CreateView):
    model=Article
    template_name="article_new.html"
    fields=("title","body",)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
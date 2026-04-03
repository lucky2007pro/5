from django.shortcuts import render
from .models import Product, Category, User, Review
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    class Meta:
        ordering = ['-id']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    class Meta:
        ordering = ['-id']

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'category', 'price', 'image', 'description']
    template_name = 'products/product_form.html'
    class Meta:
        ordering = ['-id']

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'category', 'price', 'image', 'description']
    template_name = 'products/product_form.html'
    class Meta:
        ordering = ['-id']

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/'
    template_name = 'products/product_delete.html'

class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    class Meta:
        ordering = ['-id']

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'products/category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'desc']
    template_name = 'products/category_form.html'

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'desc']
    template_name = 'products/category_form.html'

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'
    template_name = 'products/category_delete.html'

class UserListView(ListView):
    model = User
    template_name = 'products/user_list.html'
    class Meta:
        ordering = ['-id']

class UserDetailView(DetailView):
    model = User
    template_name = 'products/user_detail.html'
    class Meta:
        ordering = ['-id']

class UserCreateView(CreateView):
    model = User
    fields = ['full_name', 'year_of_birth', 'username']
    template_name = 'products/user_form.html'
    class Meta:
        ordering = ['-id']

class UserUpdateView(UpdateView):
    model = User
    fields = ['full_name', 'year_of_birth', 'username']
    template_name = 'products/user_form.html'
    class Meta:
        ordering = ['-id']

class UserDeleteView(DeleteView):
    model = User
    success_url = '/'
    template_name = 'products/user_delete.html'
    class Meta:
        ordering = ['-id']

class ReviewListView(ListView):
    model = Review
    template_name = 'products/review_list.html'
    class Meta:
        ordering = ['-id']

class ReviewCreateView(CreateView):
    model = Review
    fields = ['product', 'user', 'rating', 'comment']
    template_name = 'products/review_form.html'
    class Meta:
        ordering = ['-id']

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['product', 'user', 'rating', 'comment']
    template_name = 'products/review_form.html'

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = '/'
    template_name = 'products/review_delete.html'
    class Meta:
        ordering = ['-id']


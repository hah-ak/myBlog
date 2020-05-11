from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Algorithm
from .forms import search_forms

# paging 메소드
def paging(self,context):
    paginator = context['paginator']
    page_number_range = 5
    max_index = len(paginator.page_range)
    
    page = self.request.GET.get('page')
    current_page = int(page) if page else 1
    start_index = int((current_page-1)//page_number_range)*page_number_range
    end_index = start_index+page_number_range
    if end_index >= max_index:
        end_index = max_index
    
    page_range = list(range(start_index+1,end_index+1))
    context['page_range'] = page_range
    
# mainpage 함수로 구현
def main(request):
    Algorithms = Algorithm.objects.order_by('created_date')
    
    paginator = Paginator(Algorithms,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    page_number_range = 5
    max_index = paginator.num_pages
    current_page = int(page_number) if page_number else 1
    start_index = int((current_page-1)//page_number_range)*page_number_range
    end_index = start_index+page_number_range
    if end_index >= max_index:
        end_index = max_index

    page_range = paginator.page_range[start_index:end_index]
    
    context = {'Algorithms':Algorithms,'page_range':page_range,'page_obj' : page_obj}
    return render(request,'blog/index.html',context)

class CodeDetailView(generic.DetailView):
    model = Algorithm
    template_name = "blog/code_page.html"
    context_object_name = 'Algorithm'

# def codes(request, index, post_id):
#     post = Post.objects.get(pk=post_id)
#     context = {'post':post,'index':index}
#     return render(request, 'blog/codes.html', context)


class AlgorithmTemplateVeiw(generic.TemplateView):
    template_name = 'blog/Algorithm_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(AlgorithmTemplateVeiw, self).get_context_data(**kwargs)
        context[object_list] = ['Algorithm']
        return context
    
    
class AlgorithmVeiw(generic.ListView):
    model = Algorithm
    queryset = Algorithm.objects.order_by('created_date')
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super(AlgorithmVeiw, self).get_context_data(**kwargs)
        paging(self,context)
        return context
    
    

class SSEAView(generic.ListView):
    queryset = Algorithm.objects.filter(site = 'SSEA')
    queryset = queryset.order_by('created_date')
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super(SSEAView, self).get_context_data(**kwargs)
        paging(self,context)
        return context
    
    
class programmersView(AlgorithmVeiw ,generic.ListView):
    queryset = Algorithm.objects.filter(site = 'programmers')
    queryset = queryset.order_by('created_date')
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super(programmersView, self).get_context_data(**kwargs)
        paging(self,context)
        return context

    
# def SSEA(request):
#     posts = Post.objects.order_by('created_date')
#     context = {'posts' : posts, 'index' : 'SSEA'}
#     return render(request, 'blog/SSEA.html',context)

# class SearchView(generic.ListView):
#     template_name = 'blog/search.html'
#     context_object_name = 'results'
#     def get_queryset(self):
#         # queryset = super(SearchView, self).get_queryset()
#         # search = self.request.GET['search']
#         search = search_forms(self.request.GET)
#         if search.is_valid():
#             queryset = Algorithm.objects.filter(title__contains=search)
#         return queryset

def Search(request):
    search = request.GET['search']
    results = Algorithm.objects.filter(title__contains=search)
    return render(request,'blog/search.html', {'results':results,'notfound':search})
    
    
    
    
    
def fashion(request):
    context = {}
    return render(request, 'blog/fashion.html',context)

def contact(request):
    context = {}
    return render(request, 'blog/contact.html',context)

def about(request):
    context = {}
    return render(request, 'blog/about.html',context)


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Algorithm


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
    return render(request,'blog/main.html',context)

class CodeDetailView(generic.DetailView):
    model = Algorithm
    template_name = "blog/code_page.html"
    context_object_name = 'Algorithm'

# def codes(request, index, post_id):
#     post = Post.objects.get(pk=post_id)
#     context = {'post':post,'index':index}
#     return render(request, 'blog/codes.html', context)

class SSEAView(generic.ListView):
    paginate_by = 5
    template_name = 'blog/SSEA.html'
    context_object_name = 'Algorithms'
    def get_queryset(self):
        queryset = Algorithm.objects.filter(site = 'SSEA')
        queryset = queryset.order_by('created_date')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(SSEAView, self).get_context_data(**kwargs)
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
        return context
    


class programmersView(generic.ListView):
    paginate_by = 5
    template_name = 'blog/programmers.html'
    context_object_name = "Algorithms"
    def get_queryset(self):
        queryset = Algorithm.objects.filter(site = 'programmers')
        queryset = queryset.order_by('created_date')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(programmersView, self).get_context_data(**kwargs)
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
        return context
    
# def SSEA(request):
#     posts = Post.objects.order_by('created_date')
#     context = {'posts' : posts, 'index' : 'SSEA'}
#     return render(request, 'blog/SSEA.html',context)

class SearchView(generic.ListView):
    template_name = 'blog/search.html'
    context_object_name = 'results'
    search = ""
    def get_queryset(self):
        # queryset = super(SearchView, self).get_queryset()
        search = self.request.GET['search']
        if search:
            queryset = Algorithm.objects.filter(title__contains=search)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        search = self.request.GET['search']
        context['notfound'] = search
        return context
    
    
def fashion(request):
    context = {}
    return render(request, 'blog/fashion.html',context)

def contact(request):
    context = {}
    return render(request, 'blog/contact.html',context)

def about(request):
    context = {}
    return render(request, 'blog/about.html',context)


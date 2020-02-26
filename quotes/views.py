from django.shortcuts import render,redirect, get_object_or_404
from . models import Quote,QuoteCategory
from django.contrib.auth.decorators import login_required
from . forms import CreateForm,editForm
import django.utils.timezone
from pytz import timezone
import pytz
from django.db.models import Prefetch
from registration.models import User
from django.core.paginator import Paginator



# Create your views here.

def home(request):
    all_quotes=Quote.objects.order_by('-pub_date').prefetch_related('author')
    paginator = Paginator(all_quotes, 9, orphans=5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'quotes/home.html', {'page_obj': page_obj})
    # return render(request,'quotes/home.html',{'quotes': all_quotes} )


@login_required()
def create(request):
    # if request.user.is_anonymous:
    #     messages.add_message(request, messages.INFO,
    #                          'You must be logged in')
    #     return redirect('your_login_views')
    # else:
    #     # do smothing
    #     return redirect(request, 'your_page.html')
    if request.method=='POST':
        #create a form instance and populate it with data from the request:
        form=CreateForm(request.POST)
        if form.is_valid():
            # newquote=Quote()
            # newquote.quote=form.cleaned_data['quote']
            # newquote.author=request.user
            # newquote.quote_categories=form.cleaned_data['quote_categories']
            # newquote.save()

            #when you get most of your model data from a form,
            #but need to populate some null=False fields with non-form data. 
            pending_author=form.save(commit=False)
            if request.user.is_authenticated:
                pending_author.author = request.user
            pending_author.save()
            form.save_m2m()
            return redirect('home')
        else:
            return render(request, 'quotes/create.html',{'form':form})


    else:
        form=CreateForm()
        return render(request, 'quotes/create.html', {'form':form})


# def set_timezone(request):
#     if request.method == 'POST':
#         request.session['django_timezone'] = request.POST['timezone']
#         return redirect('/')
#     else:
#         return render(request, 'quotes/template.html', {'timezones': pytz.common_timezones})

@login_required()
def editQuote(request, quote_id):

    singlequote=get_object_or_404(Quote,id=quote_id)
    if request.method=='POST':
        form=editForm(request.POST)
        if form.is_valid():
            singlequote.quote=form.cleaned_data['new_quote']
            category=form.cleaned_data['new_category']
            singlequote.save()
            # newCategory=QuoteCategory.objects.filter(title__in=category)
            singlequote.categories.set(category)
            return redirect('profile',user_id=request.user.id)
        else:
            return render(request, 'quotes/quoteEdit.html',{'form':form, 'quote':singlequote})
    if request.method=='GET':
        form=editForm(initial={'new_quote':singlequote.quote})
        return render(request, 'quotes/quoteEdit.html',{'form':form, 'quote':singlequote})
    
# class quoteUpdateView(UpdateView):
#     model=Quote
#     template_name='quotes/quoteEdit.html'
#     form_class=CreateForm
#     def get_object(self, **kwargs):
#         #get the uuid out of the url group and find the Product
#         return Quote.objects.filter(id=self.kwargs.get('uuid')).first()

@login_required()
def deleteQuote(request, quote_id):
    qt=get_object_or_404(Quote,id=quote_id)
    if request.method=='POST':
        qt.delete()
        return redirect('profile',user_id=request.user.id)
    else:
        return redirect('profile',user_id=request.user.id)

@login_required()
def quoteCat(request, quote_cat):
    quoteCat=get_object_or_404(QuoteCategory, title=quote_cat)
    newquoteCat=quoteCat.quote_set.all()   
    return render(request,'quotes/quoteCat.html', {'category':newquoteCat, 'status':'active', 'QuoteCategory':quote_cat})        


@login_required()   
def Search(request):
    queryAuthor = request.GET.get('q')
    publicProfile=User.objects.filter(username__icontains=queryAuthor).prefetch_related()
    return render(request, 'quotes/showSearchResult.html',{'profile':publicProfile, 'searchResult':queryAuthor})


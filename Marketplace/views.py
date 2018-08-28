from django.shortcuts import render, get_object_or_404, redirect 
from django.db.models import Q
from itertools import chain
import time
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponseRedirect


from .models import market, article, Liked, Comment, Internship, UserProfile, Friend, Workshop 

from Marketplace.forms import marketForm, articleForm, CommentForm, InternshipForm, UserProfileForm, WorkshopForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User # added

from notify.signals import notify   # django notify





# datetime = time.strftime('%A, %d %B %Y', time.localtime(time.time()))
# context = {'today' : datetime}


def index(request):
#    members = User.objects.all()
#    topics = article.objects.all()
    articleboard = article.objects.filter(approved_article = True).order_by('-pk').order_by('-likes')[:20]
    return render(request, 'Marketplace/index.html', {'board' : articleboard})
    
def directory(request, ):
    if request.method == 'GET':
        selection = request.GET.get('dropdown', None)
        if selection == 'Agriculture':
            markets = market.objects.all().filter(section = 'Agriculture').order_by('-pk')
            paginator = Paginator(markets, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/directory.html', {'market' : page})  
        elif selection == 'IT/Programming':
            markets = market.objects.all().filter(section = 'IT/Programming').order_by('-pk')
            paginator = Paginator(markets, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/directory.html', {'market' : page})            
        elif selection == 'Education':
            markets = market.objects.all().filter(section = 'Education').order_by('-pk')
            paginator = Paginator(markets, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/directory.html', {'market' : page})              
        elif selection == 'Event Management':
            markets = market.objects.all().filter(section = 'Event Management').order_by('-pk')
            paginator = Paginator(markets, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/directory.html', {'market' : page})               
        elif selection == 'Catering/Hospitality':
            markets = market.objects.all().filter(section = 'Catering/Hospitality').order_by('-pk')
            paginator = Paginator(markets, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/directory.html', {'market' : page})            
        elif selection == 'Fashion':
            markets = market.objects.all().filter(section = 'Fashion').order_by('-pk')
            paginator = Paginator(markets, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/directory.html', {'market' : page})    
        elif selection == 'General':
            markets = market.objects.all().filter(section = 'General').order_by('-pk')
            paginator = Paginator(markets, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/directory.html', {'market' : page})
        elif selection == 'Health':
            markets = market.objects.all().filter(section = 'Health').order_by('-pk')
            paginator = Paginator(markets, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/directory.html', {'market' : page})
        elif selection == 'Technology':
            markets = market.objects.all().filter(section = 'Technology').order_by('-pk')
            paginator = Paginator(markets, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/directory.html', {'market' : page})  
        elif selection == 'All':
            markets = market.objects.all().order_by('-pk')
            paginator = Paginator(markets, 50)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/directory.html', {'market' : page})
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
           
            
     

def contact(request):
    return render(request, 'Marketplace/contact.html', {'form' : marketForm})

def policy(request):    
    return render(request, 'Marketplace/policy.html')    
    
def about(request):
    return render(request, 'Marketplace/aboutpage.html')

@login_required    
def addmarket(request):
    mform = marketForm()
    if request.method == 'POST':
        form = marketForm(request.POST, request.FILES)
        if form.is_valid():
            market = form.save(commit = False)
            market.added_by = request.user
            market.save()
        return redirect('marketdetail', pk=market.pk)
    else:
        return render(request, 'Marketplace/contact.html', {'form' : mform})

       
def articleview(request, ):
    if request.method == 'GET':
        selection = request.GET.get('dropdown', None)
        if selection == 'Agriculture':
            articles = article.objects.all().filter(section = 'Agriculture').order_by('-pk')
            paginator = Paginator(articles, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/article.html', {'article' : page}) 
        elif selection == 'IT/Programming':
            articles = article.objects.all().filter(section = 'IT/Programming').order_by('-pk')
            paginator = Paginator(articles, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/article.html', {'article' : page})            
        elif selection == 'Education':
            articles = article.objects.all().filter(section = 'Education').order_by('-pk')
            paginator = Paginator(articles, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/article.html', {'article' : page})             
        elif selection == 'Event Management':
            articles = article.objects.all().filter(section = 'Event Management').order_by('-pk')
            paginator = Paginator(articles, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/article.html', {'article' : page})              
        elif selection == 'Catering/Hospitality':
            articles = article.objects.all().filter(section = 'Catering/Hospitality').order_by('-pk')
            paginator = Paginator(articles, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/article.html', {'article' : page})           
        elif selection == 'Fashion':
            articles = article.objects.all().filter(section = 'Fashion').order_by('-pk')
            paginator = Paginator(articles, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/article.html', {'article' : page})   
        elif selection == 'General':
            articles =article.objects.all().filter(section = 'General').order_by('-pk')
            paginator = Paginator(articles, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/article.html', {'article' : page})
        elif selection == 'Health':
            articles =article.objects.all().filter(section = 'Health').order_by('-pk')
            paginator = Paginator(articles, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/article.html', {'article' : page})
        elif selection == 'Technology':
            articles =article.objects.all().filter(section = 'Technology').order_by('-pk')
            paginator = Paginator(articles, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/article.html', {'article' : page})
        elif selection == 'All':
            articles = article.objects.all().order_by('-pk')
            paginator = Paginator(articles, 20)
            page_number = request.GET.get('page')
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return render(request, 'Marketplace/article.html', {'article' : page})
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                      

@login_required           
def addarticle(request):
    if request.method == 'POST':
        form = articleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit = False)
            article.added_by = request.user
            article.save()
            
            # django notify
            post = article         
            author = User.objects.get(username = request.user)
            author_friend = author.friend_set.all()
            friends = []
            for follower in author_friend:
                friend = follower.current_user
                friends.append(friend)
            
            followers = list(friends)
            
            if len(followers) >= 1 :
                notify.send(request.user, recipient_list=followers, actor=post,
                        verb='posted', nf_type='all')
            else:
                pass          
            
            
            return redirect('articledetail', pk=article.pk)
    else:
        form = articleForm()
    return render(request, 'Marketplace/articleform.html', {'form' : form})

    
def mydirectory(request):
    markets = market.objects.all().order_by('-pk')
    return render(request, 'Marketplace/directory.html', {'market' : markets})    
    
    
def articledetail(request, pk):
    Article = get_object_or_404(article, pk=pk)
    comment = Comment.objects.all().filter(article = Article)
    return render (request, 'Marketplace/article_detail.html', {'articles' : Article,'comment' : comment})

    
 
def editarticle(request, article_id):
    global article
    Article = get_object_or_404(article, id=article_id)
    if request.method == 'POST':
        form = articleForm(request.POST, instance = Article)
        if form.is_valid():
            form.save()
            return redirect('articledetail', id=article.id)
        else:
            form = articleForm(instance = Article)
            return render(request, 'Marketplace/articleform.html', {'form' : form})
    else:
        form = articleForm(instance = Article)
        return render(request, 'Marketplace/articleform.html', {'form' : form})
       


@login_required
def article_approve(request, pk):
    post = get_object_or_404(article, pk=pk)
    post.approve()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required
def article_disapprove(request, pk):
    post = get_object_or_404(article, pk=pk)
    post.disapprove()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    


def marketdetail(request, pk):
    Market = get_object_or_404(market, pk=pk)  
    return render (request, 'Marketplace/market_detail.html', {'markets' : Market})

        
def market_remove(request, pk):
    markets = market.objects.all().order_by('-pk')
    Market = get_object_or_404(market, pk=pk)
    try:
        market.objects.get(added_by=request.user, pk=pk)
        Market.delete()
        return render(request, 'Marketplace/directory.html', {'market' : markets})
    except market.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




def likedarticle(request, pk):
    Article = get_object_or_404(article, pk=pk)
    try:
        Liked.objects.get(added_by = request.user, post = Article)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Liked.DoesNotExist:
         pref = Liked()
         pref.added_by = request.user
         pref.post = Article
         pref.save()
         Article.likes += 1
         Article.save()
         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_comment(request, pk):
    post = get_object_or_404(article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.added_by = request.user
            comment.article = post
            comment.article_author = post.added_by
            comment.save()
            
            # django notify
            author = User.objects.get(username = post.added_by)
            notify.send(request.user, recipient = author, actor=request.user, 
                            verb='commented', target = post, nf_type='all')
                              
            
            return redirect('articledetail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'Marketplace/addcomment.html', {'form' : form})
    

        
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    try:
        Comment.objects.get(article_author = request.user, pk=pk)
        comment.approve()
        return redirect('articledetail', pk=comment.article.pk)
    except Comment.DoesNotExist:
        return redirect('articledetail', pk=comment.article.pk)          
    
 

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    try:
        Comment.objects.get(article_author = request.user, pk=pk)
        comment.delete()
        return redirect('articledetail', pk=comment.article.pk)
    except Comment.DoesNotExist:
        return redirect('articledetail', pk=comment.article.pk)
    
    
def search(request):
    if request.method == 'GET':
        query = request.GET.get('search')
        market_list = market.objects.filter(Q(businessname__icontains=query))
        article_list = article.objects.filter(Q(topic__icontains=query))
        result_list = list(chain(market_list, article_list))
        return render(request, 'Marketplace/result.html', {'result' : result_list})


        
@login_required            
def add_internship(request):
    internships = Internship.objects.all().order_by('-pk')
    if request.method == 'POST':
        form = InternshipForm(request.POST, request.FILES)
        if form.is_valid():
            internship = form.save(commit = False)
            internship.added_by = request.user
            internship.save()
            
            # notify
            intern = internship         
            author = User.objects.get(username = request.user)
            author_friend = author.friend_set.all()
            friends = []
            for follower in author_friend:
                friend = follower.current_user
                friends.append(friend)
            
            followers = list(friends)
            
            if len(followers) >= 1 :
                notify.send(request.user, recipient_list=followers, actor=intern,
                            verb = 'posted', nf_type='all')
            else:
                pass                    
            
            
            return render(request, 'Marketplace/internship.html', 
                  {'internships' : internships})         
    else:
        form = InternshipForm()
        
    return render(request, 'Marketplace/add_internship.html', {'form' : form})
    


def internship_view(request):
    internships = Internship.objects.all().order_by('-pk')
    return render(request, 'Marketplace/internship.html', 
                  {'internships' : internships})           
                
def internship_remove(request, pk):
    internships = Internship.objects.all().order_by('-pk')
    internship = get_object_or_404(Internship, pk=pk)
    try:
        Internship.objects.get(added_by=request.user, pk=pk)
        internship.delete()
        return render(request, 'Marketplace/internship.html', {'internships' : internships})
    except Internship.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    
    
@login_required          
def register_profile(request):
    form = UserProfileForm()
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('index')
        else:
            print(form.errors)
    context_dict = {'form' : form}
    return render(request, 'Marketplace/profile_registration.html', context_dict)

@login_required   
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
    
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm({'website': userprofile.website, 
                            'picture': userprofile.picture})
    userarticles = article.objects.all().filter(added_by = username).order_by('-pk')
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)
    
    f, created = Friend.objects.get_or_create(current_user = user)
    friends = f.following.all()
    
    
    
    owner = User.objects.get(username = request.user)
    follow, created = Friend.objects.get_or_create(current_user = owner)
    follower = follow.following.all()
        
                      
    return render(request, 'Marketplace/profile.html',
                  {'userprofile': userprofile, 'selecteduser': user, 'form': form,
                   'userarticles': userarticles, 'friends': friends,
                   'follower': follower})
    
    
        
def change_friend(request, operation, pk):
    
    current_user = User.objects.get(username = request.user)
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.add_friend(current_user, new_friend)
        
        # django notify code
        notify.send(request.user, recipient=new_friend, actor=request.user,
                    verb='followed you.', nf_type='all')
        
    elif operation == 'remove':
        Friend.remove_friend(current_user, new_friend)
        
        # django notify code
        notify.send(request.user, recipient=new_friend, actor=request.user,
                    verb='stopped following you.', nf_type='all')
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




@login_required            
def add_workshop(request):
    workshops = Workshop.objects.all().order_by('-pk')
    if request.method == 'POST':
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            workshop = form.save(commit = False)
            workshop.added_by = request.user
            workshop.save()
            
            # notify
            training = workshop         
            author = User.objects.get(username = request.user)
            author_friend = author.friend_set.all()
            friends = []
            for follower in author_friend:
                friend = follower.current_user
                friends.append(friend)
            
            followers = list(friends)
            
            if len(followers) >= 1 :
                notify.send(request.user, recipient_list=followers, actor=training, verb = 'posted', 
                    nf_type='all')
            else:
                pass                    
            
            
            return render(request, 'Marketplace/workshop.html', 
                  {'workshops' : workshops})         
    else:
        form = WorkshopForm()
        
    return render(request, 'Marketplace/add_workshop.html', {'form' : form})


        

def workshop_view(request):
    workshops = Workshop.objects.all().order_by('-pk')
    return render(request, 'Marketplace/workshop.html', 
                  {'workshops' : workshops}) 


def workshop_remove(request, pk):
    workshops = Workshop.objects.all().order_by('-pk')
    workshop = get_object_or_404(Workshop, pk=pk)
    try:
        Workshop.objects.get(added_by=request.user, pk=pk)
        workshop.delete()
        return render(request, 'Marketplace/workshop.html', {'workshops' : workshops})
    except Workshop.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  




    
    
    


        
                
    
               
    
       
       
                
        
    
    
 
    
   
  
      
 
        
           
            
            
        
           
    


        
            







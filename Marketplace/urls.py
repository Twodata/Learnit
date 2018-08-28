from django.urls import path, re_path
from . import views




urlpatterns = [
        path('', views.index, name = 'index'),
        path('directory/', views.directory, name = 'directory'),
        path('contact/', views.contact, name = 'contact'),        
        path('policy/', views.policy, name = 'policy'),
        path('about/', views.about, name = 'about'),
        path('addmarket/', views.addmarket, name = 'success'),
        path('marketdetail/<int:pk>', views.marketdetail, name = 'marketdetail'),
        path('marketdetail/<int:pk>/remove', views.market_remove, name = 'market_remove'),
        path('articleview/', views.articleview, name = 'articleview'),
        path('addarticle/', views.addarticle, name = 'addarticle'),
        path('mydirectory/', views.mydirectory, name = 'mydirectory'),
        path('articledetail/<int:pk>', views.articledetail, name = 'articledetail'),
        path('editarticle/<int:article_id>/', views.editarticle, name = 'editarticle'),
        path('article/<int:pk>/approve/', views.article_approve, name = 'article_approve'),
        path('article/<int:pk>/disapprove/', views.article_disapprove, name = 'article_disapprove'),
        path('likedarticle/<int:pk>', views.likedarticle, name = 'likedarticle'),
        path('add_comment/<int:pk>/comment/', views.add_comment, name = 'add_comment'),
        path('comment/<int:pk>/approve/', views.comment_approve, name = 'comment_approve'),
        path('comment/<int:pk>/remove/', views.comment_remove, name = 'comment_remove'),
        path('search/', views.search, name = 'search'),
        path('add_internship/', views.add_internship, name = 'add_internship'),
        path('internship_view/', views.internship_view, name = 'internship_view'),
        path('internship_view/<int:pk>/remove', views.internship_remove, name = 'internship_remove'),
        path('register_profile/', views.register_profile, name = 'register_profile'),
        re_path(r'profile/(?P<username>[\w\-]+)/', views.profile, name='profile'),
        re_path(r'connect/(?P<operation>.+)/(?P<pk>\d+)/', views.change_friend, name = 'change_friend'),
        path('add_workshop/', views.add_workshop, name = 'add_workshop'),
        path('workshop_view/', views.workshop_view, name = 'workshop_view'),
        path('workshop_view/<int:pk>/remove', views.workshop_remove, name = 'workshop_remove'),
                ]


                    
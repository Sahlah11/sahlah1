from django.urls import path


from . import views  


urlpatterns = [
    path('', views.index),  
    path('index2/<int:val1>/', views.index2)  ,
   

    path('<int:bookId>', views.viewbook),


   path('', views.index, name= "books.index"),

   path('list_books/', views.list_books, name= "books.list_books"),

   path('<int:bookId>/', views.viewbook, name="books.view_one_book"),

   path('aboutus/', views.aboutus, name="books.aboutus"),
   
    path('lab5/', views.lab5Page, name='book.lab5Page'),
   
    path('text/formatting/', views.formatting_page, name="text_formatting"),
   
    path('listing/', views.listing_page, name="listing_page"),
    path('tables/', views.tables_page, name="tables_page"),
    path('search/', views.search_books, name='search_books'),
    path('query1/',views.simple_query,name='books.simple_query'),
    path('query2/',views.complex_query,name='books.complex_query'),
    path('books/', views.list_books, name='list_books'),
]






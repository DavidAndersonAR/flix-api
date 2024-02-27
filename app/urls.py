from django.contrib import admin
from django.urls import include, path
from genres.views import GenreCreateListView, GenreReatriveUpdate
from actors.views import ActorCreatelistView, ActorRetrieve
from movies.views import MovieCreateListView, MovieRetrieve
from reviews.views import ReviewCreateListView, ReviewRetrieveView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls')),

    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreReatriveUpdate.as_view(), name='genre-detail-list'),

    path('actors/', ActorCreatelistView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActorRetrieve.as_view(), name='actors-detail-list'),

    path('movie/', MovieCreateListView.as_view(), name='movie-create-list'),
    path('movie/<int:pk>/', MovieRetrieve.as_view(), name='movie-detail-list'),

    path('review/', ReviewCreateListView.as_view(), name='review-create-list'),
    path('review/<int:pk>/', ReviewRetrieveView.as_view(), name='review-detail-list'),
]

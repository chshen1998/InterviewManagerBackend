from django.urls import path
from .views import ApplicationView, AddApplicationView, GetApplicationsView, DeleteApplicationView, UpdateApplicationView


urlpatterns = [
    path('application', ApplicationView.as_view()),
    path('add-application', AddApplicationView.as_view()),
    path('get-applications', GetApplicationsView.as_view()),
    path('delete-application', DeleteApplicationView.as_view()),
    path('update-application', UpdateApplicationView.as_view()),
]
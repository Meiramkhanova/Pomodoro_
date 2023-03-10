from django.contrib import admin
from django.urls import include, path

handler400 = 'pomodorotech.views.error_400'
handler403 = 'pomodorotech.views.error_403'
handler404 = 'pomodorotech.views.error_404'
handler500 = 'pomodorotech.views.error_500'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('pomodorotech.urls')),
]

handler404= 'pomodorotech.views.pageNotFound'

handler403 = 'pomodorotech.views.error_403'

handler400='pomodorotech.views.error_400'

handler500='pomodorotech.views.error_500'

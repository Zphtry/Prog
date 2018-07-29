from django.conf.urls import url
import view

urlpatterns = [
    url(r'^ino/', view.arduino)
]

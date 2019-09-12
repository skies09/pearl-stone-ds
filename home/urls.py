from django.conf.urls import url, include
from .views import home
from .views import deliveries
from .views import track
from .views import contact
from .views import faq
from .views import sizes
from .views import metal

urlpatterns = [
url(r'^home/', home, name="home"),
url(r'^deliveries/', deliveries, name="deliveries"),
url(r'^track/', track, name="track"),
url(r'^contact/', contact, name="contact"),
url(r'^faq/', faq, name="faq"),
url(r'^sizes/', sizes, name="sizes"),
url(r'^metal/', metal, name="metal"),

]
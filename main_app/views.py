from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView



# Create your views here.

class Home(TemplateView):
   template_name = 'home.html'


class Duck:
    def __init__(self, name, img, bio):
        self.name = name
        self.img = img
        self.bio = bio

ducks = [
    Duck('Cool Duck', 'https://www.thoughtfulcode.com/wp-content/uploads/2019/01/rubber-duck-debugging-and-psychology-sunglassed-rubber-duck-1272x848.jpg', 'This Duck is Too Cool For School'),
    Duck('Dragon Duck', 'https://m.media-amazon.com/images/I/61Fa1fs6W+L._AC_SL1200_.jpg', 'When a Dragon and a Duck Love Eachother Very Much'),
    Duck('Science Duck', 'https://cdn.shopify.com/s/files/1/0604/4801/products/SG-REYTD-JCNYO_1024x1024_clipped_rev_1-min.jpeg?v=1505504539', 'The Power of SCIENCE!!!!!'),
    Duck('DuckPool', 'https://www.elinkdesign.com/assets/files/Page_Editor_Files/20180418_105737.jpg', 'Bad DuckPool.......Good DuckPool!!'),
    Duck('OctoDuck', 'https://m.media-amazon.com/images/I/61su4ZAG94L._AC_SL1200_.jpg', "I don't even know how to explain this one. How could this happen?"),
    Duck('OG Duck', 'https://www.munchkin.com/media/catalog/product/cache/fa94a348188ff11085d90b41566e795b/3/1/31001_white_hot_safety_bath_ducky.jpg', "Rubber Ducky, You're the one"),
    Duck('GA Graduate Duck', 'https://partycity4.scene7.com/is/image/PartyCity/_sq_?$_500x500_$&$product=PartyCity/165979_full', 'This Duck is going to be a very successful Software Engineer')
]

class DuckList(TemplateView):
    template_name = 'duck_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ducks'] = ducks
        return context
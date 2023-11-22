from django.views import View
from django.shortcuts import render

class HomepageView(View):
    def get(self, request):
        return render(request, 'homepage.html')


from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''"<h1>hello</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django Purnendu</a>''')

# def about(request):
#     return HttpResponse("hello purnendu")

def index(request):
#    params = {'name':'harry', 'place':'Mars'}
   return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    #get the text
    djtext= request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        # analysed = djtext
        punctuations= '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose':'Removed Punctuation', 'analysed_text':analysed}

        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("cap first")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def sapceremove(request):
#     return HttpResponse("space remove")

# def charcount(request):
#     return HttpResponse("charcount")
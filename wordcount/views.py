from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()
    worddict = {}
    for word in wordcount:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'count':len(wordcount), 'fulltext':fulltext, 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')

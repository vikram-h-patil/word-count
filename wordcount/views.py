from django.http import HttpResponse
from django.shortcuts import render
import operator 


def home(request):
    #pass the request object and the file inside the templates folder; we can also pass dictionary here
    return render(request,'home.html',{'Uni':'Monash'} )

def oz(request):
    return HttpResponse('Welcome to OZ, you landed on 2018!')
    
def test2(request):
    return render(request,'test2.html',{'Uni':'Monash'})

def count(request):
    vikramtext = request.GET['vikramtext']
    
    indiv_words= vikramtext.split()
    
    #creating a dictionary for the task
    word_dict = {}
    for word in indiv_words:
        #if the word already in dict, then increase the count
        if word in word_dict:
            word_dict[word] +=1
        #else, add the new word into the dictionary
        else:
            word_dict[word]=1
            
     #Sorting begins
    sorted_words= sorted(word_dict.items(), key=operator.itemgetter(1), reverse= True)
         
            
    return render(request,'count.html',{'vikramtext':vikramtext , 'count_of_words' :len(indiv_words), 'sorted_words':sorted_words })   


def about(request):
    return render(request,'about.html')



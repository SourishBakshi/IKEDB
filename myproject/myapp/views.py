from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
import search
import search1
import filesync
import spellcheck
import time
#forms
from forms import NameForm
from forms import UpdateForm
import update
import language
import prediction_content
import json

def get_name(request):
    form=NameForm()
    form1=UpdateForm()
    s8 = prediction_content.get_prediction_content()
    json_pre = json.dumps(s8)

    # if this is a POST request we need to process the form data
    if request.method == 'POST' and 'search' in request.POST:
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #start of search processing time
            start_time=time.time()
            your_name = request.POST.get('your_name')
            your_name1=your_name
            s=search1.get_search_result(your_name1)
            s1=search1.get_file_name()
            s3=[]
            s4=search1.pre()
            s5=search1.get_knownerror()
            for i in s1:
                if i not in s3:
                    s3.append(i)
            s2=zip(s,s1,s4,s5)
            c=len(s)
            tim=time.time()-start_time
            tim=str(tim)+" sec"
            #end of search process time
            form=NameForm()

            return render(request,'myapp/thanks.html',{'name':your_name1,'file':s3,'filename':s2,'number':c,'result':s,'form':form,'form1':form1,'soln':s,'ti':tim,'json_pre':json_pre})

    if request.method == 'POST' and 'update' in request.POST:
        form1 = UpdateForm(request.POST)
        if form1.is_valid():
            question = request.POST.get('question')
            answer = request.POST.get('comment')
            pre = request.POST.get('pre')
            file_choice=request.POST.get('file_choice')
            print answer

            print question
            print file_choice
            form1 = UpdateForm()
            update.update(question,answer,pre,file_choice)

            return render(request, 'myapp/thanks.html',
                          {'form':form,'form1':form1,'json_pre':json_pre})
    else:
            form = NameForm()
            form1=UpdateForm()


    #template = loader.get_template("myapp/name.html")
    context = {'form': form,'form1':form1,'json_pre':json_pre}
    #return HttpResponse(template.render(context, request))
    return render(request, "myapp/name.html", context)





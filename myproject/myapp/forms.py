from django import forms
import filesync
#import search1
s=filesync.syncfile()
s3=[]
for i in s:
    s1=i.split("\\")
    s2=s1[-1]
    leng=len(s2)
    i1=s2[0:leng-5:]
    s3.append(i1)
#print s
#s3=[]
#for i in s1:
#    if i not in s3:
#        s3.append(i)
FILE_CHOICES=[tuple([x,x]) for x in s3]
#FILE_CHOICES= [
#    ('orange', 'Oranges'),
#    ('cantaloupe', 'Cantaloupes'),
#    ('mango', 'Mangoes'),
#    ('honeydew', 'Honeydews'),
#    ]

class NameForm(forms.Form):
    your_name = forms.CharField(label="IKEDB SEARCH ",
                                widget=forms.TextInput(attrs={'placeholder':'Search..',
                                                              'id':'predictivesearch'
                                                            }) ,max_length=100)
class UpdateForm(forms.Form):
    file_choice = forms.CharField(label='Please select the KEDB file.', widget=forms.Select(choices=FILE_CHOICES))
    question=forms.CharField(label="Known Error ",widget=forms.Textarea(attrs={'rows':5}))
    comment=forms.CharField(label="Solution ",widget=forms.Textarea(attrs={'rows':5}))
    #answer=forms.CharField(label="Solution ",widget=forms.TextInput(attrs={'placeholder':'Solution'}),max_length=500)
    pre=forms.CharField(label="Prerequisite ",widget=forms.Textarea(attrs={'rows':5}))

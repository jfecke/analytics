from django.shortcuts import render
from regression.models import Topic, WebPage, AccessRecord, User
from regression.forms import NewUser
import pandas as pd


# Create your views here.
def index(request):
    user_list = User.objects.order_by('lastName')
    user_dict = {"user_records": user_list}
    return render(request, 'regression/index.html', context=user_dict)

def other(request):

    if "GET" == request.method:
        return render(request, 'regression/other.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        df = pd.read_excel(excel_file)

        df_dict = df.to_dict('series')


    return render(request, 'regression/other.html', {'dataframe': df_dict})

def relative_URL(request):
    return render(request, 'regression/relative_url.html')

def users(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error is invalid")

    return render(request, 'regression/users.html', {'form':form})


# def form_view(request):
#     form = forms.FormName()
#
#     if request.method == 'POST':
#         form = forms.FormName(request.POST)
#
#         if form.is_valid():
#             print("Success!")
#             print("Name: " + form.cleaned_data['name'])
#             print("Email: " + form.cleaned_data['email'])
#             print("Text: " + form.cleaned_data['textArea'])
#
#     return render(request, 'regression/form.html', {"form": form})
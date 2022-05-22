from urllib import response
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm,LoginForm,PosteForm, DemanderForm, CommentForm
from django.contrib.auth.decorators import permission_required
from .models import Demandeur, Postes, User, Comment
from django.contrib.auth.models import Group
from django.http import FileResponse
import os





""""
def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

"""


def index(request):
    postes = Postes.objects.all()
    return render(request, 'tik/index.html', {'postes':postes})



def register(request):
    form = RegisterForm()
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='hommes')
            group = Group.objects.get(name='femmes')
            user.groups.add(group)
            messages.success(request, " Compte creer ")
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'tik/register.html', {'form':form})




def login_us(request):
    forms = LoginForm()
    if request.method =='POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            user = authenticate(request, username= forms.cleaned_data['username'], password= forms.cleaned_data['password'])
            if user is not None and user.is_homme:
                login(request, user)
                return redirect("homme")
                
            elif user is not None and user.is_femme:
                login(request, user)
                return redirect('femme')
    return render(request, 'tik/login.html', {'forms':forms})






def upload(request):
    upload = PosteForm()
    if request.method =='POST':
        upload = PosteForm(request.POST)
        if upload.is_valid():
            upload.save()
            return redirect("index")

    return render(request, 'tik/upload_poste.html', {'upload':upload})


def detail_post(request, id):
    post = get_object_or_404(Postes, id=id)
    comments = Comment.objects.all()
    new_comment = None
    if request.method =='POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
           # NOUVEAU COMMENTAIRE EGALE A L OBJECT POST DE DATAIL
            new_comment.post = post
            new_comment.save()
    return render(request, 'tik/post_detail.html', {'post':post, 'comments':comments, 'new_comment':new_comment})



def editform(request, my_id):
    form = Postes.objects.get(id=my_id)
    upload = PosteForm(instance=form)
    if request.method=='POST':
        upload = PosteForm(request.POST, instance=form)
        if upload.is_valid():
            upload.save()
            return redirect('index')
    return render(request, 'tik/edit.html', {'upload':upload})




def demander(request):
    de = DemanderForm()
    if request.method =='POST':
        de = DemanderForm(request.POST)
        if de.is_valid():
            de.save()
            return redirect('staff')

    return render(request, 'tik/demander.html', {'de':de})




def staf(request):
    de = Demandeur.objects.all()
    return render(request, 'tik/staff.html',{'de':de})



def donne(request):
    return render(request, 'tik/donnees.html')




def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response=HttpResponse(fh.read(),content_type='tik/upload')
            response["content Disposition"]="inline;filename"+os.path.basename(file_path)
            return response
    raise Http404



def detail(request, id):
    de = get_object_or_404(Demandeur, id=id)
    return render(request, 'tik/donnees.html', {'de':de})




def updatedemande(request, id):
    dem = Demandeur.objects.get(id=id)
    de = DemanderForm(instance=dem)
    if request.method=='POST':
        de = DemanderForm(request.POST, instance=dem)
        if de.is_valid():
            de.sava()
            return redirect('donnee')
    return render(request, 'tik/updated.html', {'de':de})














def homme(request):
    return render(request, 'tik/homme.html')





def femme(request):
    return render(request, 'tik/femme.html')




def logout_user(request):
    logout(request)




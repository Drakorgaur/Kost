from django.shortcuts import render
from django.views import generic
from django.views.generic import RedirectView
from django.shortcuts import redirect

from .models import Note, CurrentNote, RegisterToken

class RegtokenListView(generic.ListView):
    model = RegisterToken

class NoteDetailView(generic.DetailView):
    model = Note

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            return self.get(request, *args, **kwargs)
        elif request.method == 'POST':
            update_object = Note.objects.get(pk=kwargs['pk'])
            form = NoteForm(request.POST, instance=update_object)
            form.save()
            context = NoteDetailView.get_context_data(self)
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        context['hello'] = Note.objects.all().count()
        context['place'] = Note.pk
        context['hell'] = self.kwargs['pk']
        context['form'] = NoteForm()
        return context

def index(request):
    num_note=Note.objects.all().count()

    return render(request, 'index.html', context={'num_note':num_note},)

import datetime
from .forms import NoteForm
from django.contrib.auth.models import User
def post_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = datetime.date.today()
            post.save()
            return redirect('note-detail', pk=post.pk)

    else:
        form = NoteForm()
    return render(request, 'main/adding_note.html', {'form': form})


from .forms import LoginForm, UserRegistrationForm, ProfileForm
from .forms import TokenInputForm
from .models import RegisterToken
def tokenInput(request):
    if request.method == 'POST':
        form = TokenInputForm(request.POST)
        if form.is_valid():
            post = form
            current_token=request.POST['token']
            try:
               RegisterToken.objects.get(token=current_token)
               return redirect('reg-tokens')
            except RegisterToken.DoesNotExist:
                return render(request, 'main/token_input.html', {'form': form})
            except RegisterToken.MultipleObjectsReturned:
                return render(request, 'main/token_input.html', {'form': form})
    else:
        form = TokenInputForm()
    return render(request, 'main/token_input.html', {'form': form})

from .forms import RegisterTokenForm
from .models import RegisterToken
import random
class TokenCreation():
        
    def getNumber():
        return str(random.randrange(10))
    def getLetter():
        return random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'])

    def getRegisterToken():
        token = ''
        for i in range(3):
            token = token + TokenCreation.getNumber()
            token = token + TokenCreation.getLetter()
        return token

    def reg_token_create(request):
        if request.method == "POST":
            form = RegisterTokenForm(request.POST)
            if form.is_valid():
                registerToken = RegisterToken()
                registerToken.token = TokenCreation.getRegisterToken()
                registerToken.save()
            
                return redirect('reg-tokens')

        else:
            form = RegisterTokenForm()
        return render(request, 'main/token.html', {'form': form})

    
from django.contrib.auth import authenticate, login
class MultipleFormAuth():
    def mulitpleForms(request):
        #registration
        if request.method=='POST' and 'btnform2' in request.POST:
            if request.method == 'POST':
                user_form = UserRegistrationForm(request.POST)
                if user_form.is_valid():
                    new_user = user_form.save(commit=False)
                    new_user.set_password(user_form.cleaned_data['password'])
                    new_user.save()
                    return render(request, 'main/register_done.html', {'new_user': new_user})
            else:
                user_form = UserRegistrationForm()
            return render(request, 'main/login2.html', {'user_form': user_form})
        #login
        elif request.method=='POST' and 'btnform1' in request.POST:
            if request.method == 'POST':
                login_form = LoginForm(request.POST)
                if login_form.is_valid():
                    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                    if user is not None:
                        login(request, user)
                        # Redirect to a success page?
                        # return HttpResponseRedirect('/')
                        return render(request, 'index.html')
                    else:
                        return render(request, 'main/login2.html', {'login_form': login_form, 'error': True})
                else:
                    login_form = LoginForm()
                return render(request, 'main/login2.html', {'login_form': login_form, 'error': False})
        else:
            user_form = UserRegistrationForm()
            login_form = LoginForm()
        return render(request, 'main/login2.html', {'user_form': user_form, 'login_form': login_form})

from django.core.paginator import Paginator
from .forms import FilterForm
from .models import Note
class NotesFilter():
    def NoteFilter(request):
        non_filtered_list = Note.objects.all()  
        if request.method == 'GET':
            form = FilterForm(request.GET)
            if form.is_valid():
                filtered_list=Note.objects.filter(name__icontains = request.GET['filter'])
                paginator = Paginator(filtered_list, 1)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)

                return render(request, 'main/notes.html', {'form': form, 'note_list': filtered_list, 'page_obj': page_obj})
        else:
            form = FilterForm()
        paginator = Paginator(non_filtered_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'main/notes.html', {'form': form, 'note_list': non_filtered_list, 'page_obj': page_obj})

class Profile():
    def profile(request):
        return render(request, 'main/profile.html', {'last_name': request.user.last_name, 'first_name': request.user.first_name})
    def profileUpdate(request):
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                request.user.username = request.POST['username']
                request.user.first_name = request.POST['first_name']
                request.user.last_name = request.POST['last_name']
                request.user.save()
                return render(request, 'main/profile.html')
        else:
            form = ProfileForm()
        return render(request, 'main/profile_update.html', {'form': form})

class Chat():
    def index(request):
        return render(request, 'main/chat.html')

from django.shortcuts import render
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


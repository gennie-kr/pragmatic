from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    #success_url = reverse_lazy('accountapp:hello_world')
    success_url = reverse_lazy('home')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
#원래 수업코드 입력시 changeinfo 기능이 적용안되어 수정
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    #success_url = reverse_lazy('accountapp:hello_world')
    success_url = reverse_lazy('home')
    template_name = 'accountapp/update.html'

    # 추가
    context_object_name = 'target_user'

"""

from django.contrib.auth.views import PasswordChangeView

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(PasswordChangeView):
#class AccountUpdateView(UpdateView):
    model = User
# 추가
    form_class = AccountUpdateForm

    context_object_name = 'target_user'
#    success_url = reverse_lazy('accountapp:hello_world')
    success_url = reverse_lazy('home')
    template_name = 'accountapp/update.html'
# 위의 코드로 수정하여 해결
"""
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
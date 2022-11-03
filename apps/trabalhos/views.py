from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, View
from .models import Trabalho
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from .form import TrabalhoForm

class TrabalhoCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = TrabalhoForm
    success_message = 'Trabalho cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_trabalhos")                                     #precisar criar um url com isso!!!!!!!!!!!

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'TCCs'
        context['descricao'] = 'Cadastro de tccs'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class TrabalhoUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
     login_url = reverse_lazy('login')
     model = Trabalho
     form_class = TrabalhoForm
     success_message = 'Tcc atualizado com sucesso!'
     template_name = "cadastros/form.html"
     success_url = reverse_lazy("listar_trabalhos")                                    #precisar criar um url com isso!!!!!!!!!!!

     def get_context_data(self, **kwargs):
         context = super(UpdateView, self).get_context_data(**kwargs)
         context['titulo'] = 'TCCs'
         context['descricao'] = 'Editar tcc'
         context['botao'] = 'Salvar'
         return context

     def form_valid(self, form):
         url = super().form_valid(form)
         return url

class TrabalhoDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
     login_url = reverse_lazy('login')
     model = Trabalho
     success_message = 'Tcc excluído com sucesso!'
     template_name = "cadastros/form-excluir.html"
     success_url = reverse_lazy("listar_trabalhos")                                  #precisar criar um url com isso!!!!!!!!!!!

     def get_context_data(self, **kwargs):
         context = super(DeleteView, self).get_context_data(**kwargs)
         context['titulo'] = 'TCCs'
         return context

     def delete(self, request, *args, **kwargs):
         messages.success(self.request, self.success_message)
         return super(TrabalhoDelete, self).delete(request, *args, **kwargs)

class TrabalhoList(ListView):
    model = Trabalho
    template_name = "cadastros/listas/trabalhos.html"
    

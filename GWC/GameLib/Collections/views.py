from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Person, Boardgame, Collection, Checkout
from .forms import PersonCreateForm, BoardgameCreateForm, CollectionCreateForm, CheckoutCreateForm

class PersonListView(LoginRequiredMixin, ListView):
	template_name = 'collections/person_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Person.objects.filter(
					Q(LastName__iexact=slug) |
					Q(LastName__icontains=slug) |
					Q(FirstName__iexact=slug) |
					Q(FirstName__icontains=slug)
				)
		else:
			queryset = Person.objects.all()
		return queryset

class PersonDetailView(LoginRequiredMixin, UpdateView):
	form_class = PersonCreateForm
	queryset = Person.objects.all()
	template_name = 'collections/person_form.html'
	success_url = '/person'

	def get_context_data(self, *args, **kwargs):
		context = super(PersonDetailView, self).get_context_data(*args, **kwargs)
		return context

class PersonCreateView(LoginRequiredMixin, CreateView):
	form_class = PersonCreateForm
	template_name = 'collections/person_form.html'
	success_url = '/person'

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.AuthUser = self.request.user
		#instance.save()
		return super(PersonCreateView, self).form_valid(form)

class BoardgameListView(LoginRequiredMixin, ListView):
	template_name = 'collections/boardgame_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Boardgame.objects.filter(
					Q(Name__iexact=slug) |
					Q(Name__icontains=slug)
				)
		else:
			queryset = Boardgame.objects.all()
		return queryset

class BoardgameDetailView(LoginRequiredMixin, UpdateView):
	form_class = BoardgameCreateForm
	queryset = Boardgame.objects.all()
	template_name = 'collections/boardgame_form.html'
	success_url = '/boardgame'

	def get_context_data(self, *args, **kwargs):
		context = super(BoardgameDetailView, self).get_context_data(*args, **kwargs)
		return context

class BoardgameCreateView(LoginRequiredMixin, CreateView):
	form_class = BoardgameCreateForm
	template_name = 'collections/boardgame_form.html'
	success_url = '/boardgame'


class CollectionListView(LoginRequiredMixin, ListView):
	template_name = 'collections/collection_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Collection.objects.filter(
					Q(Person__LastName__iexact=slug) |
					Q(Person__LastName__icontains=slug) |
					Q(Boardgame__Name__iexact=slug) |
					Q(Boardgame__Name__icontains=slug)
				)
		else:
			queryset = Collection.objects.all()
		return queryset

class CollectionDetailView(LoginRequiredMixin, UpdateView):
	form_class = CollectionCreateForm
	queryset = Collection.objects.all()
	template_name = 'collections/collection_form.html'
	success_url = '/collection'

	def get_context_data(self, *args, **kwargs):
		context = super(CollectionDetailView, self).get_context_data(*args, **kwargs)
		return context

class CollectionCreateView(LoginRequiredMixin, CreateView):
	form_class = CollectionCreateForm
	template_name = 'collections/collection_form.html'
	success_url = '/collection'


class CheckoutListView(LoginRequiredMixin, ListView):
	template_name = 'collections/checkout_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = Checkout.objects.filter(
					Q(Attendee__LastName__iexact=slug) |
					Q(Attendee__LastName__icontains=slug) |
					Q(BoardgameFromCollection__Name__iexact=slug) |
					Q(BoardgameFromCollection__Name__icontains=slug) |
					Q(BoardgameFromCollection__id__iexact=slug)
				)
		else:
			queryset = Checkout.objects.all()
		return queryset

class CheckoutDetailView(LoginRequiredMixin, DetailView):
	queryset = Checkout.objects.all()
	template_name = 'collections/checkout_detail.html'
	def get_context_data(self, *args, **kwargs):
		context = super(CheckoutDetailView, self).get_context_data(*args, **kwargs)
		return context

class CheckoutCreateView(LoginRequiredMixin, CreateView):
	form_class = CheckoutCreateForm
	template_name = 'collections/checkout_form.html'
	success_url = '/checkout'
from django.shortcuts import render, HttpResponse
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms import layout
from . import models

class IndexView(generic.ListView):
    context_object_name = 'presentations'
    template_name = 'index.html'

    def get_queryset(self):
        return models.Presentation.objects.all()

class DetailView(generic.DetailView):
    context_object_name = 'presentation'
    model = models.Presentation
    template_name = 'detail.html'

class PresentationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.message = kwargs.pop('message', None)
        self.header = kwargs.pop('header', None)
        super(PresentationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = models.Presentation
        fields = ['title', 'abstract', 'track']
    
    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = layout.Layout(
            layout.HTML(f'<h2>{self.header}</h2>'),
            layout.HTML(f'<div>{self.message}</div>'),
        )
        for field in self.Meta().fields:
            helper.layout.append(layout.Field(field, wrapper_class='row'))
        helper.layout.append(layout.Submit('submit', 'Submit your session', css_class='btn-success col-12'))
        helper.label_class = 'col-3'
        helper.field_class = 'col-9'
        return helper

class CreateView(SuccessMessageMixin, generic.CreateView):
    template_name = 'edit.html'
    success_message = 'Thank you for submitting! We will be in touch'
    form_class = PresentationForm

    def form_valid(self, form):
        # Simulate assigning current user to speaker
        form.instance.speaker = models.Speaker.objects.get(pk=1)
        return super().form_valid(form)
    def get_form_kwargs(self):
        kwargs = super(CreateView, self).get_form_kwargs()
        kwargs.update({
            'header': 'Submit a session!',
            'message': 'Got something you want to talk about? Submit it!'
        })
        return kwargs

class EditView(SuccessMessageMixin, generic.UpdateView):
    template_name = 'edit.html'
    success_message = 'Your update has been saved!'
    form_class = PresentationForm
    model = models.Presentation

    def get_form_kwargs(self):
        kwargs = super(EditView, self).get_form_kwargs()
        kwargs.update({
            'header': 'Update your session',
            'message': 'Want to make some changes? Update the form below!'
        })
        return kwargs

    # GET:
    #   Present the user with a form
    # POST: (receive information from user)
    #   Prevent csrf
    #   Validate the form
    #   Save objects to the database
    #   Redirect the user to a success page (typically details)

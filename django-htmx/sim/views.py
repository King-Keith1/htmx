from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from sim.forms import SampleForm
from sim.models import Message

def sample_post(request, *args, **kwargs):
    form = SampleForm(request.POST or None)
    if form.is_valid():
        message = Message(
            email=form.cleaned_data['email'],
            name=form.cleaned_data['name'],
            favourite_color=form.cleaned_data['favourite_color']
        )
        message.save()
        messages = Message.objects.all()  # Fetch updated list of messages
        return render(request, 'message_list.html', {'messages': messages})
    else:
        error_message = '<p class="error">Your form submission was unsuccessful ❌. Please correct the errors:</p>'
        error_message += '<ul>'
        for field, errors in form.errors.items():
            for error in errors:
                error_message += f'<li>{field}: {error}</li>'
        error_message += '</ul>'
        return HttpResponse(error_message)

def example(request):
    messages = Message.objects.all()  # Fetch all messages
    return render(request, 'example.html', {'messages': messages})

def edit_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    form = SampleForm(initial={
        'email': message.email,
        'name': message.name,
        'favourite_color': message.favourite_color
    })
    return render(request, 'edit_form.html', {'form': form, 'message': message})

def update_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    form = SampleForm(request.POST or None)
    if form.is_valid():
        message.email = form.cleaned_data['email']
        message.name = form.cleaned_data['name']
        message.favourite_color = form.cleaned_data['favourite_color']
        message.save()
        return render(request, 'message_card.html', {'message': message})
    else:
        error_message = '<p class="error">Update failed ❌. Please correct the errors:</p>'
        error_message += '<ul>'
        for field, errors in form.errors.items():
            for error in errors:
                error_message += f'<li>{field}: {error}</li>'
        error_message += '</ul>'
        return HttpResponse(error_message)

@require_http_methods(["DELETE"])
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return HttpResponse("")  # Return an empty response to remove the element
from django.shortcuts import render,redirect
from .models import chat_app

def chat_view(request):
  if request.method == "POST":
    text = request.POST.get("message")
    is_admin = request.user.is_staff  # Assuming admin users are marked as staff
    chat_app.objects.create(name = request.user,text=text, is_admin=is_admin)
    return redirect('chat:chat')  # Prevent form resubmission

  messages = chat_app.objects.order_by('timestamp')
  return render(request, 'chat/chat.html', {'messages': messages})

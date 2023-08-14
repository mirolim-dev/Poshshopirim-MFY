from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Appeal
# Create your views here.

def contact(request):
    contact_messages = ''
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        address = request.POST['address']
        message_content = request.POST['message']
        if first_name and last_name and phone and address and message_content:
            Appeal.objects.create(
                first_name=first_name, last_name=last_name, 
                phone=phone, address=address, content=message_content)
            contact_messages = messages.success(request, "Habaringiz muvaffaqiyatli jo'natildi. \
                Hodimlar sizga 3 ish kuni davomida javob beradilar")
            return redirect('contact')
        else:
            contact_messages = messages.error(request, "Habarni jo'natishdan avval barcha ma'lumotlarni kiriting")
    context = {
        'contact_messages': contact_messages,
    }
    return render(request, 'contact.html', context)
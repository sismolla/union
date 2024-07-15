from django.shortcuts import render,redirect,HttpResponse
from .models import (Research,Thesis,GraphicsDesignSubmission,ProgrammingProjectSubmission,VideoEditingSubmission,Transcription,Assignment,Business_plan)
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='user:login')
def create_research(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        number_of_pages = request.POST.get('number_of_pages')
        deadline = request.POST.get('deadline')
        abstract = request.FILES.get('abstract')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'


        Research.objects.create(firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,deadline=deadline,abstract=abstract,description=description,accept_terms=accept_terms)
   
        return redirect('order:order')  # Replace with your success URL

    return render(request, 'order/research.html')

@login_required(login_url='user:login')
def create_thesis(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        number_of_pages = request.POST.get('number_of_pages')
        deadline = request.POST.get('deadline')
        abstract = request.FILES.get('abstract')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'


        Thesis.objects.create(firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,deadline=deadline,abstract=abstract,description=description,accept_terms=accept_terms)
   
        return redirect('order:thesis')  # Replace with your success URL

    return render(request, 'order/thesis.html')


@login_required(login_url='user:login')
def graphics_design_submission(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        service = request.POST.get('service')
        deadline = request.POST.get('deadline')
        design_file = request.FILES.get('design_file')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')

        # You can add validation and error handling here

        # Save the submission to the database
        submission = GraphicsDesignSubmission(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone_number=phone_number,
            gender=gender,
            service=service,
            deadline=deadline,
            design_file=design_file,
            description=description,
            accept_terms=accept_terms == 'on'
        )
        submission.save()

        # Redirect to a success page or render a success message

        return redirect('order:graphics-design')  # Replace with your success URL

    return render(request, 'order/graphics_design.html')

@login_required(login_url=('user:login'))
def programming_project_submission(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        title = request.POST.get('title')
        programming_language = request.POST.get('programming_language')
        specific_work_area = request.POST.get('specific_work_area')
        deadline = request.POST.get('deadline')
        project_file = request.FILES.get('project_file')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')

        # Save the submission to the database
        submission = ProgrammingProjectSubmission(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone_number=phone_number,
            gender=gender,
            title=title,
            programming_language=programming_language,
            specific_work_area=specific_work_area,
            deadline=deadline,
            project_file=project_file,
            description=description,
            accept_terms=accept_terms == 'on'
        )
        submission.save()

        return redirect('order:program-project')  # Replace with your success URL

    return render(request, 'order/programming.html')



def video_editing_submission(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        title = request.POST.get('title')
        video_length = request.POST.get('video_length')
        video_format = request.POST.get('video_format')
        deadline = request.POST.get('deadline')
        project_file = request.FILES.get('project_file')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')

        # Save the submission to the database
        submission = VideoEditingSubmission(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone_number=phone_number,
            gender=gender,
            title=title,
            video_length=video_length,
            video_format=video_format,
            deadline=deadline,
            project_file=project_file,
            description=description,
            accept_terms=accept_terms == 'on'
        )
        submission.save()

        return redirect('order:video-project')  # Replace with your success URL

    return render(request, 'order/video_editing.html')

def transcription(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        accept_terms = request.POST.get('accept_terms')
        title = request.POST.get('title')
        source_language = request.POST.get('source_language')
        target_language = request.POST.get('target_language')
        deadline = request.POST.get('deadline')

        # Save the submission to the database
        submission = Transcription(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone_number=phone_number,
            gender=gender,
            accept_terms=accept_terms == 'on',
            title=title,
            source_language=source_language,
            target_language=target_language,
            deadline=deadline
        )
        submission.save()
        return redirect('order:transcription')  # Replace with your success URL

    return render(request, 'order/transcription.html')

# ////////////////////////////////////////////////////

@login_required(login_url='user:login')
def assignment(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        number_of_pages = request.POST.get('number_of_pages')
        deadline = request.POST.get('deadline')
        abstract = request.FILES.get('abstract')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'


        Assignment.objects.create(firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,deadline=deadline,abstract=abstract,description=description,accept_terms=accept_terms)
   
        return redirect('order:assignment')  # Replace with your success URL

    return render(request, 'order/assignment.html')

@login_required(login_url='user:login')
def business_plan(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        number_of_pages = request.POST.get('number_of_pages')
        deadline = request.POST.get('deadline')
        abstract = request.FILES.get('abstract')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'


        Business_plan.objects.create(firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,deadline=deadline,abstract=abstract,description=description,accept_terms=accept_terms)
   
        return redirect('order:business-plan')  # Replace with your success URL

    return render(request, 'order/business_plan.html')
# def order_tabel(request):
#     pending = Order.objects.filter(user=request.user,status = 'pending').count()
#     complete = Order.objects.filter(user=request.user,status = 'completed').count()
#     all_orders = Order.objects.filter(user=request.user).all().count()

#     context = {

#         'pending': pending,
#         'completed':complete,
#         'orders':all_orders
#     }
#     # Filter orders submitted by the currently logged-in user
#     orders = Order.objects.filter(user=request.user)
#     return render(request, 'order/order_projects.html', {'orders': orders,'context': context})
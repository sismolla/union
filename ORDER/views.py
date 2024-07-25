from django.shortcuts import render,redirect
from .models import (editing,Website_project,Research,Thesis,GraphicsDesignSubmission,ProgrammingProjectSubmission,VideoEditingSubmission,Transcription,Assignment,Business_plan)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
def utility(user):
    graphics = GraphicsDesignSubmission.objects.filter(user_name=user,status='completed').count()
    programming = ProgrammingProjectSubmission.objects.filter(user_name=user,status='completed').count()
    video = VideoEditingSubmission.objects.filter(user_name=user,status='completed').count()
    transcription = Transcription.objects.filter(user_name=user,status='completed').count()
    assignment = Assignment.objects.filter(user_name=user,status='completed').count()
    business_plans = Business_plan.objects.filter(user_name=user,status='completed').count()
    researches = Research.objects.filter(user_name=user,status='completed').count()
    theses = Thesis.objects.filter(user_name=user,status='completed').count()
    website = Website_project.objects.filter(user_name=user,status='completed').count()
    edit = editing.objects.filter(user_name=user,status='completed').count()

    total_completed_orders = graphics + programming + video + assignment + business_plans + researches + theses  + transcription + website + edit

    tgraphics = GraphicsDesignSubmission.objects.filter(user_name=user,status='pending').count()
    tprogramming = ProgrammingProjectSubmission.objects.filter(user_name=user,status='pending').count()
    tvideo = VideoEditingSubmission.objects.filter(user_name=user,status='pending').count()
    ttranscription = Transcription.objects.filter(user_name=user,status='pending').count()
    tassignment = Assignment.objects.filter(user_name=user,status='pending').count()
    tbusiness_plans = Business_plan.objects.filter(user_name=user,status='pending').count()
    tresearches = Research.objects.filter(user_name=user,status='pending').count()
    ttheses = Thesis.objects.filter(user_name=user,status='pending').count()
    twebsite = Website_project.objects.filter(user_name=user,status='pending').count()
    tedit = editing.objects.filter(user_name=user,status='pending').count()

    total_pending_orders = tgraphics + tprogramming + tvideo + tassignment + tbusiness_plans + tresearches + ttheses  + ttranscription + twebsite + tedit

    total = total_pending_orders + total_completed_orders 
    
    return total,total_pending_orders,total_completed_orders

@login_required(login_url='user:login')
def profile_page(request):
    total,pending,completed = utility(request.user)
    context = {
        'total_completed':completed,
        'total_pending':pending,
        'total':total,

    }
    return render(request,'order/profile.html',context)


@login_required
def user_orders(request):
    # Retrieve orders for the logged-in user
    graphics = GraphicsDesignSubmission.objects.filter(user_name=request.user)
    programming = ProgrammingProjectSubmission.objects.filter(user_name=request.user)
    video = VideoEditingSubmission.objects.filter(user_name=request.user)
    transcription = Transcription.objects.filter(user_name=request.user)
    assignment = Assignment.objects.filter(user_name=request.user)
    business_plans = Business_plan.objects.filter(user_name=request.user)
    researches = Research.objects.filter(user_name=request.user)
    theses = Thesis.objects.filter(user_name=request.user)
    web = Website_project.objects.filter(user_name=request.user)
    edit = editing.objects.filter(user_name=request.user)
    
    total,pending,completed = utility(request.user)

    context = {
        'total_completed':completed,
        'total_pending':pending,
        'total':total,
        'business_plans': business_plans,
        'researches': researches,
        'theses': theses,
        'assignment':assignment,
        'transcriptions':transcription,
        'videos':video,
        'programmings':programming,
        'graphicss':graphics,
        'websites':web,
        'editings':edit
    }

    return render(request, 'order/ordres.html', context)

@login_required(login_url='user:login')
def completed_orders(request):
    # Retrieve orders for the logged-in user
    graphics = GraphicsDesignSubmission.objects.filter(user_name=request.user,status='completed')
    programming = ProgrammingProjectSubmission.objects.filter(user_name=request.user,status='completed')
    video = VideoEditingSubmission.objects.filter(user_name=request.user,status='completed')
    transcription = Transcription.objects.filter(user_name=request.user,status='completed')
    assignment = Assignment.objects.filter(user_name=request.user,status='completed')
    business_plans = Business_plan.objects.filter(user_name=request.user,status='completed')
    researches = Research.objects.filter(user_name=request.user,status='completed')
    theses = Thesis.objects.filter(user_name=request.user,status='completed')
    web = Website_project.objects.filter(user_name=request.user,status='completed')
    edit = editing.objects.filter(user_name=request.user,status='completed')
    total,pending,completed = utility(request.user)

    context = {
        'total_completed':completed,
        'total_pending':pending,
        'total':total,
        'business_plans': business_plans,
        'researches': researches,
        'theses': theses,
        'assignment':assignment,
        'transcriptions':transcription,
        'videos':video,
        'programmings':programming,
        'graphicss':graphics,
        'websites':web,
        'editings':edit
    }

    return render(request, 'order/completed_ordres.html', context)

@login_required(login_url='user:login')
def pending_orders(request):
    # Retrieve orders for the logged-in user
    graphics = GraphicsDesignSubmission.objects.filter(user_name=request.user,status='pending')
    programming = ProgrammingProjectSubmission.objects.filter(user_name=request.user,status='pending')
    video = VideoEditingSubmission.objects.filter(user_name=request.user,status='pending')
    transcription = Transcription.objects.filter(user_name=request.user,status='pending')
    assignment = Assignment.objects.filter(user_name=request.user,status='pending')
    business_plans = Business_plan.objects.filter(user_name=request.user,status='pending')
    researches = Research.objects.filter(user_name=request.user,status='pending')
    theses = Thesis.objects.filter(user_name=request.user,status='pending')
    web = Website_project.objects.filter(user_name=request.user,status='pending')
    edit = editing.objects.filter(user_name=request.user,status='pending')
    total,pending,completed = utility(request.user)

    context = {
        'total_completed':completed,
        'total_pending':pending,
        'total':total,
        'business_plans': business_plans,
        'researches': researches,
        'theses': theses,
        'assignment':assignment,
        'transcriptions':transcription,
        'videos':video,
        'programmings':programming,
        'graphicss':graphics,
        'websites':web,
        'editings':edit
    }

    return render(request, 'order/pending_ordres.html', context)



@login_required(login_url='user:login')
def create_research(request):
    if request.method == 'POST':
        user_name = request.user
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

        if user_name and firstname and lastname and email and phone_number and gender and titles and number_of_pages and deadline and abstract and description and accept_terms:
            Research.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,deadline=deadline,abstract=abstract,description=description,accept_terms=accept_terms)
            messages.success(request,'order submitted successfully you can see it in the dashboard ')
            
            return redirect(reverse_lazy('order:order'))
        else:
            messages.error(request,'please check the form again and check every thing is filled correctly!')
            return redirect(reverse_lazy('order:order'))
        # Replace with your success URL

    return render(request, 'order/research.html')

@login_required(login_url='user:login')
def create_thesis(request):
    if request.method == 'POST':
        user_name = request.user
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


        Thesis.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,deadline=deadline,abstract=abstract,description=description,accept_terms=accept_terms)
   
        return redirect('order:thesis')  # Replace with your success URL

    return render(request, 'order/thesis.html')


@login_required(login_url='user:login')
def graphics_design_submission(request):
    if request.method == 'POST':
        user_name = request.user
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
            user_name=user_name,
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
        user_name = request.user
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
            user_name = user_name,
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
        user_name = request.user
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
            user_name=user_name,
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
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        transcribed_file = request.POST.get('file')
        accept_terms = request.POST.get('accept_terms')
        title = request.POST.get('title')
        source_language = request.POST.get('source_language')
        target_language = request.POST.get('target_language')
        deadline = request.POST.get('deadline')

        # Save the submission to the database
        submission = Transcription(
            user_name=user_name,
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone_number=phone_number,
            gender=gender,
            accept_terms=accept_terms == 'on',
            title=title,
            source_language=source_language,
            target_language=target_language,
            deadline=deadline,
            transcribed_file = transcribed_file
        )
        submission.save()
        return redirect('order:transcription')  # Replace with your success URL

    return render(request, 'order/transcription.html')

# ////////////////////////////////////////////////////

@login_required(login_url='user:login')
def assignment(request):
    if request.method == 'POST':
        user_name = request.user
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


        Assignment.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,deadline=deadline,abstract=abstract,description=description,accept_terms=accept_terms)
   
        return redirect('order:assignment')  # Replace with your success URL

    return render(request, 'order/assignment.html')

@login_required(login_url='user:login')
def business_plan(request):
    if request.method == 'POST':
        user_name = request.user
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


        Business_plan.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,gender=gender,title=titles,number_of_pages=number_of_pages,deadline=deadline,abstract=abstract,description=description,accept_terms=accept_terms)
   
        return redirect('order:business-plan')  # Replace with your success URL

    return render(request, 'order/business_plan.html')
def website_project(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        titles = request.POST.get('title')
        web_type = request.POST.get('web-type')
        framework = request.POST.get('framework')
        deadline = request.POST.get('deadline')
        website_file = request.FILES.get('web_file')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'


        Website_project.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number,website_type = web_type, gender=gender,website_title=titles,framework=framework,deadline=deadline,website_file=website_file,description=description,accept_terms=accept_terms)
   
        return redirect('order:profile')  # Replace with your success URL

    return render(request, 'order/web_design.html')


def Writing_editing_project(request):
    if request.method == 'POST':
        user_name = request.user
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        deadline = request.POST.get('deadline')
        edited_file = request.FILES.get('edited_file')
        description = request.POST.get('description')
        accept_terms = request.POST.get('accept_terms')== 'on'


        editing.objects.create(user_name=user_name, firstname=firstname, lastname=lastname,email=email,phone_number=phone_number, gender=gender,deadline=deadline,edited_file=edited_file,description=description,accept_terms=accept_terms)
   
        return redirect('order:profile')  # Replace with your success URL

    return render(request, 'order/writhing_editing.html')

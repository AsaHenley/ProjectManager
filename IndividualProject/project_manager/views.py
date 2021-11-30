from django.shortcuts import render
from django.http import HttpResponseRedirect
from project_manager.models import BugReport, Project, Task, FeatureRequest
from project_manager.forms import CreateProject, CreateTask, Search, CreateFeatureRequest, CreateBugReport
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    sort = 'name'
    if request.method == "POST":
        search_form = Search(request.POST)
        create_form = CreateProject(request.POST)
        if create_form.is_valid() and create_form.cleaned_data['name'] != '':
            new_project = create_form.save(commit=False)
            new_project.owner = request.user
            new_project.save()
        if search_form.is_valid():
            projects = Project.objects.all()
            sort = search_form.cleaned_data['sort']
            projects = projects.filter(name__contains=search_form.cleaned_data['search_result'])
            if sort != '':
                projects = projects.order_by(sort)
    else:
        search_form = Search()
        create_form = CreateProject()
        projects = Project.objects.order_by('name')
    dict = {'projects':projects, 'search_form':search_form, 'create_form':create_form}
    return render(request, 'project_manager/home.html', dict)

@login_required(login_url='/login/')
def project(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'project_manager/project.html', {'project':project, 'id':id})

@login_required(login_url='/login/')
def task_list(request, id):
    if not request.user.is_superuser:
        return HttpResponseRedirect('/')
    tasks = Task.objects.filter(project__id = id)
    sort = 'name'
    if request.method == "POST":
        form = CreateTask(request.POST)
        search_form = Search(request.POST)
        if search_form.is_valid():
            sort = search_form.cleaned_data['sort']
            tasks = tasks.filter(name__contains=search_form.cleaned_data['search_result'])
            if sort != '':
                tasks = tasks.order_by(sort)
        if form.is_valid()  and form.cleaned_data['name'] != '':
            new_task = form.save(commit=False)
            new_task.project = Project.objects.get(id=id)
            new_task.user = request.user
            new_task.save()
            return HttpResponseRedirect("/%i/task" %id)
    else:
        form = CreateTask()
        search_form = Search()
        tasks = tasks.order_by(sort)
    dict = {'tasks':tasks, 'id':id, 'form':form, 'search_form':search_form}
    return render(request, 'project_manager/task_list.html', dict)

@login_required(login_url='/login/')
def feature_list(request, id):
    features = FeatureRequest.objects.filter(project__id = id)
    sort = 'name'
    if request.method == "POST":
        form = CreateFeatureRequest(request.POST)
        search_form = Search(request.POST)
        if search_form.is_valid():
            sort = search_form.cleaned_data['sort']
            features = features.filter(name__contains=search_form.cleaned_data['search_result'])
            if sort != '':
                features = features.order_by(sort)
        if form.is_valid()  and form.cleaned_data['name'] != '':
            new_feature = form.save(commit=False)
            new_feature.project = Project.objects.get(id=id)
            new_feature.user = request.user
            new_feature.save()
            return HttpResponseRedirect("/%i/feature" %id)
    else:
        form = CreateFeatureRequest()
        search_form = Search()
        features = features.order_by(sort)
    dict = {'features':features, 'id':id, 'form':form, 'search_form':search_form}
    
    return render(request, 'project_manager/feature_list.html', dict)

@login_required(login_url='/login/')
def bug_list(request, id):
    bugs = BugReport.objects.filter(project__id = id)
    sort = 'name'
    if request.method == "POST":
        form = CreateBugReport(request.POST)
        search_form = Search(request.POST)
        if search_form.is_valid():
            sort = search_form.cleaned_data['sort']
            bugs = bugs.filter(name__contains=search_form.cleaned_data['search_result'])
            if sort != '':
                bugs = bugs.order_by(sort)
        if form.is_valid()  and form.cleaned_data['name'] != '':
            new_bug = form.save(commit=False)
            new_bug.project = Project.objects.get(id=id)
            new_bug.user = request.user
            new_bug.save()
            return HttpResponseRedirect("/%i/bug" %id)
    else:
        form = CreateBugReport()
        search_form = Search()
        bugs = bugs.order_by(sort)
    dict = {'bugs':bugs, 'id':id, 'form':form, 'search_form':search_form}
    return render(request, 'project_manager/bug_list.html', dict)    


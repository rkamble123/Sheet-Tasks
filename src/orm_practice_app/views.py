from django.shortcuts import HttpResponse, render

'''
filter()
exclude()
                        annotate()
order_by()
reverse()
values()
values_list()
all()
get()
create()
get_or_create()
update_or_create()
bulk_create()
bulk_update()
count()
latest()
earliest()
first()
last()
aggregate()
exists()
update()
delete()
select_related()
prefetch_related()

'''
from orm_practice_app.models import Employee, ForeignProject, ManyToManyProject
from django.db.models import Avg, Count, Max, Min
from django.core.cache import cache
# Create your views here.

def home(request):

    # data = Employee.objects.all()


    # fiter
    # data = data.filter( salary_date =  '2023-01-28 18:00:00+00:00')
    # print(data)

    # print(vars(data[1]))


    #exclude
    # data = data.exclude(employee_id=102)


    # anonate


    # data = ManyToManyProject.objects \
    #     .annotate(count=Count("employee_assigned")) \
    #     .filter(count__lt=2)
    # print(data)


    # order_by
    # data = data.order_by('employee_name')
    # print(data)

    # reverse
    # data = data.reverse()[2:5]
    # print(data)

    #values
    # data = data.values('employee_name','salary')
    # print(data)

    # value_list
    # data = data.values_list('id','employee_name')
    # print(data)

    # get_or_create
    # data = ManyToManyProject.objects.get_or_create(project_name = 'Task 15')
    # print(data)

    # update_or_create
    # data = ManyToManyProject.objects.update_or_create(project_name = 'Task 15',defaults={'project_name':'Task 16'})
    # print(data)

    # bulk_create
    # data_list =[]
    # for i in range(17, 21):
    #     obj = ManyToManyProject(project_name=f"Test-{i+1}")
    #     data_list.append(obj)
    # data = ManyToManyProject.objects.bulk_create(data_list)
    # print(data)

    # bulk_update
    # count
    # data = data.count()
    # print(data)

    # latest
    # data=data.latest('employee_name')
    # print(data)

    # earliest
    # data = data.earliest('employee_name')
    # print(data)

    # first
    # data = data.first()
    # print(data)

    # last
    # data = data.last()
    # print(data)

    # aggregate
    # data = data.aggregate(Count('salary'))
    # print(data)

    # exists
    # data = data.filter(id=100).exists()
    # print(data)

    # update
    # data = data.filter(salary__gte =  20000).update( salary = 18000)
    # print(data)

    
    from django.db.models import Prefetch

    # data = Employee.objects.prefetch_related(
    #     Prefetch(
    #         "foreignproject_set",
    #         ForeignProject.objects.all()
    #         to_attr="projects"
    #     )
    # )

    # for i in data:
    #     print("Employee: ", i.employee_email)
    #     for j in i.projects:
    #         print("Project ", j.project_name)



    # select_related

    # if data is None:
    #     data = ForeignProject.objects.select_related()
    #     for i in data:
    #         print(i.Employee_assigned.salary_date)


    # Prefetch_related

    # data = Employee.objects.all()
    # for i in data:
    #     print(i)


    # data = Employee.objects.all()

    # for i in data:
    #     print(i.foreignproject_set.all())
    # data = Employee.objects.prefetch_related("foreignproject_set")



    # data = cache.get("PROJECTS_DATA")
    # if data is None:
    #     data = Employee.objects.prefetch_related("foreignproject_set")
    #     cache.set("PROJECTS_DATA", data)

    # for i in data:
    #     projects = i.foreignproject_set.all()
    #     print(projects[0])
    #     break



    # cache

    # data= cache.get('project')
    # if data is None:
    #     data = ForeignProject.objects.select_related()
    #     cache.set('project',data,15)
    #     for i in data:
    #         print(i.Employee_assigned.salary_date)



    # data = Employee.objects.all()

    # data = Employee.objects.filter(employee_name__    iexact = 'Rohan')
    # data = Employee.objects.filter(employee_name__exact = 'Rohan')
    # data = Employee.objects.filter(employee_name__contains = 's')
    # data = Employee.objects.filter(employee_name__icontains = 's')
    # data = Employee.objects.filter(employee_name__in = ['Rohan','Om'])



    data = Employee.objects.aggregate(Count('employee_name'))
    print(data)


    return render(request,'orm.html',{'data':data})
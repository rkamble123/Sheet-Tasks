from django.shortcuts import render,HttpResponse



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
from orm_practice_app.models import Employee,ManyToManyProject

# Create your views here.

def home(request):

    data = Employee.objects.all()

    # fiter
    # data = data.filter( salary_date =  '2023-01-28 18:00:00+00:00')
    # print(data)

    # print(vars(data[1]))


    #exclude
    # data = data.exclude(employee_id=102)




    # anonate

    from django.db.models import Count,Min,Max,Avg

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

    

    return render(request,'orm.html',{'data':data})


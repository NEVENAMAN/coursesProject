from django.db import models

class CourseManger(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5 :
            errors['name'] = "Course name should be at least 5 characters"
        if len(postData['desc']) < 15 :
            errors['desc'] = "Course description should be at least 15 characters"
        return errors
    

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = CourseManger()

class Comment(models.Model):
    desc = models.TextField()
    courses = models.ForeignKey(Course , related_name="comments" , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

def AddCourse(request):
    name = request.POST['name']
    desc = request.POST['desc']
    return Course.objects.create(name = name , desc = desc)

def GetCourses(request):
    return Course.objects.all()

def Get_Course_info(id):
    cours = Course.objects.get(id = id)
    return cours

def Confirm_del_course(id):
    cours = Course.objects.get(id = id)
    return cours.delete()

def AddComment(request,id):
    desc = request.POST['desc']
    courses = Course.objects.get(id=id)
    return Comment.objects.create( desc = desc , courses = courses)

def Get_comment_info(request):
    return Comment.objects.all()

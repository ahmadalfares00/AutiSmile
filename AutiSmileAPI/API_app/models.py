from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager
from rest_framework.authtoken.models import Token


# Create your models here.
#asd
class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phonenumber = models.CharField(null=True, max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USER_TYPES = (
        (1, 'Parents'),
        (2, 'Health professionals'),
        (3, 'Diagnosing person'),
        (4, 'Admin')
    )

    user_type = models.IntegerField(choices=USER_TYPES, default=3)
    REQUIRED_FIELDS = ['username', 'phonenumber', 'first_name', 'last_name', 'user_type','is_superuser'
                       ]
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

    def get_user_from_token(token):
        return Token.objects.get(key=token).user


# Index(['Case_No', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10',
#        'Age_Mons', 'Qchat-10-Score', 'Sex', 'Ethnicity', 'Jaundice',
#        'Family_mem_with_ASD', 'Who completed the test', 'Class/ASD Traits '],
#       dtype='object')

class AutismRecord(models.Model):
    Answers_choices_0_9 = (
        (1,'Always'),
        (2,'Usually'),
        (3,'Sometimes'),
        (4,'Rarely'),
        (5,'Never'),
    )
    Answers_choices_10 = (
        (1, 'Always'),
        (2, 'Usually'),
        (3, 'Sometimes'),
        (4, 'Rarely'),
        (5, 'Never'),
    )
    # Answers_choices_0_9 = (
    #     (0,'Always'),
    #     (0,'Usually'),
    #     (1,'Sometimes'),
    #     (1,'Rarely'),
    #     (1,'Never'),
    # )
    # Answers_choices_10 = (
    #     (1, 'Always'),
    #     (1, 'Usually'),
    #     (0, 'Sometimes'),
    #     (0, 'Rarely'),
    #     (0, 'Never'),
    # )
    Family_members_with_asd = (
        (1, 'Yes'),
        (0, 'No')
    )

    user = models.ForeignKey(User , null=True , default=None , on_delete=models.SET_NULL , blank=True)
    # q1 : Does your child look at you when you call his/her name ?
    A1 = models.IntegerField(default=None , null=False,choices=Answers_choices_0_9)
    # q2 :How easy is it for you to get eye contact with your child?
    A2 = models.IntegerField(default=None , null=False, choices=Answers_choices_0_9)
    # q3 :Does your child point to indicate that s/he wants something? (e.g. a toy that is  out of reach)
    A3 = models.IntegerField(default=None , null=False , choices=Answers_choices_0_9)
    # q4 :Does your child point to share interest with you? (e.g. poin9ng at an  interes9ng sight)
    A4 = models.IntegerField(default=None , null=False, choices=Answers_choices_0_9)
    # q5 :Does your child pretend? (e.g. care for dolls, talk on a toy phone)
    A5 = models.IntegerField(default=None , null=False, choices=Answers_choices_0_9)
    # q6 :Does your child follow where you’re looking?
    A6 = models.IntegerField(default=None , null=False, choices=Answers_choices_0_9)
    # q7 :If you or someone else in the family is visibly upset, does your child show signs  of wan9ng to comfort
    # them? (e.g. stroking hair, hugging them)
    A7 = models.IntegerField(default=None , null=False, choices=Answers_choices_0_9)
    # q8 :Would you describe your child’s first words as:
    A8 = models.IntegerField(default=None , null=False, choices=Answers_choices_0_9)
    # q9 :Does your child use simple gestures? (e.g. wave goodbye)
    A9 = models.IntegerField(default=None , null=False, choices=Answers_choices_0_9)
    # q10 :Does your child stare at nothing with no apparent purpose?
    A10 = models.IntegerField(default=None , null=False , choices=Answers_choices_10)
    Age_mons= models.IntegerField(null=False)
    Qchat_10_Score = models.IntegerField(null=False)
    gender = models.CharField(null=False, max_length=50 ,choices=(('Male','Male') , ('Female' , 'Female')))
    Ethnicity = models.CharField(max_length=150 , null=False)
    #Born with jaundice	Boolean  (yes or no)	Whether the case was born with jaundice
    Jaundice = models.CharField(default=None , null=False ,choices=(('Yes','Yes') , ('No','No')) , max_length=10)
    Who_completed_the_test = models.CharField(max_length=100 ,default="parent")
    Why_are_you_taken_the_screening = models.CharField(max_length=300 , default=None)
    class_variable = models.CharField(null=False ,max_length= 10 , choices=(('No','No'),('Yes','Yes')))
    percentage = models.FloatField()
    Family_mem_with_ASD = models.IntegerField(default=None,null=False,choices=Family_members_with_asd,blank=True)
    def __str__(self):
        return "" + self.class_variable[0]+ ","+  str(self.percentage)

    def save_record(request):
        Qchat_10_Score = request['A1'] + request['A2']+request['A3']+request['A4']+request['A5']+request['A6'] + request['A7'] + request['A8']+request['A9'] + request['A10']
        record = AutismRecord(user=request['user'], A1=request['A1'], A2=request['A2'], A3=request['A3'],
                              A4=request['A4'],
                              A5=request['A5'], A6=request['A6'], A7=request['A7'],
                              A8=request['A8'],
                              A9=request['A9'], A10=request['A10'], Age_mons=request['Age_mons'],
                              Qchat_10_Score=Qchat_10_Score, gender=request['gender'],
                              Ethnicity=request['Ethnicity'],
                              Jaundice=request['Jaundice'],
                              Who_completed_the_test=request['Who_completed_the_test'],
                              Family_mem_with_ASD=request['Family_mem_with_ASD'],
                              Why_are_you_taken_the_screening=request['Why_are_you_taken_the_screening'],
                              class_variable=request['y_prediction'], percentage=request['percentage']
                              )
        record.save()


class Clinic(models.Model):
    name = models.CharField(null=False, default=None , max_length=50)
    location = models.CharField(null=False, default=None , max_length=200)
    phone_number = models.CharField(null=True , default=None , max_length=50)
    email = models.CharField(null=True , default=True , max_length=50)

    def __str__(self):
        return self.name

class FeedBack(models.Model):
    user = models.ForeignKey(User , null=True , default=None , on_delete=models.SET_NULL , blank=True)
    feed = models.CharField(max_length=1000 , null=False , default=None)

    def __str__(self):
        return self.user.name


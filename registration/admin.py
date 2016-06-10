from django.contrib import admin
from registration.models import User,Student
from registration.models import User,Test
from registration.models import User,TechTest
from registration.models import User,QuantitativeTest
from registration.models import User,ReasoningTest
from registration.models import User,AptitudeTest
from registration.models import User,EligibilityTest
from registration.models import User,VerbalTest
from registration.models import User,HRTest

class UserAdmin(admin.ModelAdmin):
    pass
search_fields = ('first_name', 'last_name', 'email')
list_display = ('first_name', 'last_name', 'email')
admin.site.register(User, UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class TestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Test, TestAdmin)

class TechTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(TechTest, TechTestAdmin)


class QuantitativeTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(QuantitativeTest, QuantitativeTestAdmin)


class ReasoningTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(ReasoningTest, ReasoningTestAdmin)


class AptitudeTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(AptitudeTest, AptitudeTestAdmin)


class EligibilityTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(EligibilityTest, EligibilityTestAdmin)


class VerbalTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(VerbalTest, VerbalTestAdmin)


class HRTestAdmin(admin.ModelAdmin):
  pass
admin.site.register(HRTest, HRTestAdmin)
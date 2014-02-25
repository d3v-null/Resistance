from django.contrib import admin
from roster.models import Member, Occupation, MemberOccupation

class MemberInline(admin.StackedInline):
	model = Member
	extra = 3
	
class OccupationInline(admin.StackedInline):
	model = Occupation
	
class MemberOccupationAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': []}),
	]
	inlines = [OccupationInline]


# Register your models here.
# admin.site.register(MemberOccupation, MemberOccupationAdmin)
admin.site.register(MemberOccupation)
admin.site.register(Occupation)
admin.site.register(Member)
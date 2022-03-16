from django.contrib import admin
from .models import company, slight, AboutDetails, whyus, whypoint, serviceDetail, testimonial, team, QandA, comment
# Register your models here.

class companyInline(admin.StackedInline):
    model = company

#
# class CompanyAdmin(admin.ModelAdmin):
    # inlines = [companyInline] to get foriend kry from another page


admin.site.register(company)
admin.site.register(slight)
admin.site.register(whyus)
admin.site.register(whypoint)
admin.site.register(AboutDetails)
admin.site.register(serviceDetail)
admin.site.register(testimonial)
admin.site.register(team)
admin.site.register(QandA)
admin.site.register(comment)

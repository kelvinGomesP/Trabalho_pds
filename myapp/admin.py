from django.contrib import admin
from myapp import models

# Register your models here.
admin.site.register(models.Client) 
admin.site.register(models.RegisterLocation)


# admin.site.register(models.Immobile)
# admin.site.register(models.ImmobileImage)

#TabularInline 1 movel para varias imagens
class ImmobileImageInlineAdmin(admin.TabularInline):
    model = models.ImmobileImage
    extra = 0 #criar campo quando clicar no botâo


class ImmobileAdmin(admin.ModelAdmin):
    inlines = [ImmobileImageInlineAdmin]


admin.site.register(models.Immobile, ImmobileAdmin)
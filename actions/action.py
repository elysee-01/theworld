from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin



class Action(ImportExportModelAdmin):

    date_hierarchy = 'date_add'
    ordering = ('-date_add',)
    list_filter = ('status',)
    list_per_page = 50

    actions = ["activate", "deactivate", "toggle_status"]


    def activation(self, obj):
        if obj.status:
            return mark_safe('<img style="width:18px;height:18px" src="https://res.cloudinary.com/dfifj7ahf/image/upload/v1613241914/media/icone/true_s7tlkp.svg" alt="True">')
        else:
            return mark_safe('<img style="width:18px;height:18px" src="https://res.cloudinary.com/dfifj7ahf/image/upload/v1613241914/media/icone/false_fu6ark.svg" alt="False">')


    def deactivate(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, "Désactivation(s) effectué(s)")
    deactivate.short_description = "Désactiver les elements selectionnés"

    def activate(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, "Activation(s) effectué(s)")
    activate.short_description = "Activer les elements selectionnés"

    def toggle_status(self, request, queryset):
        for item in queryset:
            item.status = not item.status
            item.save()

        self.message_user(request, "Invertion du status effectué(s)")
    toggle_status.short_description = "Inverser les status les elements selectionnés"

    def log_addition(self, *args):
        return

    def log_change(self, *args):
        return

    def log_deletion(self, *args):
        return

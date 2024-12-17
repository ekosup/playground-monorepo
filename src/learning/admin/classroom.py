from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdmin
from unfold.contrib.import_export.forms import ImportForm, ExportForm, SelectableFieldsExportForm

from learning.models import Classroom, UserClassroom, UserClassroomTask, ClassroomTask


class UserClassroomTaskResource(resources.ModelResource):
    # Define new fields to hold related model data
    classroom_title = fields.Field(attribute='user_classroom.classroom.title', column_name='Classroom Title')
    task_title = fields.Field(attribute='task.title', column_name='Task Title')

    class Meta:
        model = UserClassroomTask
        # Specify the fields you want to export
        fields = ('id', 'user_classroom', 'task', 'score', 'classroom_title', 'task_title')  # Add other fields as necessary
        export_order = ('id', 'user_classroom', 'task', 'score', 'classroom_title', 'task_title')  # Order of fields in export
        # You can also specify the import fields if needed
        import_id_fields = ('user_classroom', 'task')  # If you want to use user_classroom and task as identifiers for imports

    def dehydrate_classroom_title(self, user_classroom_task):
        return user_classroom_task.user_classroom.classroom.title

    def dehydrate_task_title(self, user_classroom_task):
        return user_classroom_task.task.title


@admin.register(Classroom)
class ClassroomAdmin(ModelAdmin):
    pass


@admin.register(UserClassroom)
class UserClassroomAdmin(ModelAdmin):
    pass


@admin.register(ClassroomTask)
class ClassroomTaskAdmin(ModelAdmin):
    list_display = ['classroom', 'title', 'completed', 'completed_at']
    list_filter = ['classroom', 'completed']


@admin.register(UserClassroomTask)
class UserClassroomTaskAdmin(ModelAdmin, ImportExportModelAdmin):
    list_display = ['user_classroom', 'task', 'score']
    import_form_class = ImportForm
    export_form_class = ExportForm

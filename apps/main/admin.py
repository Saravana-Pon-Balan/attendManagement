from django.contrib import admin
from .models import Student, Staff
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import Widget

dept_choices = [
    ('Computer Science and Engineering', 'CSE'),
    ('Electronics and Communication Engineering', 'ECE'),
    ('Electrical and Electronic Engineering', 'EEE'),
    ('Mechanical Engineering', 'Mech'),
    ('Civil Engineering', 'Civil')
]


class ChoicesWidget(Widget):
    """
    Widget that uses choice display values in place of database values
    """

    def __init__(self, choices, *args, **kwargs):
        """
        Creates a self.choices dict with a key, display value, and value,
        db value, e.g. {'Chocolate': 'CHOC'}
        """
        self.choices = {str(value): str(key) for (key, value) in dept_choices}

    def clean(self, value, row=None):
        """Returns the db value given the display value"""
        return self.choices.get(value, value) if value else None

    def render(self, value):
        """Returns the display value given the db value"""
        for display_val, db_val in self.choices.items():
            if db_val == value:
                return display_val
        return ''


class StaffResource(resources.ModelResource):
    '''department = fields.Field(
        widget=ChoicesWidget(Staff, field='department'),
        column_name='department',
        attribute='department',
    )'''

    class Meta:
        model = Staff


class StaffAdmin(ImportExportModelAdmin):
    resource_classes = [StaffResource]


admin.site.register(Student)
admin.site.register(Staff, StaffAdmin)

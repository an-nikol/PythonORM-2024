# Generated by Django 5.0.4 on 2024-06-24 17:16

from django.db import migrations


def set_age_group(apps, schema_editor):
    person_model = apps.get_model('main_app', 'Person')

    people = person_model.objects.all()

    for person in people:  # {name: "Dido", age: 20, age_group: No age group}
        if person.age <= 12:
            person.age_group = "Child"
        elif person.age <= 17:
            person.age_group = "Teen"
        else:
            person.age_group = "Adult"

    person_model.objects.bulk_update(people, ['age_group'])


def reverse_age_group(apps, schema_editor):
    person_model = apps.get_model('main_app', 'Person')

    people = person_model.objects.all()

    for person in people:
        person.age_group = person_model._meta.get_field('age_group').default  # No age group

    person_model.objects.bulk_update(people, ['age_group'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_person'),
    ]

    operations = [
        migrations.RunPython(set_age_group, reverse_age_group)
    ]
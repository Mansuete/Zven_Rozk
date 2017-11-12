from django.shortcuts import render, render_to_response
from ControlPanel.models import Timetable, Group, Teacher


def search_form(request):
    return render_to_response('students-table/student.html')


def students(request):

    group_name = Group.objects.filter()

    return render(request, 'students-table/student.html', locals())


def teacher(request):
    timetable_teacher = Teacher.objects.filter()
    return render(request, 'teacher-table/teacher.html', locals())


def teacher_table(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        timetable_teacher = Timetable.objects.filter(teacher__teacher_name=q)

        if not timetable_teacher:
            timetable_teacher = Teacher.objects.filter()
            return render_to_response('errors/incorectteacher.html', locals())

        week1_day1_lesson1 = ''
        week1_day1_lesson2 = ''
        week1_day1_lesson3 = ''
        week1_day1_lesson4 = ''
        week1_day1_lesson5 = ''
        week1_day1_lesson6 = ''
        week1_day1_lesson7 = ''

        week1_day2_lesson1 = ''
        week1_day2_lesson2 = ''
        week1_day2_lesson3 = ''
        week1_day2_lesson4 = ''
        week1_day2_lesson5 = ''
        week1_day2_lesson6 = ''
        week1_day2_lesson7 = ''

        week1_day3_lesson1 = ''
        week1_day3_lesson2 = ''
        week1_day3_lesson3 = ''
        week1_day3_lesson4 = ''
        week1_day3_lesson5 = ''
        week1_day3_lesson6 = ''
        week1_day3_lesson7 = ''

        week1_day4_lesson1 = ''
        week1_day4_lesson2 = ''
        week1_day4_lesson3 = ''
        week1_day4_lesson4 = ''
        week1_day4_lesson5 = ''
        week1_day4_lesson6 = ''
        week1_day4_lesson7 = ''

        week1_day5_lesson1 = ''
        week1_day5_lesson2 = ''
        week1_day5_lesson3 = ''
        week1_day5_lesson4 = ''
        week1_day5_lesson5 = ''
        week1_day5_lesson6 = ''
        week1_day5_lesson7 = ''

        week2_day1_lesson1 = ''
        week2_day1_lesson2 = ''
        week2_day1_lesson3 = ''
        week2_day1_lesson4 = ''
        week2_day1_lesson5 = ''
        week2_day1_lesson6 = ''
        week2_day1_lesson7 = ''

        week2_day2_lesson1 = ''
        week2_day2_lesson2 = ''
        week2_day2_lesson3 = ''
        week2_day2_lesson4 = ''
        week2_day2_lesson5 = ''
        week2_day2_lesson6 = ''
        week2_day2_lesson7 = ''

        week2_day3_lesson1 = ''
        week2_day3_lesson2 = ''
        week2_day3_lesson3 = ''
        week2_day3_lesson4 = ''
        week2_day3_lesson5 = ''
        week2_day3_lesson6 = ''
        week2_day3_lesson7 = ''

        week2_day4_lesson1 = ''
        week2_day4_lesson2 = ''
        week2_day4_lesson3 = ''
        week2_day4_lesson4 = ''
        week2_day4_lesson5 = ''
        week2_day4_lesson6 = ''
        week2_day4_lesson7 = ''

        week2_day5_lesson1 = ''
        week2_day5_lesson2 = ''
        week2_day5_lesson3 = ''
        week2_day5_lesson4 = ''
        week2_day5_lesson5 = ''
        week2_day5_lesson6 = ''
        week2_day5_lesson7 = ''

        for i in timetable_teacher:
            if str(i.week) == "Навчальний тиждень Перший":
                if str(i.day) == "Навчальний день Понеділок":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week1_day1_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week1_day1_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week1_day1_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week1_day1_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week1_day1_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week1_day1_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week1_day1_lesson7 = i

                elif str(i.day) == "Навчальний день Вівторок":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week1_day2_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week1_day2_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week1_day2_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week1_day2_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week1_day2_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week1_day2_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week1_day2_lesson7 = i

                elif str(i.day) == "Навчальний день Середа":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week1_day3_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week1_day3_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week1_day3_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week1_day3_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week1_day3_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week1_day3_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week1_day3_lesson7 = i

                elif str(i.day) == "Навчальний день Четвер":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week1_day4_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week1_day4_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week1_day4_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week1_day4_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week1_day4_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week1_day4_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week1_day4_lesson7 = i

                elif str(i.day) == "Навчальний день П'ятниця":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week1_day5_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week1_day5_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week1_day5_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week1_day5_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week1_day5_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week1_day5_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week1_day5_lesson7 = i

            elif str(i.week) == "Навчальний тиждень Другий":
                if str(i.day) == "Навчальний день Понеділок":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week2_day1_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week2_day1_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week2_day1_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week2_day1_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week2_day1_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week2_day1_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week2_day1_lesson7 = i

                elif str(i.day) == "Навчальний день Вівторок":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week2_day2_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week2_day2_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week2_day2_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week2_day2_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week2_day2_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week2_day2_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week2_day2_lesson7 = i

                elif str(i.day) == "Навчальний день Середа":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week2_day3_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week2_day3_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week2_day3_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week2_day3_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week2_day3_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week2_day3_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week2_day3_lesson7 = i

                elif str(i.day) == "Навчальний день Четвер":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week2_day4_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week2_day4_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week2_day4_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week2_day4_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week2_day4_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week2_day4_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week2_day4_lesson7 = i

                elif str(i.day) == "Навчальний день П'ятниця":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week2_day5_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week2_day5_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week2_day5_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week2_day5_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week2_day5_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week2_day5_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week2_day5_lesson7 = i

        return render_to_response('teacher-table/teacher-table.html', locals())
    else:
        timetable_teacher = Teacher.objects.filter()
        return render_to_response('teacher-table/teacher.html', locals())


def tablepage(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q'].upper()
        timetable = Timetable.objects.filter(group__group_name=q)

        if not timetable:
            group_name = Group.objects.filter()
            return render_to_response('errors/incorectgroup.html', locals())

        name_gr = "Розклад уроків " + str(q)

        week1_day1_lesson1 = ''
        week1_day1_lesson2 = ''
        week1_day1_lesson3 = ''
        week1_day1_lesson4 = ''
        week1_day1_lesson5 = ''
        week1_day1_lesson6 = ''
        week1_day1_lesson7 = ''

        week1_day2_lesson1 = ''
        week1_day2_lesson2 = ''
        week1_day2_lesson3 = ''
        week1_day2_lesson4 = ''
        week1_day2_lesson5 = ''
        week1_day2_lesson6 = ''
        week1_day2_lesson7 = ''

        week1_day3_lesson1 = ''
        week1_day3_lesson2 = ''
        week1_day3_lesson3 = ''
        week1_day3_lesson4 = ''
        week1_day3_lesson5 = ''
        week1_day3_lesson6 = ''
        week1_day3_lesson7 = ''

        week1_day4_lesson1 = ''
        week1_day4_lesson2 = ''
        week1_day4_lesson3 = ''
        week1_day4_lesson4 = ''
        week1_day4_lesson5 = ''
        week1_day4_lesson6 = ''
        week1_day4_lesson7 = ''

        week1_day5_lesson1 = ''
        week1_day5_lesson2 = ''
        week1_day5_lesson3 = ''
        week1_day5_lesson4 = ''
        week1_day5_lesson5 = ''
        week1_day5_lesson6 = ''
        week1_day5_lesson7 = ''

        week2_day1_lesson1 = ''
        week2_day1_lesson2 = ''
        week2_day1_lesson3 = ''
        week2_day1_lesson4 = ''
        week2_day1_lesson5 = ''
        week2_day1_lesson6 = ''
        week2_day1_lesson7 = ''

        week2_day2_lesson1 = ''
        week2_day2_lesson2 = ''
        week2_day2_lesson3 = ''
        week2_day2_lesson4 = ''
        week2_day2_lesson5 = ''
        week2_day2_lesson6 = ''
        week2_day2_lesson7 = ''

        week2_day3_lesson1 = ''
        week2_day3_lesson2 = ''
        week2_day3_lesson3 = ''
        week2_day3_lesson4 = ''
        week2_day3_lesson5 = ''
        week2_day3_lesson6 = ''
        week2_day3_lesson7 = ''

        week2_day4_lesson1 = ''
        week2_day4_lesson2 = ''
        week2_day4_lesson3 = ''
        week2_day4_lesson4 = ''
        week2_day4_lesson5 = ''
        week2_day4_lesson6 = ''
        week2_day4_lesson7 = ''

        week2_day5_lesson1 = ''
        week2_day5_lesson2 = ''
        week2_day5_lesson3 = ''
        week2_day5_lesson4 = ''
        week2_day5_lesson5 = ''
        week2_day5_lesson6 = ''
        week2_day5_lesson7 = ''

        for i in timetable:
            if str(i.week) == "Навчальний тиждень Перший":
                if str(i.day) == "Навчальний день Понеділок":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week1_day1_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week1_day1_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week1_day1_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week1_day1_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week1_day1_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week1_day1_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week1_day1_lesson7 = i

                elif str(i.day) == "Навчальний день Вівторок":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week1_day2_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week1_day2_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week1_day2_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week1_day2_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week1_day2_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week1_day2_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week1_day2_lesson7 = i

                elif str(i.day) == "Навчальний день Середа":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week1_day3_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week1_day3_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week1_day3_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week1_day3_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week1_day3_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week1_day3_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week1_day3_lesson7 = i

                elif str(i.day) == "Навчальний день Четвер":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week1_day4_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week1_day4_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week1_day4_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week1_day4_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week1_day4_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week1_day4_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week1_day4_lesson7 = i

                elif str(i.day) == "Навчальний день П'ятниця":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week1_day5_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week1_day5_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week1_day5_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week1_day5_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week1_day5_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week1_day5_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week1_day5_lesson7 = i

            elif str(i.week) == "Навчальний тиждень Другий":
                if str(i.day) == "Навчальний день Понеділок":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week2_day1_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week2_day1_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week2_day1_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week2_day1_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week2_day1_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week2_day1_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week2_day1_lesson7 = i

                elif str(i.day) == "Навчальний день Вівторок":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week2_day2_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week2_day2_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week2_day2_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week2_day2_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week2_day2_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week2_day2_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week2_day2_lesson7 = i

                elif str(i.day) == "Навчальний день Середа":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week2_day3_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week2_day3_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week2_day3_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week2_day3_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week2_day3_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week2_day3_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week2_day3_lesson7 = i

                elif str(i.day) == "Навчальний день Четвер":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week2_day4_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week2_day4_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week2_day4_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week2_day4_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week2_day4_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week2_day4_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week2_day4_lesson7 = i

                elif str(i.day) == "Навчальний день П'ятниця":
                    if str(i.lesson_number) == 'Номер уроку 1':
                        week2_day5_lesson1 = i
                    elif str(i.lesson_number) == 'Номер уроку 2':
                        week2_day5_lesson2 = i
                    elif str(i.lesson_number) == 'Номер уроку 3':
                        week2_day5_lesson3 = i
                    elif str(i.lesson_number) == 'Номер уроку 4':
                        week2_day5_lesson4 = i
                    elif str(i.lesson_number) == 'Номер уроку 5':
                        week2_day5_lesson5 = i
                    elif str(i.lesson_number) == 'Номер уроку 6':
                        week2_day5_lesson6 = i
                    elif str(i.lesson_number) == 'Номер уроку 7':
                        week2_day5_lesson7 = i

        return render_to_response('students-table/tablepage.html', locals())
    else:
        group_name = Group.objects.filter()
        return render_to_response('students-table/student.html', locals())

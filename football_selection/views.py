from django.shortcuts import render
from django.db.models import Count, Q
from .models import SelectionHistory


def selection_form(request):
    message = None
    user_name = ''
    user_age = ''
    user_gender = ''

    if request.method == 'POST':
        user_name = request.POST.get('user_name', '').strip()
        user_age_str = request.POST.get('user_age', '').strip()
        user_gender = request.POST.get('user_gender', '').strip().upper()

        try:
            user_age = int(user_age_str)
        except ValueError:
            message = "Please enter a valid number for age."
            user_age = ''

        if message is None:
            if user_gender not in ["MALE", "FEMALE"]:
                message = "Invalid gender. Please select either 'Male' or 'Female'."
            elif not user_name:
                message = "Please enter your name."
            else:
                if 14 <= user_age <= 20 and user_gender == "MALE":
                    message = f"Hey {user_name}, we are delighted to inform you that you are selected."
                    SelectionHistory.objects.create(
                        name=user_name,
                        age=user_age,
                        gender=user_gender,
                        status="SELECTED",
                        reason="Age and gender criteria met for football selection"
                    )
                elif user_age <= 13:
                    message = f"Hey {user_name}, we are sorry to say that you are too young for us."
                    SelectionHistory.objects.create(
                        name=user_name,
                        age=user_age,
                        gender=user_gender,
                        status="REJECTED",
                        reason="Too young (must be 14-20 years old)"
                    )
                elif 14 <= user_age <= 20 and user_gender == "FEMALE":
                    message = f"Hey {user_name}, we are sorry to inform you that currently we are not looking for any female candidate."
                    SelectionHistory.objects.create(
                        name=user_name,
                        age=user_age,
                        gender=user_gender,
                        status="REJECTED",
                        reason="Currently not accepting female candidates"
                    )
                else:
                    message = f"Hey {user_name}, we are sorry to inform you that you are too old for our selection."
                    SelectionHistory.objects.create(
                        name=user_name,
                        age=user_age,
                        gender=user_gender,
                        status="REJECTED",
                        reason="Too old (must be 14-20 years old)"
                    )

    # Calculate statistics for pie chart
    stats = SelectionHistory.objects.aggregate(
        selected=Count('id', filter=Q(status='SELECTED')),
        rejected_young=Count('id', filter=Q(
            status='REJECTED', reason__icontains='Too young')),
        rejected_old=Count('id', filter=Q(
            status='REJECTED', reason__icontains='Too old')),
        rejected_female=Count('id', filter=Q(
            status='REJECTED', reason__icontains='female'))
    )

    total_applications = stats['selected'] + stats['rejected_young'] + \
        stats['rejected_old'] + stats['rejected_female']

    # Calculate percentages
    chart_data = {
        'selected': round((stats['selected'] / total_applications * 100), 1) if total_applications > 0 else 0,
        'rejected_young': round((stats['rejected_young'] / total_applications * 100), 1) if total_applications > 0 else 0,
        'rejected_old': round((stats['rejected_old'] / total_applications * 100), 1) if total_applications > 0 else 0,
        'rejected_female': round((stats['rejected_female'] / total_applications * 100), 1) if total_applications > 0 else 0,
    }

    history = SelectionHistory.objects.all()[:10]  # Show latest 10 records

    context = {
        'message': message,
        'user_name': user_name,
        'user_age': user_age,
        'user_gender': user_gender,
        'history': history,
        'chart_data': chart_data,
        'total_applications': total_applications,
    }

    return render(request, 'football_selection/form.html', context)

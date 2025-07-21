from django.shortcuts import render
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
                    # Save to history
                    SelectionHistory.objects.create(
                        name=user_name,
                        age=user_age,
                        gender=user_gender,
                        status="REJECTED",
                        reason="Too young (must be 14-20 years old)"
                    )
                elif 14 <= user_age <= 20 and user_gender == "FEMALE":
                    message = f"Hey {user_name}, we are sorry to inform you that currently we are not looking for any female candidate."
                    # Save to history
                    SelectionHistory.objects.create(
                        name=user_name,
                        age=user_age,
                        gender=user_gender,
                        status="REJECTED",
                        reason="Currently not accepting female candidates"
                    )
                else:
                    message = f"Hey {user_name}, we are sorry to inform you that you are too old for our selection."
                    # Save to history
                    SelectionHistory.objects.create(
                        name=user_name,
                        age=user_age,
                        gender=user_gender,
                        status="REJECTED",
                        reason="Too old (must be 14-20 years old)"
                    )

    history = SelectionHistory.objects.all()[:10]  # Show latest 10 records

    context = {
        'message': message,
        'user_name': user_name,
        'user_age': user_age,
        'user_gender': user_gender,
        'history': history,  # Add history to context
    }

    return render(request, 'football_selection/form.html', context)

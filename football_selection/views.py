from django.shortcuts import render


def selection_form(request):
    message = None
    user_name = ''
    user_age = ''
    user_gender = ''

    if request.method == 'POST':
        user_name = request.POST.get('user_name', '').strip()
        user_age_str = request.POST.get('user_age', '').strip()
        user_gender = request.POST.get('user_gender', '').strip().upper()

        # Validate Age
        try:
            user_age = int(user_age_str)
        except ValueError:
            message = "Please enter a valid number for age."
            user_age = ''  # Reset age to avoid showing invalid input

        # Validate Gender (only if age is valid)
        if message is None:  # Only proceed if age was valid
            if user_gender not in ["MALE", "FEMALE"]:
                message = "Invalid gender. Please select either 'Male' or 'Female'."
            elif not user_name:
                message = "Please enter your name."
            else:
                # Decision logic
                if 14 <= user_age <= 20 and user_gender == "MALE":
                    message = f"Hey {user_name}, we are delighted to inform you that you are selected."
                elif user_age <= 13:
                    message = f"Hey {user_name}, we are sorry to say that you are too young for us."
                elif 14 <= user_age <= 20 and user_gender == "FEMALE":
                    message = f"Hey {user_name}, we are sorry to inform you that currently we are not looking for any female candidate."
                else:
                    message = f"Hey {user_name}, we are sorry to inform you that you are too old for our selection."

    context = {
        'message': message,
        'user_name': user_name,
        'user_age': user_age,
        'user_gender': user_gender,  # Pass back to pre-fill form
    }

    return render(request, 'football_selection/form.html', context)

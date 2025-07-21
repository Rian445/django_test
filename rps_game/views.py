# rps_game/views.py
from django.shortcuts import render
import random

from .models import RPSHistory          # NEW


def play_rps(request):                                          # [2]
    user_choice = computer_choice = result_text = None

    if request.method == 'POST':
        user_input = request.POST.get('user_choice', '').upper()

        if user_input in ['R', 'P', 'S']:
            user_choice = user_input
            computer_choice = random.choice(['R', 'P', 'S'])

            if user_choice == computer_choice:
                result_code, result_text = 'T', "It's a tie!"
            elif (user_choice, computer_choice) in [
                    ('R', 'S'), ('P', 'R'), ('S', 'P')]:
                result_code, result_text = 'W', 'You win!'
            else:
                result_code, result_text = 'L', 'You lose!'

            # -------- persist the round --------
            RPSHistory.objects.create(
                user_choice=user_choice,
                computer_choice=computer_choice,
                result=result_code
            )
        else:
            result_text = "Invalid choice. Please choose Rock, Paper, or Scissors."

    context = {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result_text,
        'history': RPSHistory.objects.all()[:10],   # show 10 latest rounds
    }
    return render(request, 'rps_game/play.html', context)       # [2]

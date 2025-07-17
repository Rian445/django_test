
from django.shortcuts import render
import random


def play_rps(request):
    user_choice = None
    computer_choice = None
    result = None

    if request.method == 'POST':
        user_input = request.POST.get('user_choice', '').upper()

        if user_input in ["R", "P", "S"]:
            user_choice = user_input
            computer_choice = random.choice(["R", "P", "S"])

            if user_choice == computer_choice:
                result = "It's a tie!"
            elif (user_choice == "R" and computer_choice == "S") or \
                 (user_choice == "P" and computer_choice == "R") or \
                 (user_choice == "S" and computer_choice == "P"):
                result = "You win!"
            else:
                result = "You lose!"
        else:
            result = "Invalid choice. Please choose Rock, Paper, or Scissors."

    context = {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result,
    }
    return render(request, 'rps_game/play.html', context)

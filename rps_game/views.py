from django.db import models
from django.shortcuts import render
from django.db.models import Count, Q
import random
from .models import RPSHistory

def play_rps(request):
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
            
            
            RPSHistory.objects.create(
                user_choice=user_choice,
                computer_choice=computer_choice,
                result=result_code
            )
        else:
            result_text = "Invalid choice. Please choose Rock, Paper, or Scissors."
    
    # Calculate statistics for pie chart
    stats = RPSHistory.objects.aggregate(
        wins=Count('id', filter=Q(result='W')),
        losses=Count('id', filter=Q(result='L')),
        ties=Count('id', filter=Q(result='T'))
    )
    
    total_games = stats['wins'] + stats['losses'] + stats['ties']
    
    # Calculate percentages
    chart_data = {
        'wins': round((stats['wins'] / total_games * 100), 1) if total_games > 0 else 0,
        'losses': round((stats['losses'] / total_games * 100), 1) if total_games > 0 else 0,
        'ties': round((stats['ties'] / total_games * 100), 1) if total_games > 0 else 0,
    }
    
    context = {
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result_text,
        'history': RPSHistory.objects.all()[:10],
        'chart_data': chart_data,
        'total_games': total_games,
    }
    
    return render(request, 'rps_game/play.html', context)

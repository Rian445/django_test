from django.shortcuts import render
from django.db.models import Count, Q
import math
from .models import CalculationHistory

def calculate(request):
    """
    Handles the compound interest calculation and displays history with pie chart data.
    """
    context = {}

    if request.method == 'POST':
        try:
            principle = float(request.POST.get('principle', 0))
            rate = float(request.POST.get('rate', 0))
            time = float(request.POST.get('time', 0))

            if principle <= 0 or rate <= 0 or time <= 0:
                context['error'] = "All values must be positive numbers"
            else:
                total_amount = principle * pow((1 + rate / 100), time)

                if principle < 1_000_000:
                    millionaire_time = math.log(1_000_000 / principle) / math.log(1 + rate / 100)
                else:
                    millionaire_time = 0.0  

                is_millionaire = total_amount >= 1000000 and principle < 1000000

                CalculationHistory.objects.create(
                    principle=principle,
                    rate=rate,
                    time=time,
                    total_amount=total_amount,
                    millionaire_time=millionaire_time if is_millionaire else None
                )

                context.update({
                    'principle': principle,
                    'rate': rate,
                    'time': time,
                    'total_amount': f"{total_amount:.2f}",
                    'millionaire_time': f"{millionaire_time:.1f}" if is_millionaire else None,
                    'is_millionaire': is_millionaire
                })

        except ValueError:
            context['error'] = "Please enter valid numbers"
        except Exception as e:
            context['error'] = f"An unexpected error occurred: {e}"

    # pie chat data
    stats = CalculationHistory.objects.aggregate(
        millionaire_count=Count('id', filter=Q(millionaire_time__isnull=False)),
        non_millionaire_count=Count('id', filter=Q(millionaire_time__isnull=True))
    )
    
    total_calculations = stats['millionaire_count'] + stats['non_millionaire_count']
    
    # Calculate percentages for display
    chart_data = {
        'millionaire_count': stats['millionaire_count'],
        'non_millionaire_count': stats['non_millionaire_count'],
        'millionaire_percentage': round((stats['millionaire_count'] / total_calculations * 100), 1) if total_calculations > 0 else 0,
        'non_millionaire_percentage': round((stats['non_millionaire_count'] / total_calculations * 100), 1) if total_calculations > 0 else 0,
        'total_calculations': total_calculations
    }

    # Retrieve all calculation history records ordered by most recent first
    history = CalculationHistory.objects.all().order_by('-timestamp')
    
    context.update({
        'history': history,
        'chart_data': chart_data,
        'has_calculations': total_calculations > 0
    })

    return render(request, 'calculator/calculate.html', context)

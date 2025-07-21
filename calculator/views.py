from django.shortcuts import render
import math
from .models import CalculationHistory


def calculate(request):
    """
    Handles the compound interest calculation and displays history.
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

                # Calculate millionaire_time, handling cases where principle is already >= 1,000,000
                if principle < 1_000_000:
                    millionaire_time = math.log(
                        1_000_000 / principle) / math.log(1 + rate / 100)
                else:
                    millionaire_time = 0.0  # Already a millionaire

                is_millionaire = total_amount >= 1000000 and principle < 1000000

                # Save the calculation to history
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

    # Retrieve all calculation history records ordered by most recent first
    history = CalculationHistory.objects.all().order_by('-timestamp')
    context['history'] = history

    return render(request, 'calculator/calculate.html', context)

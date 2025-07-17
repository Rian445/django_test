from django.shortcuts import render
import math


def calculate(request):
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
                millionaire_time = math.log(
                    1_000_000 / principle) / math.log(1 + rate / 100)

                context.update({
                    'principle': principle,
                    'rate': rate,
                    'time': time,
                    'total_amount': f"{total_amount:.2f}",
                    'millionaire_time': millionaire_time,
                    'is_millionaire': total_amount >= 1000000 and principle < 1000000
                })

        except ValueError:
            context['error'] = "Please enter valid numbers"

    return render(request, 'calculator/calculate.html', context)

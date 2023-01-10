from django.shortcuts import render

def calculator(request):
    result = 0
    if request.method == 'POST':
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        symbol = request.POST.get("symbol")
        print(symbol)
        num1 = int(num1)
        num2 = int(num2)

        if symbol == '+':
            result = (num1) + (num2)
        elif symbol == '-':
            result = (num1) - (num2)
        elif symbol == '*':
            result = (num1) * (num2)
        elif symbol == '/':
            result = (num1) / (num2)
            
    return render(request, 'calculator_app/calculator.html', context={"result": result} )

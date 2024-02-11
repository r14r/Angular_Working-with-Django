from django.shortcuts import render
from django.http import JsonResponse

from decimal import getcontext, Decimal


def home(request):
    return render(request, "home.html")


def result(request):
    iterations = -1
    num1 = toInt(request.GET.get("number1", 0))
    num2 = toInt(request.GET.get("number2", 0))

    op = request.GET.get("op", "")
    format = request.GET.get("format", "html")

    if op == "":
        if request.GET.get("add") == "":
            op = "add"
        elif request.GET.get("subtract") == "":
            op = "subtract"
        elif request.GET.get("multiply") == "":
            op = "multiply"
        elif request.GET.get("divide") == "":
            op = "divide"
        elif request.GET.get("pi") == "":
            op = "pi"
        else:
            op = "divide"

    match op:
        case "add":
            ans = num1 + num2
        case "subtract":
            ans = num1 - num2
        case "multiply":
            ans = num1 * num2
        case "divide":
            ans = num1 / num2
        case "pi":
            iterations = request.GET.get("iterations", "1000")
            ans = calc_pi(iterations)
        case _:
            ans = 0

    result = {
        "num1": num1,
        "num2": num2,
        "op": op,
        "ans": ans,
        "iterations": iterations,
    }

    if format == "html":
        return render(request, "result.html", result)
    return JsonResponse(result)


def calc_pi(precision=100) -> float:
    import mpmath as m

    m.mp.dps = precision
    return str(m.mp.pi)


def toInt(number, default=None):
    try:
        return int(number)
    except Exception:
        return default

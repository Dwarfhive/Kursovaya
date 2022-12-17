from django.http import HttpResponse
from digonal.func import diag


def main(request):
    cols = request.GET.get("cols")
    rows = request.GET.get("rows")
    args = request.GET.get("args")
    d = diag(cols=cols, rows=rows, args=args)
    return HttpResponse(f"Диагональная матрица: {d}")

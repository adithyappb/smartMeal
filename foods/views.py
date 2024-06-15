from django.shortcuts import render

# Example view for foods app
def food_table(request):
    return render(request, 'food_table.html')



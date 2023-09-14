from django.shortcuts import render, redirect
from .models import Consume, Food

def index(request):
    if request.method == "POST":
        food_consumed_id = request.POST.get("food_consumed")
        consume = Food.objects.get(id=food_consumed_id)
        user = request.user        
        consume_entry = Consume(user=user, food_consumed=consume)
        consume_entry.save()
        foods = Food.objects.all()
        
    else:
        foods = Food.objects.all()
    
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, "myapp/index.html", {"foods": foods,"consumed_food": consumed_food})

def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect('/')
    else:
        return render(request,'myapp/delete.html')
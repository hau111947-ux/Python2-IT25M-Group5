from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from .models import Food, Order
from .forms import FoodForm

staff_only = user_passes_test(lambda u: u.is_staff)


# ---------- Tài khoản ----------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Đăng ký thành công!")
            return redirect('food_list')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('food_list')


# ---------- Món ăn: xem, tìm kiếm ----------
def food_list(request):
    q = request.GET.get('q', '')
    sort = request.GET.get('sort', '')
    foods = Food.objects.all()
    if q:
        foods = foods.filter(name__icontains=q)
    if sort == 'asc':
        foods = foods.order_by('price')
    elif sort == 'desc':
        foods = foods.order_by('-price')
    return render(request, 'shop/food_list.html',
                  {'foods': foods, 'q': q, 'sort': sort})


def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'shop/food_detail.html', {'food': food})


# ---------- Món ăn: thêm, sửa, xóa (chỉ admin/staff) ----------
@login_required
@staff_only
def food_create(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Đã thêm món.")
        return redirect('food_list')
    return render(request, 'shop/food_form.html',
                  {'form': form, 'title': 'Thêm món ăn'})


@login_required
@staff_only
def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    form = FoodForm(request.POST or None, instance=food)
    if form.is_valid():
        form.save()
        messages.success(request, "Đã cập nhật món.")
        return redirect('food_detail', pk=food.pk)
    return render(request, 'shop/food_form.html',
                  {'form': form, 'title': 'Sửa món ăn'})


@login_required
@staff_only
def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        food.delete()
        messages.success(request, "Đã xóa món.")
        return redirect('food_list')
    return render(request, 'shop/food_delete.html', {'food': food})


# ---------- So sánh giá ----------
def food_compare(request):
    ids = request.GET.getlist('ids')
    foods = list(Food.objects.filter(id__in=ids).order_by('price'))
    if len(foods) < 2:
        messages.error(request, "Hãy chọn ít nhất 2 món để so sánh.")
        return redirect('food_list')
    cheapest = foods[0].price
    rows = [{'food': f, 'diff': f.price - cheapest} for f in foods]
    return render(request, 'shop/compare.html', {'rows': rows})


# ---------- Đặt / hủy / hoàn ----------
@login_required
def order_create(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        try:
            qty = int(request.POST.get('quantity', 1))
        except ValueError:
            qty = 1
        if qty < 1:
            qty = 1
        Order.objects.create(user=request.user, food=food, quantity=qty)
        messages.success(request, f"Đã đặt {qty} x {food.name}.")
        return redirect('my_orders')
    return redirect('food_detail', pk=pk)


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/orders.html', {'orders': orders})


@login_required
def order_action(request, pk, action):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    if request.method == 'POST' and order.status == 'placed':
        if action == 'cancel':
            order.status = 'cancelled'
            order.save()
            messages.success(request, "Đã hủy đơn.")
        elif action == 'refund':
            order.status = 'refunded'
            order.save()
            messages.success(request, "Đã hoàn đơn.")
    return redirect('my_orders')

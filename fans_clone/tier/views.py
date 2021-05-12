from django.shortcuts import render, redirect, get_object_or_404

from .models import Tier, Subscription
from .forms import NewTierForm

from django.http import HttpResponse
from django.contrib.auth.models import User

from datetime import datetime, timedelta

def newTier_view(request):
	user = request.user

	if request.method == 'POST':
		form = NewTierForm(request.POST)

		if form.is_valid():
			description = form.cleaned_data.get('description')
			price = form.cleaned_data.get('price')
			can_message = form.cleaned_data.get('can_message')

			Tier.objects.create(description=description, price=price, user=user, can_message=can_message)
			return redirect('index')

	else:
		form = NewTierForm()

	context = {
		'form':form
	}

	return render(request, 'tier/new_tier.html', context)





def subscribe(request, username, tier_id):
	user = request.user
	subscribing = get_object_or_404(User, username=username)
	tier = Tier.objects.get(id=tier_id)



	subscription = Subscription.objects.filter(subscriber=user)

	if subscription.exists():
		subscription.delete()
	try:
		Subscription.objects.get_or_create(subscriber=user, subscribed=subscribing, tier=tier)
		return redirect('index')
	except User.DoesNotExist:
		return redirect('index')

	return redirect('index')

def fans_list(request):
	my_fans = Subscription.objects.filter(subscribed=request.user)

	context = {

		'my_fans': my_fans

	}

	return render(request, 'tier/fans_list.html', context)

def followingList(request):

    my_follows = Subscription.objects.filter(subscriber=request.user)

    for follows in my_follows:
        if follows.expired != True:
            end_date = datetime.now() - timedelta(days=30)
            remaining = follows.date.replace(tzinfo=None) - end_date.replace(tzinfo=None)
            days_left = remaining.days
            follows.date = days_left
    
    context = {
        'my_follows': my_follows
    }

    return render(request, 'tier/following_list.html', context)

def checkExpiration(request):
	exp_date = datetime.now() - timedelta(days=30)
	subs = Subscription.objects.filter(subscriber=request.user, date__lt=exp_date)
	subs.update(expired=True)
	fans = Subscription.objects.filter(subscribed=request.user, date__lt=exp_date)
	fans.update(expired=True)
	return redirect('index')
	



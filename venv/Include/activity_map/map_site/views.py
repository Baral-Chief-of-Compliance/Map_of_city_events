from django.shortcuts import render
from .models import Event
# Create your views here.

def statistics(request):
    any_types = 0
    concert_count = 0
    festival_count = 0
    entertainment_count = 0
    training_count = 0
    exhibition_count = 0
    quest_count = 0
    other_count = 0

    any_age_count = 0
    zero_count = 0
    six_count = 0
    twelve_count = 0
    fourteen_count = 0
    sixteen_count = 0
    eighteen_count = 0

    any_county = 0
    pervomaisky_count = 0
    october_count = 0
    lenin_counter = 0

    paid_count = 0
    free_count = 0

    events = Event.objects.all()
    for event in events:
        any_types = any_types + 1
        any_age_count = any_age_count + 1
        any_county = any_county + 1

        if event.category == 'Коцерт':
            concert_count = concert_count + 1
        elif event.category == 'Фестиваль':
            festival_count = festival_count + 1
        elif event.category == 'Развлечение':
            entertainment_count = entertainment_count + 1
        elif event.category == 'Тренинг':
            training_count = training_count + 1
        elif event.category == 'Выставка':
            exhibition_count = exhibition_count + 1
        elif event.category == 'Квест':
            quest_count = quest_count + 1
        elif event.category == 'Другое':
            other_count = other_count + 1

        if  event.age_limit == '0+':
            zero_count = zero_count + 1
        elif event.age_limit == '6+':
            six_count = six_count + 1
        elif event.age_limit == '12+':
            twelve_count = twelve_count + 1
        elif event.age_limit == '14+':
            fourteen_count = fourteen_count + 1
        elif event.age_limit == '16+':
            sixteen_count = sixteen_count + 1
        elif event.age_limit == '18+':
            eighteen_count = eighteen_count + 1

        if event.county == 'Первомайский':
            pervomaisky_count = pervomaisky_count + 1
        elif event.county == 'Октябрьский':
            october_count = october_count + 1
        elif event.county == 'Ленинский':
            lenin_counter = lenin_counter + 1

        if event.paid:
            paid_count = paid_count + 1
        else:
            free_count = free_count + 1

    context = {
        "any_types": any_types,
        "concert_count": concert_count,
        "festival_count": festival_count,
        "entertainment_count": entertainment_count,
        "training_count": training_count,
        "exhibition_count": exhibition_count,
        "quest_count": quest_count,
        "other_count": other_count,
        "any_age_count": any_age_count,
        "zero_count": zero_count,
        "six_count": six_count,
        "twelve_count": twelve_count,
        "fourteen_count": fourteen_count,
        "sixteen_count": sixteen_count,
        "eighteen_count": eighteen_count,
        "any_county": any_county,
        "pervomaisky_count": pervomaisky_count,
        "october_count": october_count,
        "lenin_counter": lenin_counter,
        "paid_count": paid_count,
        "free_count": free_count
    }
    return render(request, 'map_site/statistics.html', context)


def statistics_types(request):

    any_types = 0
    concert_count = 0
    festival_count = 0
    entertainment_count = 0
    training_count = 0
    exhibition_count = 0
    quest_count = 0
    other_count = 0

    events = Event.objects.all()

    for event in events:
        any_types = any_types + 1

        if event.category == 'Коцерт':
            concert_count = concert_count + 1
        elif event.category == 'Фестиваль':
            festival_count = festival_count + 1
        elif event.category == 'Развлечение':
            entertainment_count = entertainment_count + 1
        elif event.category == 'Тренинг':
            training_count = training_count + 1
        elif event.category == 'Выставка':
            exhibition_count = exhibition_count + 1
        elif event.category == 'Квест':
            quest_count = quest_count + 1
        elif event.category == 'Другое':
            other_count = other_count + 1

    context = {
        "any_types": any_types,
        "concert_count": concert_count,
        "festival_count": festival_count,
        "entertainment_count": entertainment_count,
        "training_count": training_count,
        "exhibition_count": exhibition_count,
        "quest_count": quest_count,
        "other_count": other_count
    }

    return render(request, 'map_site/statistics_types.html', context)


def statistics_age(request):

    any_age_count = 0
    zero_count = 0
    six_count = 0
    twelve_count = 0
    fourteen_count = 0
    sixteen_count = 0
    eighteen_count = 0

    events = Event.objects.all()

    for event in events:

        any_age_count = any_age_count + 1

        if  event.age_limit == '0+':
            zero_count = zero_count + 1
        elif event.age_limit == '6+':
            six_count = six_count + 1
        elif event.age_limit == '12+':
            twelve_count = twelve_count + 1
        elif event.age_limit == '14+':
            fourteen_count = fourteen_count + 1
        elif event.age_limit == '16+':
            sixteen_count = sixteen_count + 1
        elif event.age_limit == '18+':
            eighteen_count = eighteen_count + 1

    context = {
        "any_age_count": any_age_count,
        "zero_count": zero_count,
        "six_count": six_count,
        "twelve_count": twelve_count,
        "fourteen_count": fourteen_count,
        "sixteen_count": sixteen_count,
        "eighteen_count": eighteen_count
    }

    return render(request, 'map_site/statistics_age.html', context)


def statistics_county(request):

    any_county = 0
    pervomaisky_count = 0
    october_count = 0
    lenin_counter = 0

    events = Event.objects.all()

    for event in events:

        if event.county == 'Первомайский':
            pervomaisky_count = pervomaisky_count + 1
        elif event.county == 'Октябрьский':
            october_count = october_count + 1
        elif event.county == 'Ленинский':
            lenin_counter = lenin_counter + 1

    context = {
        "any_county": any_county,
        "pervomaisky_count": pervomaisky_count,
        "october_count": october_count,
        "lenin_counter": lenin_counter
    }

    return render(request, 'map_site/statistics_county.html', context)


def statistics_paid(request):

    paid_count = 0
    free_count = 0

    events = Event.objects.all()

    for event in events:

        if event.paid:
            paid_count = paid_count + 1
        else:
            free_count = free_count + 1

    context = {
        "paid_count": paid_count,
        "free_count": free_count
    }

    return render(request, 'map_site/statistics_paid.html', context)
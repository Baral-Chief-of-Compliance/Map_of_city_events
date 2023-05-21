from django.shortcuts import render
from .models import Event, EventImg
from django.contrib.admin.views.decorators import staff_member_required
from .forms import DateForm
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@staff_member_required
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
            list_concert.append(event)

        elif event.category == 'Фестиваль':
            festival_count = festival_count + 1
            list_festival.append(event)

        elif event.category == 'Развлечение':
            entertainment_count = entertainment_count + 1
            list_entertainment.append(event)

        elif event.category == 'Тренинг':
            training_count = training_count + 1
            list_training.append(event)

        elif event.category == 'Выставка':
            exhibition_count = exhibition_count + 1
            list_exhibition.append(event)

        elif event.category == 'Квест':
            quest_count = quest_count + 1
            list_quest.append(event)

        elif event.category == 'Другое':
            other_count = other_count + 1
            list_other.append(event)

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
        "free_count": free_count,

        "list_concert": list_concert,
        "list_festival": list_festival,
        "list_entertainment": list_entertainment,
        "list_training": list_training,
        "list_exhibition": list_exhibition,
        "list_quest": list_quest,
        "list_other": list_other
    }
    return render(request, 'map_site/statistics.html', context)


@staff_member_required
def statistics_types(request):

    any_types = 0
    concert_count = 0
    festival_count = 0
    entertainment_count = 0
    training_count = 0
    exhibition_count = 0
    quest_count = 0
    other_count = 0

    list_concert =[]
    list_festival = []
    list_entertainment = []
    list_training = []
    list_exhibition = []
    list_quest = []
    list_other = []

    events = Event.objects.all()

    for event in events:
        any_types = any_types + 1

        if event.category == 'Коцерт':
            concert_count = concert_count + 1
            list_concert.append(event)

        elif event.category == 'Фестиваль':
            festival_count = festival_count + 1
            list_festival.append(event)

        elif event.category == 'Развлечение':
            entertainment_count = entertainment_count + 1
            list_entertainment.append(event)

        elif event.category == 'Тренинг':
            training_count = training_count + 1
            list_training.append(event)

        elif event.category == 'Выставка':
            exhibition_count = exhibition_count + 1
            list_exhibition.append(event)

        elif event.category == 'Квест':
            quest_count = quest_count + 1
            list_quest.append(event)

        elif event.category == 'Другое':
            other_count = other_count + 1
            list_other.append(event)


    context = {
        "any_types": any_types,
        "concert_count": concert_count,
        "festival_count": festival_count,
        "entertainment_count": entertainment_count,
        "training_count": training_count,
        "exhibition_count": exhibition_count,
        "quest_count": quest_count,
        "other_count": other_count,

        "list_concert": list_concert,
        "list_festival": list_festival,
        "list_entertainment": list_entertainment,
        "list_training": list_training,
        "list_exhibition": list_exhibition,
        "list_quest": list_quest,
        "list_other": list_other
    }

    return render(request, 'map_site/statistics_types.html', context)


@staff_member_required
def statistics_age(request):

    any_age_count = 0
    zero_count = 0
    six_count = 0
    twelve_count = 0
    fourteen_count = 0
    sixteen_count = 0
    eighteen_count = 0

    list_zero =[]
    list_six = []
    list_twelve = []
    list_fourteen = []
    list_sixteen = []
    list_eighteen = []

    events = Event.objects.all()

    for event in events:

        any_age_count = any_age_count + 1

        if  event.age_limit == '0+':
            zero_count = zero_count + 1
            list_zero.append(event)

        elif event.age_limit == '6+':
            six_count = six_count + 1
            list_six.append(event)

        elif event.age_limit == '12+':
            twelve_count = twelve_count + 1
            list_twelve.append(event)

        elif event.age_limit == '14+':
            fourteen_count = fourteen_count + 1
            list_fourteen.append(event)

        elif event.age_limit == '16+':
            sixteen_count = sixteen_count + 1
            list_sixteen.append(event)

        elif event.age_limit == '18+':
            eighteen_count = eighteen_count + 1
            list_eighteen.append(event)


    context = {
        "any_age_count": any_age_count,
        "zero_count": zero_count,
        "six_count": six_count,
        "twelve_count": twelve_count,
        "fourteen_count": fourteen_count,
        "sixteen_count": sixteen_count,
        "eighteen_count": eighteen_count,

        "list_zero": list_zero,
        "list_six": list_six,
        "list_twelve": list_twelve,
        "list_fourteen": list_fourteen,
        "list_sixteen": list_sixteen,
        "list_eighteen": list_eighteen

    }

    return render(request, 'map_site/statistics_age.html', context)


@staff_member_required
def statistics_county(request):

    any_county = 0
    pervomaisky_count = 0
    october_count = 0
    lenin_counter = 0

    pervomaisky_list = []
    october_list = []
    lenin_list = []

    events = Event.objects.all()

    for event in events:

        any_county = any_county + 1

        if event.county == 'Первомайский':
            pervomaisky_count = pervomaisky_count + 1
            pervomaisky_list.append(event)

        elif event.county == 'Октябрьский':
            october_count = october_count + 1
            october_list.append(event)

        elif event.county == 'Ленинский':
            lenin_counter = lenin_counter + 1
            lenin_list.append(event)

    context = {
        "any_county": any_county,
        "pervomaisky_count": pervomaisky_count,
        "october_count": october_count,
        "lenin_counter": lenin_counter,

        "pervomaisky_list": pervomaisky_list,
        "october_list": october_list,
        "lenin_list": lenin_list
    }

    return render(request, 'map_site/statistics_county.html', context)


@staff_member_required
def statistics_paid(request):

    paid_count = 0
    free_count = 0

    list_paid = []
    list_free = []

    events = Event.objects.all()

    for event in events:

        if event.paid:
            paid_count = paid_count + 1
            list_paid.append(event)

        else:
            free_count = free_count + 1
            list_free.append(event)

    context = {
        "paid_count": paid_count,
        "free_count": free_count,

        "list_paid": list_paid,
        "list_free": list_free
    }

    return render(request, 'map_site/statistics_paid.html', context)


@staff_member_required
def statistics_date(request):

    if request.method == 'POST':
        form = DateForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data['start_of_interval'])
            print(form.cleaned_data['end_of_interval'])
            return HttpResponseRedirect(f'/statistics_date/{form.cleaned_data["start_of_interval"]}-{form.cleaned_data["end_of_interval"]}')

    else:
        form = DateForm()

    return render(request, 'map_site/statistics_date.html')


@staff_member_required
def statistics_interval(request, start_year, start_month, start_day, end_year, end_month,  end_day):

    event_counter = 0

    list_of_event = []

    events = Event.objects.all()

    date_of_start = f"{start_year}-{start_month}-{start_day}"
    date_of_end = f"{end_year}-{end_month}={end_day}"

    for event in events:

        if (str(event.dt_of_start)[0:10] >= date_of_start) and (str(event.dt_of_end)[0:10]) <= date_of_end:
            event_counter = event_counter + 1
            list_of_event.append(event)

        elif (str(event.dt_of_start)[0:10] <=  date_of_start) and (str(event.dt_of_end)[0:10]) >= date_of_end:
            event_counter = event_counter + 1
            list_of_event.append(event)

        elif (str(event.dt_of_start)[0:10] >=  date_of_start and str(event.dt_of_start)[0:10] <= date_of_end) and (str(event.dt_of_end)[0:10]) >= date_of_end:
            event_counter = event_counter + 1
            list_of_event.append(event)

        elif (str(event.dt_of_start)[0:10] <=  date_of_start) and ((str(event.dt_of_end)[0:10]) <= date_of_end and (str(event.dt_of_end)[0:10]) >= date_of_start):
            event_counter = event_counter + 1
            list_of_event.append(event)


    context = {
        "start_year": start_year,
        "start_month": start_month,
        "start_day": start_day,
        "end_year": end_year,
        "end_month": end_month,
        "end_day": end_day,
        "event_counter": event_counter,
        "events": list_of_event
    }
    return render(request, 'map_site/statistics_interval.html', context)


def all_events(request):
    events = Event.objects.all()
    imgs = EventImg.objects.all()

    json_events = []


    for event in events:
        json_img = []

        for img in imgs:
            if event.id == img.events.id:
                json_img.append(img.img.url)


        json_events.append(
            {
                "id": event.id,
                "name": event.name,
                "dt_of_start": event.dt_of_start,
                "town": event.town,
                "street": event.street,
                "house": event.house,
                "frame": event.frame,
                "url": event.url,
                "county": event.county,
                "category": event.category,
                "img": json_img,
                "latitude": event.latitude,
                "longitude": event.longitude
            }
        )

    return JsonResponse({'events': json_events})


@csrf_exempt
def use_filter(request):
    if request.method == 'GET':
        return JsonResponse({'foo': "bar"})

    elif request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        town_list = body["town_list"]
        county_list = body["county_list"]
        type_list = body["type_list"]

        events = Event.objects.all()

        filter_event = []
        list_events = []

        def get_image(event):
            imgs = EventImg.objects.all()
            json_img = []

            for img in imgs:
                if event.id == img.events.id:
                    json_img.append(img.img.url)
            return json_img

        def create_json_object(list_ev, event):
            list_ev.append(
                {
                    "id": event.id,
                    "name": event.name,
                    "dt_of_start": event.dt_of_start,
                    "town": event.town,
                    "street": event.street,
                    "house": event.house,
                    "frame": event.frame,
                    "url": event.url,
                    "county": event.county,
                    "category": event.category,
                    "img": get_image(event),
                    "latitude": event.latitude,
                    "longitude": event.longitude
                }
            )

            return list_ev

        def check_element(list_ev, event):
            id_ev = event.id
            for ev in list_ev:
                if ev.id == id_ev:
                    return False
                else:
                    return True

        if ("Все города" in town_list) or ("Выбрать все" in county_list) or ("Выбрать все" in type_list):
            for event in events:
                filter_event = create_json_object(filter_event, event)

            return JsonResponse({'events': filter_event})

        else:

            for event in events:

                for town in town_list:
                    if town == event.town:
                        filter_event = create_json_object(filter_event, event)
                        list_events.append(event)

                for county in county_list:
                    if county == event.county:
                        if event in list_events:
                            pass
                        else:
                            filter_event = create_json_object(filter_event, event)
                            list_events.append(event)

                for type_ev in type_list:
                    if type_ev == event.category:
                        if event in list_events:
                            pass
                        else:
                            filter_event = create_json_object(filter_event, event)
                            list_events.append(event)

            return JsonResponse({'events': filter_event})


@csrf_exempt
def categories_filter(request):

    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        town_list = body["town_list"]
        county_list = body["county_list"]
        type_list = body["type_list"]
        age_limit_list = body["age_limit_list"]

        events = Event.objects.all()

        filter_event = []
        list_events = []

        def get_image(event):
            imgs = EventImg.objects.all()
            json_img = []

            for img in imgs:
                if event.id == img.events.id:
                    json_img.append(img.img.url)
            return json_img

        def create_json_object(list_ev, event):
            list_ev.append(
                {
                    "id": event.id,
                    "name": event.name,
                    "dt_of_start": event.dt_of_start,
                    "town": event.town,
                    "street": event.street,
                    "house": event.house,
                    "frame": event.frame,
                    "url": event.url,
                    "county": event.county,
                    "category": event.category,
                    "img": get_image(event),
                    "latitude": event.latitude,
                    "longitude": event.longitude
                }
            )

            return list_ev

        def check_element(list_ev, event):
            id_ev = event.id
            for ev in list_ev:
                if ev.id == id_ev:
                    return False
                else:
                    return True

        if ("Все города" in town_list) or ("Выбрать все" in county_list) or ("Выбрать все" in type_list) or ("Выбрать все" in age_limit_list):
            for event in events:
                filter_event = create_json_object(filter_event, event)

            return JsonResponse({'events': filter_event})

        else:

            for event in events:

                for town in town_list:
                    if town == event.town:
                        filter_event = create_json_object(filter_event, event)
                        list_events.append(event)

                for county in county_list:
                    if county == event.county:
                        if event in list_events:
                            pass
                        else:
                            filter_event = create_json_object(filter_event, event)
                            list_events.append(event)

                for type_ev in type_list:
                    if type_ev == event.category:
                        if event in list_events:
                            pass
                        else:
                            filter_event = create_json_object(filter_event, event)
                            list_events.append(event)

                for age in age_limit_list:
                    if age == event.age_limit:
                        if event in list_events:
                            pass
                        else:
                            filter_event = create_json_object(filter_event, event)
                            list_events.append(event)

            print(filter_event)
            return JsonResponse({'events': filter_event})
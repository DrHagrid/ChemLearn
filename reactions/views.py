from django.http import JsonResponse
from django.shortcuts import render
from reactions.models import Reaction
from users.models import UserInfo
import random


def check_answer(request):
    return_dict = dict()
    data = request.POST
    answer = data.get("answer")
    reaction_id = data.get("reaction_id")
    reaction = Reaction.objects.get(pk=reaction_id)

    replica_success = random.choice([
        'Верно! Откуда ты это знаешь, жук?',
        'Правильно. ТЫ ЧЕ, ПЁС, самый умный?',
        'Верно! Ты что компьютер!?'
    ])
    replica_fail = random.choice([
        'Ну ты и простофиля! Попробуй ещё...',
        'Не верно! Как тебя вообще земля носит?',
        'Я вижу у тебя трисомия 21 хромосомы. Попробуй ещё раз!'
    ])

    reaction_number = len(Reaction.objects.all())
    return_dict["response"] = False
    initial = reaction.products.lower().replace(' ', '').split('+')
    entrance = answer.lower().replace(' ', '').split('+')
    intersection = list(set(initial) & set(entrance))

    return_dict["replica_success"] = replica_success
    return_dict["replica_fail"] = replica_fail

    if (len(entrance) == len(initial)) and (len(entrance) == len(intersection)):
        next_reaction_id = int(reaction_id) + 1

        user_info = UserInfo.objects.get(user=request.user)
        user_info.last_reaction = next_reaction_id
        user_info.save(force_update=True)

        return_dict["response"] = True
        return_dict["next_reaction_id"] = next_reaction_id
        return_dict["products_trans"] = reaction.products_trans

    return JsonResponse(return_dict)

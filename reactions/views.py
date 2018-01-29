from django.http import JsonResponse
from django.shortcuts import render
from reactions.models import Reaction
from users.models import UserInfo


def check_answer(request):
    return_dict = dict()
    data = request.POST
    answer = data.get("answer")
    reaction_id = data.get("reaction_id")
    reaction = Reaction.objects.get(pk=reaction_id)

    reaction_number = len(Reaction.objects.all())
    return_dict["response"] = False
    initial = reaction.products.lower().replace(' ', '').split('+')
    entrance = answer.lower().replace(' ', '').split('+')
    intersection = list(set(initial) & set(entrance))
    if (len(entrance) == len(initial)) and (len(entrance) == len(intersection)):
        next_reaction_id = int(reaction_id) + 1
        user_info = UserInfo.objects.get(user=request.user)
        user_info.last_reaction = next_reaction_id
        user_info.save(force_update=True)
        return_dict["response"] = True
        return_dict["next_reaction_id"] = next_reaction_id
        return_dict["products_trans"] = reaction.products_trans

    return JsonResponse(return_dict)

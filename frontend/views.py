from django.shortcuts import render
from reactions.models import Reaction
import random


def reaction_test_page(request, reaction_id):
    reaction_number = len(Reaction.objects.all())

    replica_common = random.choice([
        'Оба-ёба! А ну реши мне эту реакцию. Сможешь?',
        'Это реакцию ты точно не знаешь...',
        'Сможешь ли ты дописать эту реакцию?'
    ])

    if int(reaction_id) > reaction_number:
        return render(request, 'error_end-of-reactions.html', locals())
    else:
        reaction = Reaction.objects.get(pk=reaction_id)
        return render(request, 'reaction_test_page.html', locals())

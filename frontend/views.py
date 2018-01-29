from django.shortcuts import render
from reactions.models import Reaction


def reaction_test_page(request, reaction_id):
    reaction_number = len(Reaction.objects.all())
    if int(reaction_id) > reaction_number:
        return render(request, 'error_end-of-reactions.html', locals())
    else:
        reaction = Reaction.objects.get(pk=reaction_id)
        return render(request, 'reaction_test_page.html', locals())

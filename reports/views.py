from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from challenges.models import Challenge


@login_required
def report(request, id):
    if request.method == 'GET':
        challenge = Challenge.objects.get(id=id)
        hits = challenge.flashcards.filter(got_it_right=True).count()
        errors = challenge.flashcards.filter(got_it_right=False).count()
        name_category = [c.name for c in challenge.category.all()]

        result = [hits, errors]
        hits_category = []
        for c in challenge.category.all():
            hits_category.append(
                challenge.flashcards.filter(flashcard__category=c)
                .filter(got_it_right=True)
                .count()
            )

        return render(
            request,
            'report.html',
            {
                'challenge': challenge,
                'result': result,
                'categories': name_category,
                'hits_category': hits_category,
            },
        )

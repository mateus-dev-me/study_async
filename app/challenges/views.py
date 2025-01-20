from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from flashcards.models import Category, FlashCard

from .models import Challenge, FlashCardChallenge


@login_required
def create_challenge(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        difficulties = FlashCard.DIFFICULTY_CHOICES

        return render(
            request,
            'new_challenge.html',
            {'categories': categories, 'difficulties': difficulties},
        )

    elif request.method == 'POST':
        title = request.POST.get('title')
        categories = request.POST.getlist('category')
        difficulty = request.POST.get('difficulty')
        number_questions = request.POST.get('number_questions')

        challenge = Challenge(
            user=request.user,
            title=title,
            number_questions=number_questions,
            difficulty=difficulty,
        )

        challenge.save()
        challenge.category.add(*categories)

        flashcards = (
            FlashCard.objects.filter(user=request.user)
            .filter(difficulty=difficulty)
            .filter(category_id__in=categories)
            .order_by('?')
        )

        if flashcards.count() < int(number_questions):
            challenge.delete()
            messages.add_message(
                request,
                constants.ERROR,
                'Não foi possível criar este desafio.',
            )

            return redirect('/challenges/new_challenge')

        for flashcard in flashcards:
            flashcard_challenge = FlashCardChallenge(flashcard=flashcard)
            flashcard_challenge.save()
            challenge.flashcards.add(flashcard_challenge)

        challenge.save()

        return redirect('/challenges/list_challenges')


@login_required
def list_challenges(request):
    if request.method == 'GET':
        challenges = Challenge.objects.filter(user=request.user)
        difficulties = FlashCard.DIFFICULTY_CHOICES
        categories = Category.objects.all()

        filter_difficulty = request.GET.get('difficulty')
        filter_category = request.GET.get('category')

        print(filter_category)
        print(filter_category)

        if filter_difficulty:
            challenges = challenges.filter(difficulty=filter_difficulty)
        if filter_category:
            challenges = challenges.filter(category=filter_category)

        return render(
            request,
            'list_challengs.html',
            {
                'challenges': challenges,
                'difficulties': difficulties,
                'categories': categories,
            },
        )


@login_required
def challenge(request, id):
    if request.method == 'GET':
        challenge = Challenge.objects.get(id=id)

        result = {
            'hits': 0,
            'errors': 0,
            'missing': challenge.flashcards.count(),
        }
        for flash in challenge.flashcards.all():
            if flash.answered:
                result['missing'] -= 1

                if flash.got_it_right:
                    result['hits'] += 1
                else:
                    result['errors'] += 1

        return render(
            request,
            'challenge.html',
            {'challenge': challenge, 'result': result},
        )


@login_required
def remove_challenge(request, id):
    challenge = Challenge.objects.get(id=id)

    for flashcard_challange in challenge.flashcards.all():
        flashcard_challange.delete()
    challenge.delete()

    return redirect('/challenges/list_challenges')

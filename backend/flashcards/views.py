from challenges.models import FlashCardChallenge
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.shortcuts import redirect, render

from .models import Category, FlashCard


@login_required
def create_flashcard(request):
    if request.method == 'GET':
        flashcards = FlashCard.objects.filter(user=request.user)
        categories = Category.objects.all()
        difficulties = FlashCard.DIFFICULTY_CHOICES

        filter_category = request.GET.get('category')
        filter_difficulty = request.GET.get('difficulty')

        if filter_category:
            flashcards = flashcards.filter(category_id=filter_category)
        if filter_difficulty:
            flashcards = flashcards.filter(difficulty=filter_difficulty)

        return render(
            request,
            'new_flashcard.html',
            {
                'categories': categories,
                'difficulties': difficulties,
                'flashcards': flashcards,
            },
        )
    elif request.method == 'POST':
        user = request.user
        question = request.POST.get('question')
        response = request.POST.get('response')
        category = request.POST.get('category')
        difficulty = request.POST.get('difficulty')

        if len(question.strip()) == 0 or len(response.strip()) == 0:
            messages.add_message(
                request,
                constants.ERROR,
                'Preencha os campos de pergunta e resposta.',
            )
            return redirect('/flashcards/new_flashcard/')

        try:
            flashcard = FlashCard(
                user=user,
                question=question,
                response=response,
                category_id=category,
                difficulty=difficulty,
            )
            flashcard.save()
            messages.add_message(
                request, constants.SUCCESS, 'Flashcard cadastrado com sucesso!'
            )
            return redirect('/flashcards/new_flashcard')
        except Exception:
            messages.add_message(
                request,
                constants.ERROR,
                'Aconteceu um erro ao cadastrar o flashcard.',
            )
            return redirect('/flashcards/new_flashcard/')


@login_required
def remove_flashcard(request, id):
    try:
        flashcard = (
            FlashCard.objects.filter(user=request.user).filter(id=id).first()
        )
        flashcard.delete()
        messages.add_message(
            request, constants.SUCCESS, 'Flashcard deletado com sucesso.'
        )
        return redirect('/flashcards/new_flashcard')
    except Exception:
        return redirect('/flashcards/new_flashcard')


@login_required
def reply_flashcard(request, id):
    flashcard = FlashCardChallenge.objects.get(id=id)
    right = request.GET.get('right')
    challenge_id = request.GET.get('challenge')

    flashcard.answered = True
    flashcard.got_it_right = True if right == '1' else False
    flashcard.save()
    return redirect(f'/challenges/challenge/{challenge_id}')

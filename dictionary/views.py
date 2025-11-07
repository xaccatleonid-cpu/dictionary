from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Language, Word
from .forms import LanguageForm, WordForm


def home(request):
    languages = Language.objects.all()
    return render(request, 'dictionary/home.html', {'languages': languages})


def language_detail(request, pk):
    language = get_object_or_404(Language, pk=pk)
    words = language.words.all()
    return render(request, 'dictionary/language_detail.html', {'language': language, 'words': words})


def add_language(request):
    form = LanguageForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dictionary:home')
    cancel_link = reverse('dictionary:home')
    return render(request, 'dictionary/form.html', {
        'form': form,
        'title': 'Добавить язык',
        'cancel_link': cancel_link
    })


def edit_language(request, pk):
    language = get_object_or_404(Language, pk=pk)
    form = LanguageForm(request.POST or None, instance=language)
    if form.is_valid():
        form.save()
        return redirect('dictionary:home')
    cancel_link = reverse('dictionary:home')
    return render(request, 'dictionary/form.html', {
        'form': form,
        'title': 'Редактировать язык',
        'cancel_link': cancel_link
    })


def delete_language(request, pk):
    language = get_object_or_404(Language, pk=pk)
    language.delete()
    return redirect('dictionary:home')


def add_word(request, pk):
    language = get_object_or_404(Language, pk=pk)
    form = WordForm(request.POST or None, initial={'language': language})
    if form.is_valid():
        form.save()
        return redirect('dictionary:language_detail', pk=pk)
    cancel_link = reverse('dictionary:language_detail', args=[pk])
    return render(request, 'dictionary/form.html', {
        'form': form,
        'title': 'Добавить слово',
        'cancel_link': cancel_link
    })


def edit_word(request, pk):
    word = get_object_or_404(Word, pk=pk)
    form = WordForm(request.POST or None, instance=word)
    if form.is_valid():
        form.save()
        return redirect('dictionary:language_detail', pk=word.language.pk)
    cancel_link = reverse('dictionary:language_detail', args=[word.language.pk])
    return render(request, 'dictionary/form.html', {
        'form': form,
        'title': 'Редактировать слово',
        'cancel_link': cancel_link
    })


def delete_word(request, pk):
    word = get_object_or_404(Word, pk=pk)
    language_pk = word.language.pk
    word.delete()
    return redirect('dictionary:language_detail', pk=language_pk)


def confirm_delete_language(request, pk):
    language = get_object_or_404(Language, pk=pk)
    if request.method == 'POST':
        language.delete()
        return redirect('dictionary:home')
    return render(request, 'dictionary/confirm_delete.html', {
        'object': language,
        'type': 'язык',
        'cancel_url': 'dictionary:home'
    })


def confirm_delete_word(request, pk):
    word = get_object_or_404(Word, pk=pk)
    if request.method == 'POST':
        language_pk = word.language.pk
        word.delete()
        return redirect('dictionary:language_detail', pk=language_pk)
    return render(request, 'dictionary/confirm_delete.html', {
        'object': word,
        'type': 'слово',
        'cancel_url': 'dictionary:language_detail',
        'cancel_args': [word.language.pk]
    })

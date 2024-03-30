from django.shortcuts import render
from .models import Class, Subject, Chapter
from django.http import JsonResponse
from questions.models import Question, Answer
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def home_page(request):
    return render(request,'quizes/home.html')

def start_quiz(request):
    classes = []

    for cls in Class.objects.all():
        class_data = {
            'name': cls.name,
            'subject': []
        }
        for subject in cls.get_subjects():
            subject_data = {
                'name': subject.name,
                'slug': subject.slug,
                'chapter': []
            }
            for chapter in subject.get_chapters():
                chapter_data = {
                    'name': chapter.name,
                    'slug': chapter.slug
                }
                subject_data['chapter'].append(chapter_data)
            class_data['subject'].append(subject_data)
        classes.append(class_data)

    return JsonResponse({'data': classes})


def quiz_view(request,slug):
    chapter = Chapter.objects.get(slug=slug)
    return render(request, 'quizes/quiz.html', {'chapter': chapter})

def quiz_data_view(request, slug):
    chapter = Chapter.objects.get(slug=slug)

    questions = []
    for question in chapter.get_questions():
        answers = []
        for answer in question.get_answers():
            answers.append(answer.text)
        questions.append({str(question): answers})

    return JsonResponse({'data': questions})


def save_quiz_view(request, slug):
    chapter = Chapter.objects.get(slug=slug)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        questions = []
        data_ = request.POST
        data = dict(data_)
        data.pop('csrfmiddlewaretoken')

        for k in data.keys():
            question = Question.objects.get(text = k)
            questions.append(question)
            print(questions)

            score = 0
            multiplier = 100 / chapter.number_of_questions
            results = []

            for q in questions:
                selected_answer = request.POST.get(q.text)
                
                if selected_answer != "":
                    questions_answers = Answer.objects.filter(question=q)

                    for a in questions_answers:
                        if selected_answer == a.text:
                            if a.correct:
                                score += 1
                                correct_answer = a.text

                        else:
                            if a.correct:
                                correct_answer = a.text

                    results.append({str(q): {'correct': correct_answer, 'answered': selected_answer}})

                else:
                    results.append({str(q): 'not answered'})

        total_score = score * multiplier

        if total_score >= chapter.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': total_score, 'results': results})

        else:
            return JsonResponse({'passed': False, 'score': total_score, 'results': results})
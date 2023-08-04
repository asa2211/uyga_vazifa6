from .models import SubjectModel
from django.http import JsonResponse


def get_all(request):
    if request.method == 'GET':
        all_subjects = SubjectModel.objects.all()
        results = []
        for subject in all_subjects:
            results.append({
                'id': subject.id,
                'subject_name': subject.subject_name,
                'added_at': subject.added_at
            })
        return JsonResponse(data=results, safe=False)


def get_by_index(request, sub_id):
    if request.method == 'GET':
        try:
            data = SubjectModel.objects.get(id=sub_id)
        except SubjectModel.DoesNotExist:
            return JsonResponse({'MSG': 'question does not found'}, safe=False)
        return JsonResponse({
            'id': data.id,
            'subject_name': data.subject_name,
            'added_at': data.added_at
        }, safe=False)
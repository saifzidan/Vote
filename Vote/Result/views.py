from django.views import generic
from Worker.models import Question
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'Result/results.html'
class IndexView(generic.ListView):
    template_name = 'Result/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

from django.views.generic import ListView

from babel.moments.models import Moment


class MomentsListView(ListView):
    """
    View for listing all moments
    """

    queryset = Moment.objects.all()
    context_object_name = "moments"

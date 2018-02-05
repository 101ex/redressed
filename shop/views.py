from django.shortcuts import render

#decorators
from django.views.decorators.csrf import ensure_csrf_cookie

#exceptions
from django.core.exceptions import ObjectDoesNotExist
from django.http            import Http404

from .models import ApparelType, Apparel

@ensure_csrf_cookie
def sortiment(request, apparel, apparel_id=False):

    try:
        requested_apparel = ApparelType.objects.get(type=apparel)   #filter for non-sold objects
        requested_apparel_list = requested_apparel.apparel_set.all()

    except ObjectDoesNotExist:
        raise Http404("Requested Apparel Type Does Not Exist!")


    try:
        apparel_focus = Apparel.objects.get(id=apparel_id)

    except ObjectDoesNotExist:
        apparel_focus = False

    #all_apparel = Apparel.objects.all()

    context = {
        'requested_apparel':requested_apparel,
        'requested_apparel_list':requested_apparel_list,
        'apparel_focus':apparel_focus,
    }

    return render(request, 'shop/base_Sortiment.html', context)
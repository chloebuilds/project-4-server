from datetime import date, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#? from rest_framework.exceptions import NotFound

from ..models import WeeklyIntention
from ..serializers import WeeklyIntentionSerializer



#! WEEKLY VIEWS

#* Weekly Intentions
class WeeklyIntentionListView(APIView):
    #GET ALL INTENTIONS
    def get(self, _request, sprint_pk):
        all_intentions = WeeklyIntention.objects.all()
        serialized_intentions = WeeklyIntentionSerializer (all_intentions, many=True)
        return Response(serialized_intentions.data, status=status.HTTP_200_OK)
    #POST AN INTENTION
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data["end_date"] = date.today() + timedelta(days=6)
        serialized_intention = WeeklyIntentionSerializer(data=request.data)
        if serialized_intention.is_valid():
            serialized_intention.save()
            return Response(serialized_intention.data, status=status.HTTP_201_CREATED)
        return Response(serialized_intention.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class WeeklyIntentionDetailView(APIView):   
    #DELETE  AN INTENTION
    def delete(self, _request, sprint_pk, intention_pk):
        intention_to_delete = WeeklyIntention.objects.get(pk=intention_pk)
        intention_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE AN INTENTION
    def put(self, request, sprint_pk, intention_pk):
        intention_to_update = WeeklyIntention.objects.get(pk=intention_pk)
        request.data['sprint'] = sprint_pk
        request.data['owner'] = request.user.id
        request.data['end_date'] = WeeklyIntention.objects.get(pk=intention_pk).end_date
        updated_intention = WeeklyIntentionSerializer(intention_to_update, data=request.data)
        if updated_intention.is_valid():
            updated_intention.save()
            return Response(updated_intention.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_intention.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
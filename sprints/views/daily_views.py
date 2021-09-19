from datetime import date, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#? from rest_framework.exceptions import NotFound

from ..models import Sprint, DailyToDo,  DailyMood, DailyEnergy, DailyGratitude
from ..serializers import DailyToDoSerializer, DailyMoodSerializer,  DailyEnergySerializer, DailyGratitudeSerializer 

#! DAILY VIEWS

#* Daily To-Do 
class DailyToDoListView(APIView):  
    #GET ALL TO-DOs
    def get(self, _request, sprint_pk):
        all_to_dos = DailyToDo.objects.all()
        serialized_all_to_dos = DailyToDoSerializer(all_to_dos, many=True)
        return Response(serialized_all_to_dos.data, status=status.HTTP_200_OK)
    #POST A TO-DO 
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data['end_date'] = date.today() + timedelta(days=0)
        serialized_to_do = DailyToDoSerializer(data = request.data)
        if serialized_to_do.is_valid():
            serialized_to_do.save()
            return Response(serialized_to_do.data, status=status.HTTP_201_CREATED)
        return Response(serialized_to_do.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class DailyToDoDetailView(APIView):     
    #DELETE A TO-DO
    def delete(self, _request, sprint_pk, to_do_pk):
        # try:
        to_do_to_delete = DailyToDo.objects.get(pk=to_do_pk)
        to_do_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE A TO-DO
    def put(self, request, sprint_pk, to_do_pk):
        to_do_to_update = DailyToDo.objects.get(pk=to_do_pk)
        request.data['sprint'] = sprint_pk
        request.data['owner'] = request.user.id
        request.data['end_date'] = DailyToDo.objects.get(pk=to_do_pk).end_date
        updated_to_do = DailyToDoSerializer(to_do_to_update, data=request.data)
        if updated_to_do.is_valid():
            updated_to_do.save()
            return Response(updated_to_do.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_to_do.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#* Daily Mood
class DailyMoodListView(APIView):
    #GET ALL MOODS
    def get(self, _request, sprint_pk):
        sprint = Sprint.objects.get(pk=sprint_pk)
        serialized_moods = DailyMoodSerializer(sprint.moods, many=True)
        return Response(serialized_moods.data, status=status.HTTP_200_OK)
    #POST A MOOD
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data['end_date'] = date.today() + timedelta(days=0)
        serialized_mood = DailyMoodSerializer(data=request.data)
        if serialized_mood.is_valid():
            serialized_mood.save()
            return Response(serialized_mood.data, status=status.HTTP_201_CREATED)
        return Response(serialized_mood.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class DailyMoodDetailView(APIView): 
    #DELETE A MOOD
    def delete(self, _request, sprint_pk, mood_pk):
        mood_to_delete = DailyMood.objects.get(pk=mood_pk)
        mood_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#* Daily Energy Level
class DailyEnergyListView(APIView):
    #GET ALL ENERGY LEVELS
    def get(self, _request, sprint_pk):
        all_energy_levels = DailyEnergy.objects.all()
        serialized_energy_levels = DailyEnergySerializer(all_energy_levels, many=True)
        return Response(serialized_energy_levels.data, status=status.HTTP_200_OK)
    #POST AN ENERGY LEVEL
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data['end_date'] = date.today() + timedelta(days=0)
        serialized_energy = DailyEnergySerializer(data=request.data)
        if serialized_energy.is_valid():
            serialized_energy.save()
            return Response(serialized_energy.data, status=status.HTTP_201_CREATED)
        return Response(serialized_energy.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
class DailyEnergyDetailView(APIView):
    #DELETE ENERGY LEVEL
    def delete(self, _request, sprint_pk, energy_level_pk):
        energy_level_to_delete = DailyEnergy.objects.get(pk=energy_level_pk)
        energy_level_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    #UPDATE ENERGY LEVEL
    def put(self, request, sprint_pk, energy_level_pk):
        energy_level_to_update = DailyEnergy.objects.get(pk=energy_level_pk)
        request.data['sprint'] = sprint_pk
        request.data['owner'] = request.user.id
        request.data['end_date'] = DailyEnergy.objects.get(pk=energy_level_pk).end_date
        updated_energy_level = DailyEnergySerializer(energy_level_to_update, data=request.data)
        if updated_energy_level.is_valid():
            updated_energy_level.save()
            return Response(updated_energy_level.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_energy_level.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#* Daily Gratitude
class DailyGratitudeListView(APIView):

    #GET ALL GRATITUDES
    def get(self, _request, sprint_pk):
        sprint = Sprint.objects.get(pk=sprint_pk)
        serialized_gratitudes = DailyGratitudeSerializer (sprint.daily_gratitudes, many=True)
        return Response(serialized_gratitudes.data, status=status.HTTP_200_OK)

    #POST GRATITUDE 
    def post(self, request, sprint_pk):
        request.data['sprint'] = sprint_pk
        request.data['end_date'] = date.today() + timedelta(days=0)
        serialized_gratitude = DailyGratitudeSerializer(data=request.data)
        if serialized_gratitude.is_valid():
            serialized_gratitude.save()
            return Response(serialized_gratitude.data, status=status.HTTP_201_CREATED)
        return Response(serialized_gratitude.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class DailyGratitudeDetailView(APIView):

    #DELETE GRATITUDE 
    def delete(self, _request, sprint_pk, gratitude_pk):
        gratitude_to_delete = DailyGratitude.objects.get(pk=gratitude_pk)
        gratitude_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #UPDATE GRATITUDE 
    def put(self, request, sprint_pk, gratitude_pk):
        gratitude_to_update = DailyGratitude.objects.get(pk=gratitude_pk)
        request.data['sprint'] = sprint_pk
        request.data['owner'] = request.user.id
        request.data['end_date'] = DailyGratitude.objects.get(pk=gratitude_pk).end_date
        updated_gratitude = DailyGratitudeSerializer(gratitude_to_update, data=request.data)
        if updated_gratitude.is_valid():
            updated_gratitude.save()
            return Response(updated_gratitude.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_gratitude.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

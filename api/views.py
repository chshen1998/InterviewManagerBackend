from django.shortcuts import render
from rest_framework import generics, status
from .models import Application
from .serializers import ApplicationSerializer, AddApplicationSerializer, UpdateApplicationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class ApplicationView(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class GetApplicationsView(APIView):
    def get(self, request):
        # user = self.request.session.session_key
        # queryset = Application.objects.filter(user=user)
        queryset = Application.objects.all()
        data = ApplicationSerializer(queryset, many=True).data
        return Response(data, status=status.HTTP_200_OK)


class AddApplicationView(APIView):
    def post(self, request):
        # if not self.request.session.exists(self.request.session.session_key):
        #    self.request.session.create()

        serializer = AddApplicationSerializer(data=request.data)
        if serializer.is_valid():
            # user = self.request.session.session_key
            user = serializer.data.get('user')
            title = serializer.data.get('title')
            company = serializer.data.get('company')
            resume = serializer.data.get('resume')
            application = Application(user=user, title=title, company=company, resume=resume)
            application.save()
            return Response(ApplicationSerializer(application).data, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Application failed to create'}, status=status.HTTP_400_BAD_REQUEST)


class DeleteApplicationView(APIView):
    lookup_url_kwarg = 'id'

    def delete(self, request):
        application_id = request.GET.get(self.lookup_url_kwarg)
        application = Application.objects.get(id=application_id)
        application.delete()
        return Response({'Success': 'Application has been deleted'}, status=status.HTTP_200_OK)


class UpdateApplicationView(APIView):
    lookup_url_kwarg = 'id'

    def post(self, request):
        serializer = UpdateApplicationSerializer(data=request.data)
        if serializer.is_valid():
            application_id = request.GET.get(self.lookup_url_kwarg)
            title = serializer.data.get('title')
            company = serializer.data.get('company')
            resume = serializer.data.get('resume')
            interview = serializer.data.get('interview')
            date = serializer.data.get('date')
            result = serializer.data.get('result')
            application = Application.objects.get(id=application_id)
            application.title = title
            application.company = company
            application.resume = resume
            application.interview = interview
            application.date = date
            application.result = result
            application.save(update_fields=['title', 'company', 'resume', 'interview', 'date', 'result'])
            return Response(ApplicationSerializer(application).data, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Application failed to update'}, status=status.HTTP_400_BAD_REQUEST)






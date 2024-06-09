from rest_framework import generics

from .models import Amount
from .serializers import AmountSerializer


class AmountListAPIView(generics.ListAPIView):
    serializer_class = AmountSerializer
    queryset = Amount.objects.all()


class AmountCreateAPIView(generics.CreateAPIView):
    serializer_class = AmountSerializer

    def perform_create(self, serializer):
        amount = serializer.save()
        amount.session_id = 'session_id_11'
        amount.link = 'link_1234124'
        amount.save()


class AmountUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AmountSerializer
    queryset = Amount.objects.all()


class AmountRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AmountSerializer
    queryset = Amount.objects.all()


class AmountDestroyAPIView(generics.DestroyAPIView):
    serializer_class = AmountSerializer
    queryset = Amount.objects.all()

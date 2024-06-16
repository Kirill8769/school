from django.views.generic import TemplateView
from rest_framework import generics

from .models import Amount
from .serializers import AmountSerializer
from .services import create_stripe_price, create_stripe_session


class AmountListAPIView(generics.ListAPIView):
    serializer_class = AmountSerializer
    queryset = Amount.objects.all()


class AmountCreateAPIView(generics.CreateAPIView):
    serializer_class = AmountSerializer

    def perform_create(self, serializer):
        amount = serializer.save()
        price = create_stripe_price(amount=amount.amount, course=amount.course)
        session = create_stripe_session(price=price)
        amount.session_id = session.get('id')
        amount.link = session.get('url')
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


class SuccessTemplateView(TemplateView):
    template_name = 'amount/success.html'

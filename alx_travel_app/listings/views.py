from django.shortcuts import render
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Listing, Booking
from .models import Payment
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class InitiatePaymentView(APIView):
    def post(self, request):
        booking_ref = request.data.get('booking_reference')
        amount = request.data.get('amount')
        email = request.data.get('email')

        chapa_url = 'https://api.chapa.co/v1/transaction/initialize'
        headers = {
            'Authorization': f'Bearer {settings.CHAPA_SECRET_KEY}',
            'Content-Type': 'application/json'
        }
        payload = {
            "amount": amount,
            "currency": "ETB",
            "email": email,
            "tx_ref": booking_ref,
            "callback_url": "http://yourdomain.com/api/verify-payment/",
            "return_url": "http://yourdomain.com/payment-complete/"
        }

        response = requests.post(chapa_url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json().get('data')
            Payment.objects.create(
                booking_reference=booking_ref,
                amount=amount,
                transaction_id=data['tx_ref'],
                status="Pending"
            )
            return Response({"payment_url": data['checkout_url']}, status=200)

        return Response({"error": "Failed to initiate payment"}, status=500)


class VerifyPaymentView(APIView):
    """An endpoint in the API to verify the payment status
    with Chapa after a user completes a payment"""
    def get(self, request):
        tx_ref = request.query_params.get('tx_ref')

        verify_url = f"https://api.chapa.co/v1/transaction/verify/{tx_ref}"
        headers = {
            'Authorization': f'Bearer {settings.CHAPA_SECRET_KEY}',
        }

        response = requests.get(verify_url, headers=headers)

        if response.status_code == 200:
            data = response.json().get('data')
            status_text = data.get('status')

            payment = Payment.objects.filter(transaction_id=tx_ref).first()
            if payment:
                if status_text == "success":
                    payment.status = "Completed"
                    # Trigger email via Celery here
                else:
                    payment.status = "Failed"
                payment.save()

            return Response({"status": payment.status}, status=200)

        return Response({"error": "Payment verification failed"}, status=500)

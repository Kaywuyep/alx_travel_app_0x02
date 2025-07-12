from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_payment_confirmation_email(email, booking_ref):
    subject = 'Payment Confirmation'
    message = f"Your payment for booking {booking_ref} was successful!"
    send_mail(subject, message, 'no-reply@yourdomain.com', [email])

    
@shared_task
def send_booking_email(recipient_email, booking_id):
    subject = 'Booking Confirmation'
    message = f'Your booking with ID {booking_id} has been confirmed.'
    from_email = 'no-reply@alxtravel.com'

    send_mail(subject, message, from_email, [recipient_email])
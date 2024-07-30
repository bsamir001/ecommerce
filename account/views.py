from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, OTPCode
from .utils import send_sms
import random
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class SendCodeView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            return Response({"error": "phone number is required"}, status=status.HTTP_400_BAD_REQUEST)
        otp_code, created = OTPCode.objects.get_or_create(phone_number=phone_number)
        code = str(random.randint(10000, 99999))
        otp_code.code = code
        otp_code.save()
        send_sms(phone_number=phone_number, code=code)
        return Response({'message': 'code sent'}, status=status.HTTP_200_OK)


# {"phone_number": "09145212032", "code": '52125"}


class RegisterView(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        code = request.data.get("code")
        if not phone_number:
            return Response({"error": "phone number is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not code:
            return Response({"error": "code is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            otp_code = OTPCode.objects.get(phone_number=phone_number, code=code)
            if not otp_code:
                return Response({"error": "otp code is not valid"})
            user, created = User.objects.get_or_create(phone_number=phone_number)
            otp_code.delete()
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
        except OTPCode.DoesNotExist:
            return Response({"error": "otp code does not exist"}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.models import User
from accounts.serializers.verifyAccount import VerifyAccountSerializer


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'status': status.HTTP_422_UNPROCESSABLE_ENTITY,
                    'message': 'Invalid data',
                    'data': serializer.errors
                })

            email = serializer.data['email']
            otp = serializer.data['otp']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({
                    'status': status.HTTP_422_UNPROCESSABLE_ENTITY,
                    'message': 'Invalid email',
                    'data': {}
                })

            if user.otp != otp:
                return Response({
                    'status': status.HTTP_422_UNPROCESSABLE_ENTITY,
                    'message': 'Wrong OTP',
                    'data': {}
                })

            user.is_verified = True
            user.save()

            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Account verified',
                'data': {}
            })

        except Exception as e:
            print(e)

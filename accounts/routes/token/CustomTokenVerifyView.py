from rest_framework_simplejwt.views import TokenVerifyView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = request.data.get('token')

        if token:
            try:
                decoded_token = AccessToken(token)
                user_id = decoded_token['user_id']
                User = get_user_model()
                user = User.objects.get(id=user_id)
                user_info = {
                    # 'id': str(user.id),
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'user_type': user.user_type,
                }
                response.data['user'] = user_info
            except Exception as e:
                pass

        return response

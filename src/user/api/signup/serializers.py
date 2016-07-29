from django.utils.translation import ugettext_lazy as _
from requests.exceptions import HTTPError

from rest_framework import serializers

from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.providers.facebook.views import fb_complete_login
from allauth.socialaccount.models import SocialAccount, SocialLogin, SocialToken, SocialApp


class SignupFacebookSerializer(serializers.Serializer):
    email = serializers.CharField(style={'input_type': 'email'})
    fcb_id = serializers.CharField(style={'input_type': 'password'})
    fcb_token = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        request = self.context.get('request')

        assert request is not None, \
            'Must provide "request" in a "context" dict when instantiating the serializer.'

        try:
            account = SocialAccount.objects.get(user__email__iexact=attrs.get('email'))
        except SocialAccount.DoesNotExist:
            app = SocialApp.objects.get(provider='facebook')
            social_token = SocialToken(app=app, token=attrs.get('fcb_token'))

            try:
                # Check token against Facebook
                original_request = request._request
                login = fb_complete_login(original_request, app, social_token)
                login.token = social_token
                login.state = SocialLogin.state_from_request(original_request)
                complete_social_login(original_request, login)
                account = login.account
            except HTTPError:
                # 400 Client Error
                raise serializers.ValidationError(
                    _('Facebook authentication failed.')
                )

        if account.uid != attrs.get('fcb_id'):
            msg = _('Facebook ID does not match.')
            raise serializers.ValidationError(msg)

        if not account.user.is_active:
            raise serializers.ValidationError(
                _('User account is disabled.')
            )

        attrs['user'] = account.user

        return attrs

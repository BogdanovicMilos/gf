from allauth.account.forms import SignupForm
from teams.models.team import Team
from django import forms


class CustomSignupForm(SignupForm):
    team_name = forms.CharField(max_length=63)

    def save(self, request):
        self.team = Team.objects.create(name=self.cleaned_data["team_name"])  # pylint: disable=W0201
        user = super().save(request)
        return user

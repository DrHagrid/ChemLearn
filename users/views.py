from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import UserInfo


def distribution(request):
    if not request.user.is_anonymous:
        user_info, created = UserInfo.objects.get_or_create(user=request.user, defaults={'last_reaction': 1})
        last_reaction = user_info.last_reaction
    return render(request, 'start_page.html', locals())


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "../../accounts/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "registration/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

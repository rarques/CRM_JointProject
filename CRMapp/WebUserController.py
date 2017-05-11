from CRMapp.models import Category, CategoryPerUser


class WebUserController:

    def __init__(self, request):
        self.request = request
        self.parameters = self.get_profile_parameters()

    def get_profile_parameters(self):
        parameters = {}
        self.get_basic_parameters(parameters)
        self.get_user_parameters(parameters)
        self.get_category_parameters(parameters)

        return parameters


    def get_basic_parameters(self, parameters):
        """
        Captures the parameters associated with the Django user model
        :param parameters: The dictionary where the parameters will be stored
        """
        # basic fields
        parameters['username'] = self.request.get('username')
        parameters['email'] = self.request.get('email')

    def get_user_parameters(self, parameters):
        """
        Captures the parameters associated with the WebUser model
        :param parameters: The dictionary where the parameters will be stored
        """
        # user information
        parameters['country'] = self.request.get('country')
        parameters['province'] = self.request.get('province')
        parameters['city'] = self.request.get('city')
        parameters['zip_code'] = self.request.get('zip_code')
        parameters['street'] = self.request.get('street')
        parameters['phone'] = self.request.get('phone')

    def get_category_parameters(self, parameters):
        parameters['categories'] = self.request.getlist('category')

    def update_basic_parameters(self, parameters, user):
        """
        Updates the parameters associated with the Django user model
        :param parameters: Dictionary that contains all the parameters
        :param user: Django user model
        """
        user.username = parameters['username']
        user.email = parameters['email']

    def update_user_parameters(self, parameters, web_user):
        """
        Updates the parameters associated with the WebUser model
        :param parameters: Dictionary that contains all the parameters
        :param web_user: WebUser model
        """
        web_user.country = parameters['country']
        web_user.province = parameters['province']
        web_user.city = parameters['city']
        web_user.zip_code = parameters['zip_code']
        web_user.street = parameters['street']
        web_user.phone = parameters['phone']

    def update_category_parameters(self, parameters, web_user):
        for cat in parameters['categories']:
            category = Category.objects.get(name=cat)
            CategoryPerUser.objects.create(user=web_user, category=category)

    def create_new_django_user(self, user_form):
        form_data = user_form.cleaned_data
        new_user = user_form.save(commit=False)
        new_user.set_password(form_data['password'])
        new_user.save()
        return new_user

    def create_new_web_user(self, web_user_form, django_user):
        new_web_user = web_user_form.save(commit=False)
        new_web_user.django_user = django_user
        new_web_user.save()
        return new_web_user

    def register_interested_categories(self, new_web_user, interested_categories):
        for cat in interested_categories:
            category = Category.objects.get(name=cat)
            CategoryPerUser.objects.create(user=new_web_user, category=category)

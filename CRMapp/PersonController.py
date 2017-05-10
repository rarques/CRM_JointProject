from CRMapp.WebUserController import WebUserController


class PersonController(WebUserController):
    def get_person_profile_parameters(self, request):
        """
        Capture the parameters of the person type user profile
        :param request: HttpRequest
        :return: A dictionary with parameters
        """
        parameters = {}
        self.get_basic_parameters(parameters, request)
        self.get_user_parameters(parameters, request)
        self.get_category_parameters(parameters, request)
        self.get_person_parameters(parameters, request)
        return parameters

    def get_person_parameters(self, parameters, request):
        """
        Captures the parameters associated with the UserAsPerson model
        :param parameters: The dictionary where the parameters will be stored
        :param request: HttpRequest
        """
        # company information
        parameters['dni'] = request['dni']

    def update_person_profile(self, parameters, user, web_user, user_as_person):
        """
        Update user profile of person type
        :param parameters: Dictionary that contains all the parameters
        :param user: Django user model
        :param web_user: WebUser model
        :param user_as_person: user_as_company: UserAsPerson model
        """
        self.update_basic_parameters(parameters, user)
        self.update_user_parameters(parameters, web_user)
        self.update_category_parameters(parameters, web_user)
        self.update_person_parameters(parameters, user_as_person)
        user.save(update_fields=["username", "email"])
        web_user.save(update_fields=["country", "province", "city", "zip_code",
                                     "street", "phone"])
        user_as_person.save(update_fields=["DNI"])

    def update_person_parameters(self, parameters, user_as_person):
        """
        Updates the parameters associated with the UserAsPerson model
        :param parameters: Dictionary that contains all the parameters
        :param user_as_person: UserAsPerson model
        """
        user_as_person.DNI = parameters['dni']

    def create_new_user_as_person(self, user_as_person_form, web_user):
        new_person_user = user_as_person_form.save(commit=False)
        new_person_user.web_user = web_user
        new_person_user.save()

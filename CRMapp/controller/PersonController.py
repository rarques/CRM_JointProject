from CRMapp.controller.WebUserController import WebUserController


class PersonController(WebUserController):
    def __init__(self, request):
        WebUserController.__init__(self, request)
        self.get_person_parameters()

    def get_person_parameters(self):
        """
        Captures the parameters associated with the UserAsPerson model
        """
        # company information
        self.parameters['dni'] = self.request.get('dni')

    def update_person_profile(self, user, web_user, user_as_person):
        """
        Update user profile of person type
        :param user: Django user model
        :param web_user: WebUser model
        :param user_as_person: user_as_company: UserAsPerson model
        """
        self.update_basic_parameters(self.parameters, user)
        self.update_user_parameters(self.parameters, web_user)
        self.update_category_parameters(self.parameters, web_user)
        self.update_person_parameters(user_as_person)
        user.save(update_fields=["username", "email"])
        web_user.save(update_fields=["country", "province", "city", "zip_code",
                                     "street", "phone"])
        user_as_person.save(update_fields=["DNI"])

    def update_person_parameters(self, user_as_person):
        """
        Updates the parameters associated with the UserAsPerson model
        :param user_as_person: UserAsPerson model
        """
        user_as_person.DNI = self.parameters['dni']

    def create_new_user_as_person(self, user_as_person_form, web_user):
        new_person_user = user_as_person_form.save(commit=False)
        new_person_user.web_user = web_user
        new_person_user.save()

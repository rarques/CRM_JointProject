from CRMapp.WebUserController import WebUserController


class CompanyController(WebUserController):

    def __init__(self, request):
        WebUserController.__init__(self, request)
        self.parameters = self.get_company_profile_parameters()

    def get_company_profile_parameters(self):
        """
        Capture the parameters of the company type user profile
        :return: A dictionary with parameters
        """
        parameters = {}
        self.get_basic_parameters(parameters)
        self.get_user_parameters(parameters)
        self.get_category_parameters(parameters)
        self.get_company_parameters(parameters)
        return parameters

    def get_company_parameters(self, parameters):
        """
        Captures the parameters associated with the UserAsCompany model
        """
        # company information
        parameters['cif'] = self.request.get('cif')

    def update_company_profile(self, user, web_user, user_as_company):
        """
        Update user profile of company type
        :param user: Django user model
        :param web_user: WebUser model
        :param user_as_company: UserAsCompany model
        """
        self.update_basic_parameters(self.parameters, user)
        self.update_user_parameters(self.parameters, web_user)
        self.update_category_parameters(self.parameters, web_user)
        self.update_company_parameters(user_as_company)
        user.save(update_fields=["username", "email"])
        web_user.save(update_fields=["country", "province", "city", "zip_code",
                                     "street", "phone"])
        user_as_company.save(update_fields=["CIF"])

    def update_company_parameters(self, user_as_company):
        """
        Updates the parameters associated with the UserAsCompany model
        :param user_as_company: UserAsCompany model
        """
        user_as_company.CIF = self.parameters['cif']

    def create_new_company_user(self, user_as_company_form, web_user):
        new_company_user = user_as_company_form.save(commit=False)
        new_company_user.web_user = web_user
        new_company_user.save()

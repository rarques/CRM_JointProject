from CRMapp.User import get_basic_parameters, get_user_parameters, get_category_parameters, update_basic_parameters, \
    update_user_parameters, update_category_parameters


def get_person_profile_parameters(source, user, web_user, user_as_person):
    """
    Capture the parameters of the person type user profile
    :param request: HttpRequest
    :return: A dictionary with parameters
    """
    parameters = {}
    get_basic_parameters(parameters, source)
    get_user_parameters(parameters, source)
    get_category_parameters(parameters, source)
    get_person_parameters(parameters, source)
    return parameters


def get_person_parameters(parameters, source):
    """
    Captures the parameters associated with the UserAsPerson model
    :param parameters: The dictionary where the parameters will be stored
    :param request: HttpRequest
    """
    # company information
    parameters['dni'] = source['dni']


def update_person_profile(parameters, user, web_user, user_as_person):
    """
    Update user profile of person type
    :param parameters: Dictionary that contains all the parameters
    :param user: Django user model
    :param web_user: WebUser model
    :param user_as_person: user_as_company: UserAsPerson model
    """
    update_basic_parameters(parameters, user)
    update_user_parameters(parameters, web_user)
    update_category_parameters(parameters, web_user)
    update_person_parameters(parameters, user_as_person)
    user.save(update_fields=["username", "email"])
    web_user.save(update_fields=["country", "province", "city", "zip_code",
                                 "street", "phone"])
    user_as_person.save(update_fields=["DNI"])


def update_person_parameters(parameters, user_as_person):
    """
    Updates the parameters associated with the UserAsPerson model
    :param parameters: Dictionary that contains all the parameters
    :param user_as_person: UserAsPerson model
    """
    user_as_person.DNI = parameters['dni']


def create_new_user_as_person(user_as_person_form, web_user):
    new_person_user = user_as_person_form.save(commit=False)
    new_person_user.web_user = web_user
    new_person_user.save()
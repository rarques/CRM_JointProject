# CRM_JointProject

[![CircleCI](https://circleci.com/gh/rarques/CRM_JointProject.svg?style=shield&circle-token=00cf40956a6570f716325c99c83eef1978c2ad35	)](https://circleci.com/gh/rarques/CRM_JointProject)

The goal of this project is to create a CRM (Customer Relationship Management) for TECNOGAD.
TECNOGAD is a company focused on selling technological products and gadgets.

## Getting Started

Fork and/or clone the repository into your local machine.

### Prerequisites

In order to work with the project you will need the following:

* python 2.7.12
* virtualenv

Installing and activating virtualenv:

```
sudo apt-get install python-virtualenv
sudo easy_install virtualenv
sudo pip install virtualenv
virtualenv <env-folder>/<env-name>
source <env-folder>/bin/activate
```

### Installing

Install the python dependencies. They are located in the [requirements.txt] (requirements.txt) file.
How to install:

```
pip install -r requirements.txt
```

## Running the tests

Give execution permission to the file [django_testing_script.sh] and execute it.
It will automatically apply the necessary migrations on the database and run the tests.

## Deployment

https://technogad-crm.herokuapp.com

## Built With

* [Django 1.10.5](https://www.djangoproject.com) - The web framework used

## Authors

* **Roger Arqués Vall**
* **Manel Dueñas Triguero**
* **Marc Ribalta Gené**
* **Cindy Clauwers**
* **Pol Torres Alfonso**
* **Adrià Navarro Bosqué**

## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details

# SnapFood API in DRF

**Developer: Aleksandra Haniok**

💻 [Live link](http://snapfood-drf-api.herokuapp.com/)

This repository contains the API set up using Django REST Framework for the SnapFood front-end application ([repository here](https://github.com/aleksandracodes/CI_PP5_Snapfood) and [live website here](https://ci-pp5-snapfood.herokuapp.com/))

## Table of Contents
  - [User Stories](#user-stories)
  - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Validation](#validation)

## User Stories

The back-end section of the project focuses on its administration side and covers one user story:
- As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over the content of the application and remove any potential inappropriate content

##### Back to [top](#table-of-contents)


## Database

<img src="docs/readme/database-diagram.png">

The following models were created to represent the database model structure of the application:

#### User Model

#### Profile Model

#### Post Model

#### Follower Model

#### Comment Model

#### Like Model


##### Back to [top](#table-of-contents)


## Technologies Used

### Languages & Frameworks

- Python
- Django

### Libraries & Tools

- [Cloudinary](https://cloudinary.com/) to store static files and serve them to Heroku
- [Dbdiagram.io](https://dbdiagram.io/home) used for the database schema diagram
- [Git](https://git-scm.com/) was used for version control via Gitpod terminal to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Gitpod)](https://gitpod.io/workspaces) - a virtual IDE workspace used to build this site
- [Heroku Platform](https://id.heroku.com/login) was used to deploy the project into live environment
- [Django REST Framework](https://www.django-rest-framework.org/) was used to build the back-end API
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) was used for user authentication
- [Gunicorn](https://gunicorn.org/) was used for deploying the project to Heroku
- [Pillow](https://pillow.readthedocs.io/en/stable/) was used for image processing and validation
- [Psycopg2](https://www.psycopg.org/docs/) was used as a PostgreSQL database adapter for Python
- [Postgres](https://www.postgresql.org/) – deployed project on Heroku uses a Postres database


## Validation

### PEP8 Validation
[PEP8](http://pep8online.com/) Validation Service was used to check the code for PEP8 requirements. All the code passes with no errors or warnings.

##### Back to [top](#table-of-contents)

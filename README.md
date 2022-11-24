# SnapFood API in DRF

**Developer: Aleksandra Haniok**

💻 [Live link](https://snapfood-drf-api.onrender.com/)

This repository contains the API set up using Django REST Framework for the SnapFood front-end application ([repository here](https://github.com/aleksandracodes/CI_PP5_Snapfood) and [live website here](https://ci-pp5-snapfood.onrender.com))

## Table of Contents
  - [User Stories](#user-stories)
  - [Database](#database)
  - [Technologies Used](#technologies-used)
  - [Validation](#validation)
  - [Testing](#testing)
  - [Credits](#credits)

## User Stories

The back-end section of the project focuses on its administration side and covers one user story:
- As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over the content of the application and remove any potential inappropriate content


## Database

The following models were created to represent the database model structure of the application:
<img src="docs/readme/snapfood-database-diagram.png">

#### User Model

- The User model contains information about the user. It is part of the Django allauth library.
- One-to-one relation with the Profile model owner field
- ForeignKey relation with the Follower model owner and followed fields
- ForeignKey relation with the Post model owner field
- ForeignKey relation with the Comment model owner field
- ForeignKey relation with the Like model owner field

#### Profile Model

- The Profile model contains the following fields: owner, name, description, created_on, updated_on and image
- One-to-one relation between the owner field and the User model id field

#### Post Model

- The Post model contains the following fields: owner, created_on, updated_on, title, description, category and image
- ForeignKey relation with the Comment model post field
- ForeignKey relation with the Like model post field

#### Follower Model

- The Follower model contains the following fields: owner, followed and created_on
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the followed field and the User model post field

#### Comment Model

- The Comment model contains the following fields: owner, post, created_on, updated_on and content
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the post field and the User model post field

#### Like Model

- The Like model contains the following fields: owner, post and created_on
- ForeignKey relation between to the User model id field
- ForeignKey relation between the owner field and the User model id field
- ForeignKey relation between the post field and the Post model post field

##### Back to [top](#table-of-contents)


## Technologies Used

### Languages & Frameworks

- Python
- Django

### Libraries & Tools

- [APITestCase](https://www.django-rest-framework.org/api-guide/testing/) - Django Rest Framework APITestCase was used for automated testing
- [Cloudinary](https://cloudinary.com/) to store static files
- [Coverage](https://coverage.readthedocs.io/en/6.4.4/) used to produce automated testing report
- [Dbdiagram.io](https://dbdiagram.io/home) used for the database schema diagram
- [Git](https://git-scm.com/) was used for version control via Gitpod terminal to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Gitpod)](https://gitpod.io/workspaces) - a virtual IDE workspace used to build this site
- [Render Platform](https://render.com) was used to deploy the project into live environment
- [Django REST Framework](https://www.django-rest-framework.org/) was used to build the back-end API
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) was used for user authentication
- [Pillow](https://pillow.readthedocs.io/en/stable/) was used for image processing and validation
- [Psycopg2](https://www.psycopg.org/docs/) was used as a PostgreSQL database adapter for Python
- [PostgreSQL](https://www.postgresql.org/) – deployed project on Render uses a PostgreSQL database

##### Back to [top](#table-of-contents)


## Validation

### PEP8 Validation
[PEP8](http://pep8online.com/) Validation Service was used to check the code for PEP8 requirements. All the code passes with no errors or warnings.


## Testing

The following tests were carried out on the app:
1. Manual testing of user stories
2. Automated testing

### Manual testing of user stories

- As an admin, I want to be able to create, edit and delete the users, posts, comments and likes, so that I can have a control over the content of the application and remove any potential inappropriate content

**Test** | **Action** | **Expected Result** | **Actual Result**
-------- | ------------------- | ------------------- | -----------------
User | Create, update & delete user | A user can be created, edited or deleted | Works as expected
User | Change permissions | User permissions can be updated | Works as expected
Profile | Create, update & delete | User profile can be created, edited or deleted | Works as expected
Post | Create, update & delete | A post can be created, edited or deleted | Works as expected
Comment | Create, update & delete | A comment can be created, edited or deleted | Works as expected
Like | Create & delete | A like can be created or deleted (like / unlike post) | Works as expected
Follower | Create & delete | Follow or unfollow user | Works as expected

In addition, posts, comments, likes and following can be created by logged-in users only. Users can only update or delete the content which was created by themselves.

<details><summary>Screenshots - USER</summary>
    <details><summary>Create user</summary>
    <img src="docs/testing/user-create-test.png">
    </details>
    <details><summary>Change user permissions</summary>
    <img src="docs/testing/user-change-permissions-test.png">
    </details>
</details>

<details><summary>Screenshots - PROFILE</summary>
    <details><summary>Update profile</summary>
    <img src="docs/testing/profile-update-test.png">
    </details>
        <details><summary>Delete profile</summary>
    <img src="docs/testing/profile-delete-test.png">
    </details>
</details>

<details><summary>Screenshots - POST</summary>
    <details><summary>Create post</summary>
    <img src="docs/testing/post-create-test.png">
    </details>
    <details><summary>Update post</summary>
    <img src="docs/testing/post-update-test.png">
    </details>
    <details><summary>Delete post</summary>
    <img src="docs/testing/post-delete-test.png">
    </details>
</details>

<details><summary>Screenshots - COMMENT</summary>
    <details><summary>Create comment</summary>
    <img src="docs/testing/comment-create-test.png">
    </details>
    <details><summary>Update comment</summary>
    <img src="docs/testing/comment-update-test.png">
    </details>
    <details><summary>Delete comment</summary>
    <img src="docs/testing/comment-delete-test.png">
    </details>
</details>

<details><summary>Screenshots - LIKE</summary>
    <details><summary>Create like - like post</summary>
    <img src="docs/testing/like-create-test.png">
    </details>
    <details><summary>Delete like - unlike post</summary>
    <img src="docs/testing/like-delete-test.png">
    </details>
</details>

<details><summary>Screenshots - FOLLOWER</summary>
    <details><summary>Create - Follow user</summary>
    <img src="docs/testing/follower-create-test.png">
    </details>
    <details><summary>Delete - Unfollow user</summary>
    <img src="docs/testing/follower-delete-test.png">
    </details>
</details>


### Automated testing

Automated testing was done using the Django Rest Framework APITestCase (a very similar to Django's TestCase). The report of overall testing was produced using the coverage tool (```$ coverage report``` & ```$ coverage html``` commands)

- Tests summary

<img src="docs/testing/apitestcase-snapfood.png">

<details><summary>Detailed coverage report</summary>
<img src="docs/testing/coverage-report-snapfood.jpg">
</details>

##### Back to [top](#table-of-contents)


## Credits

### Images

- User avatar default image taken from [here](https://community.atlassian.com/t5/Jira-questions/JIRA-Anonymous-users-can-t-see-user-avatars/qaq-p/1060103) and colors changed using Paint
- Default post image found [here](https://www.fiverr.com/logo-maker/brief/logo_name?brief_id=0d212c49-2416-401d-99a5-780b9b233ff7) and tweaked with Paint

### Code

This project was created based on the Code Institute's Django REST API walkthrough project ['Moments'](https://github.com/Code-Institute-Solutions/drf-api) which was a great learning experience.

##### Back to [top](#table-of-contents)

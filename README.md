# SaborAsturiano

SaborAsturiano (AsturianTastes) is a website dedicated to Asturian cuisine, offering a mix of traditional and modern recipes. The project exists to celebrate and preserve the culinary heritage of Asturias, promoting local ingredients and seasonal content.

It caters to a community of Asturian food enthusiasts, providing a platform for exploration, reviews, and contributions. The website's purpose is to bring together individuals passionate about Asturian flavors, fostering a sense of community and sharing among those interested in the region's diverse culinary traditions.

![Am I Responsive?](/static/images/readme/responsive.jpg)

## Table of Contents

### [User Experience](#user-experience-ux)

- [Agile Methodology](#agile-methodology)
- [User Stories](#user-stories)
- [Target Audience](#target-audience)
- [First Time User](#first-time-user)
- [Registered User](#registered-user)
- [Admin User](#admin-user)

### [Design](#design)

- [Color Scheme](#color-scheme)
- [Typography](#typography)
- [Data Models](#data-models)

  - [Django Allauth](#django-allauth)
  - [Recipe](#recipe)
  - [Review](#review)
  - [UserProfile](#userprofile)

### [Features](#features)

- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)

### [Testing](#testing)

- [General Testing](#general-testing)
- [General Testing](#general-testing)
- [Lighthouse](#lighthouse)
- [Code Validation](#code-validation)
- [Features Testing](#features-testing)

  - [HTML](#html)
  - [CSS](#css)
  - [Python](#python)
  - [JavaScript](#javascript)

### [Deployment](#deployment)

- [Fork](#fork)
- [Clone](#clone)
- [Heroku](#heroku)
- [Environment Variables](#environment-variables)

### [Techologies Used](#techologies-used)

- [Languages](#languages)
- [Databases](#databases)
- [Programs](#programs)
- [Frameworks](#frameworks)

### [Credits](#credits)

- [Content](#content)
- [Media](#media)

## User Experience (UX)

SaborAsturiano prioritizes a seamless and enjoyable user experience to ensure that exploring Asturian cuisine is a delightful journey for all users. The user interface is designed to be intuitive and visually appealing, making navigation through recipes effortless. Clear and concise menus guide users to easily discover traditional recipes while interactive features sucs and user-contributed content enhance the community enagement.

A responsive design has been implemented to optimize the platform for various devices to ensure users experience the same seamless interaction whether accessing SaborAsturiano from their desktops, tablets or mobile phones.

### Goals

SaborAsturiano is commited to building an inviting online platoorm for Asturian food enthusiasts with a focus on the folloiing:

- Curate a diverse collection of traditional and modern Asturian recipes to celebrate and preserve the rich culinary heritage of the region.
- Foster a sense of community where members can view, review and like recipes by fellow enthusiasts.

### Agile Methodology

- The development process was carried out using an Agile methodology with a focus on iterative development and continuous improvement.
- The project was managed using a GitHub Project board with user stories and tasks.
- User Stories were prioritised based on the MoSCoW method (Must have, Should have, Could have, Won't have).

[Link to the GitHub Project board](https://github.com/users/Hugh1996/projects/3)

### User Stories

1. As an admin, I want the capability to create, read, update, and delete content to effectively manage the platform.
2. As an admin, I want the ability to create draft content so that I can start the writing process and complete it later.
3. As an admin, I want to approve or disapprove comments to filter out objectionable content and maintain a positive community environment.
4. As a user, I want to easily view a list of items so that I can select one to explore further.
5. As a user, I want the ability to click on an item to access and read its full details.
6. As a user or Admin, I want to be able to view the number of likes on each item to identify popular content on the platform.
7. As a user or Admin, I want to be able to view comments on individual posts to read and engage with interactions from other users.
8. As a user, I want to register an account so that I can comment on posts and express my likes.
9. As a user, I want to leave comments on content to further interact with the community and share my thoughts.
10. As a user, I want to be able to like or unlike a post to interact with the content and show my appreciation.
11. As a user, I want the capability to add my own content to share with the community.
12. As an admin, I want to approve or disapprove content submissions to filter out unsuitable items from being published on the platform.
13. As a user, I want to receive feedback on the status of my content submission so that I am informed about the progress of my contribution.
14. As a user, I want to create and customize my profile with personal details and a profile picture to enhance my presence on the platform.
15. As a user, I want to curate a list of my favorite items for quick access, ensuring that I can easily find and revisit content I love.
16. As a Site User I can search for recipes so that I can easily find and explore new dishes or locate specific recipes that I have in mind.

### Target Audience

- Asturian Locals: Residents of Asturias who are interested in exploring their local culinary traditions.
- Food Enthusiasts: Individuals passionate about regional cuisines and eager to discover the flavors of Asturias dishes.
- Home Cooks and Chefs: Those who enjoy cooking and experimeting with different recipes.
- Tourists: Visitors to Asturias who are intersted in immersing themselves in the local food culture.
- Food Bloggers: Individuals who want to share their own experiences, recipes and reviews related to Asturian Cuisine.

### First Time User

- Clear navigation making it easy to find recipes and community features.
- Offers a warm introduction to the website's purpose and mission.
- Informative content providing an overview of application functionality.
- Easy registration process.
- Good quality images to make the content visually appealing.
-

### Registered User

- Easy login process with a personalised user account.
- Browse recipe details
- Ability to add new recipes, pending approval
- Ability to like or review recipes.
- Ability to edit or delete reviews.
- Ability to update user profile info.

### Admin User

- Seperate secure login portal for admin users.
- Access to dashboard for recipe and reviews.
- Management of recipes, including the ability to view, modify, or delete recipes as needed
- Ability to delete user accounts, providing the necessary control for managing user data and accounts.

## Design

### Color Scheme

- The predominant color theme across the website is a subdued reddish-brown with a variations of transparency, drawing inspiration from the aesthetic credited to [A Pinch of Yum](https://pinchofyum.com/).
- Against this backdrop, white font is employed for optimal contrast, creating a visually pleasing text presentation. On alternative surfaces, standard black text is utilized. Card test utilizes a dark bluish grey for contrast.
- Consistency is maintained in button design, with all buttons adopting the aforementioned reddish-brown hue. A smooth transition to a vibrant orange, without transparency, occurs on hover. Notably, the 'Edit' and 'Delete' buttons deviate from this standard, employing the Bootstrap classes 'btn-warning' and 'btn-danger' respectively for a distinct visual indication.

### Typography

Roboto is the primary font for the site, providing versatility and modernity with excellent readability across devices. Sans Serif serves as a backup font for added flexibility.

### Data Models

#### Django Allauth

- Django Allauth is a third-party Django package that provides a set of authentication, registration, and account management functionalities for Django web applications. It handles user authentication, including login and registration.

#### Recipe

    title: A CharField to store the title of the recipe.
    slug: A SlugField to store a URL-friendly version of the title.
    author: A ForeignKey relation to the User model, representing the author of the recipe.
    updated_on: A DateTimeField to store the date and time when the recipe was last updated.
    excerpt: A TextField to store a brief excerpt or summary of the recipe.
    ingredients: A TextField to store the list of ingredients needed for the recipe.
    instructions: A TextField to store the cooking instructions for the recipe.
    featured_image: A ClouninaryField to store the featured image of the recipe, using Cloudinary for image storage.
    created_on: A DateTimeField to store the date and time when the recipe was created.
    status: A IntegerField to store the status of the recipe.
    likes: An ManyToManyField to represent users who liked the recipe.
    is_approved: A BooleanField to store whether the recipe is approved or not.

    Meta: Specifies the default ordering for queries. In this case, recipes will be ordered by the created_on field in descending order.

    save(self, *args, **kwargs): Overrides the default save method to automatically generate a slug from the title if it's not provided.

    __str__(self): Returns a string representation of the recipe title.

    number_of_likes(self): Returns the count of likes for the recipe.

    number_of_reviews(self): Returns the count of reviews for the recipe.

#### Review

    recipe: A ForeignKey relation to the Recipe model, representing the recipe to which the review is associated.
    name: A CharField to store the name of the reviewer.
    email: An EmailField to store the email address of the reviewer.
    body: A TextField to store the content or body of the review.
    created_on: A DateTimeField to store the date and time when the review was created.

    class Meta: Specifies the default ordering for queries. In this case, reviews will be ordered by the created_on field in descending order.

    __str__(self): Returns a string representation of the review, including the review body and the name of the reviewer.

#### UserProfile

    user: A OneToOneField relation to the User model, creating a profile for each user.
    bio: A TextField to store the biography or additional information about the user.
    profile_picture: A CloudinaryField A field to store the profile picture of the user, using Cloudinary for image storage.

![DrawSQL](/static/images/readme/datamodel.jpg)

## Features

### Existing Features

#### Home Page

- Navigation bar displas main heading, about section, and footer with social links are displayed.

![Home](/static/images/readme/home.jpg)

- Upon signing in, the sign-up button disappears.

![Button Disappears](/static/images/readme/disappear.jpg)

#### Navbar

- Users are notified of their login status on the top right of the navigation bar.
- Additional features for adding a recipe or accessing the profile appear.

![Navbar](/static/images/readme/userin.jpg)

#### About

- The about section contains the main deccription, vision and expectations for the application. It also informs the user of the benefits of creating an account.

![About](/static/images/readme/about.jpg)

#### Footer

- The footer contains copyright informatoio and the creators name. It also contains social links to the creators Github and LinkedIn profiles.

![Footer](/static/images/readme/footer.jpg)

#### Register

- Users can sign up by entering a username and password, along with a password confirmation. An email field is also optional. Upon successful registration, users will be automatically logged in and directed to the home page.

![Register](/static/images/readme/register.jpg)

#### Login

- After successfully signing up for the application, users can securely log into their accounts by entering their username and associated password.
- The navbar will display a logged-in status for users who have successfully signed in.

![Login](/static/images/readme/login.jpg)

#### Logout

- To log out, users can simply click on the logout button, which will then redirect them to a confirmation page where they can confirm their intention to log out.

![Logout](/static/images/readme/logout.jpg)

#### Recipes

- Users have the ability to browse a list of recipes, each accompanied by an image and a brief excerpt that highlights the essence of the recipe.
- The author's name is prominently displayed, and users can also see the like and review counts, providing insights into the popularity of each recipe.

![Recipes](/static/images/readme/recipes.jpg)

- Upon selecting a recipe for viewing, users will be presented with a detailed page featuring a clear image of the recipe. The page includes a comprehensive list of ingredients and step-by-step instructions for users to try the recipe at home.
- Additionally, users can see the number of likes and reviews for the recipe, and they have the option to view the reviews themselves. If logged in, users can interact with the recipe by liking it or adding their own review, enhancing the overall user engagement with the platform.

#### View Recipe/Reviews

![RecipeDetail](/static/images/readme/recipedetail.jpg)
![RecipeDetail2](/static/images/readme/recipedetail2.jpg)
![Reviews](/static/images/readme/review.jpg)

- Upon successfully adding a review, users will receive a notification confirming the successful addition and expressing gratitude for their feedback. Furthermore, users will have the option to both edit and delete their reviews, providing them with control and flexibility over their contributions. This incorporates CRUD functionality.

![Reviews](/static/images/readme/reviewfeedback.jpg)

#### Add a Recipe

- For logged-in users, the platform offers the capability to contribute by adding their own recipes. These submissions are sent to the admin site as drafts for review and approval.
- When submitting a recipe, users must provide a title, a brief description, list of ingredients, and step-by-step instructions.
- Additionally, users have the option to upload an image of the recipe. In cases where the user does not provide their own image, a placeholder image will automatically be assigned to the recipe.

![Add Recipe](/static/images/readme/addrecipe.jpg)
![Add Recipe](/static/images/readme/addrecipe2.jpg)

- After a user submits a recipe, a confirmation message will appear, notifying them that the recipe has been successfully submitted and is now pending approval. This provides users with clear feedback on the status of their contribution to the platform.

![Add Recipe](/static/images/readme/recipesubmit.jpg)

#### User Profile

- When a user is logged in, they can click on the profile icon to view their profile picture or bio. Their username will alrwady be displayed. A placeholder photo will automatically be displayed if the user has not uploaded a photo, and the bio section will be blank until the user adds their own information. This ensures a consistent and user-friendly experience within the profile section.

![User Profile](/static/images/readme/userprofile.jpg)

- Users have the ability to edit their bio by clicking the edit button in the profile section.
- Alternatively, they can choose to delete their profile details. Upon deletion, the profile will be wiped clean, leaving only the username intact. This empowers users to manage and customize their profile information according to their preferences.

![Edit Profile](/static/images/readme/editprofile.jpg)

##### Admin Features

- The Django built-in administrator panel provides comprehensive control over the website.
- Within the admin panel, admins can approve, update, and delete recipes, enabling effective content management.
- The admin an manage reviews.
- Further management is implemented in the control of user account.
- Both of the above implement CRUD functionality.

![Admin](/static/images/readme/admin.jpg)

### Features Left to Implement

#### User Favourites

- Users on our platform will soon enjoy the ability to curate a personalized list of their favorite recipes. This feature is designed to offer a seamless and convenient way to access and revisit the dishes they love. With quick retrieval in mind, users can effortlessly manage and revisit their curated list for an enhanced culinary experience.

#### Search Functionality

- A user-friendly search functionality will be introduced, allowing users to effortlessly discover new recipes or locate specific dishes they have in mind. This feature aims to enhance the overall user experience by making recipe exploration convenient and enjoyable.

#### User Profile Visibility

- An upcoming feature on our platform will allow users to view profiles of fellow users, fostering a sense of community within the culinary space. This feature is designed to promote interaction and engagement among users, providing an opportunity to explore and connect with each other through shared interests in cooking and recipes. Stay tuned for this exciting addition, as we aim to create a vibrant and collaborative community within our platform.

## Testing

### General Testing

- The deployed website underwent rigorous testing across diverse screen sizes utilizing tools such as [Am I Responsive](https://ui.dev/amiresponsive) and Developer Tools.

![Am I Responsive?](/static/images/readme/responsive.jpg)

- A comprehensive array of devices, including the iPhone 13, Samsung Galaxy S20, Toshiba Laptop, and Dell Desktop, were employed to verify the website's responsiveness.
- Furthermore, extensive browser compatibility testing was conducted on Google Chrome and Microsoft Edge to ensure optimal performance across different platforms.
- To ensure aesthetic coherence, feedback was sought from friends and family who confirmed the harmony of the site's color scheme and font style. Their input also confirmed that the website is user-friendly and easy to navigate.



### Lighthouse Testing

<details>
<summary>Home</summary>

![Home](https://res.cloudinary.com/duktk6qg0/image/upload/v1705232333/lighthousehome_wzjddz.jpg)

</details>

<details>
<summary>Recipes</summary>

![Recipes](https://res.cloudinary.com/duktk6qg0/image/upload/v1705232333/lighthouserecipes_wo8w2d.jpg)

</details>

<details>
<summary>Recipes Detail</summary>

![Recipe Detail](https://res.cloudinary.com/duktk6qg0/image/upload/v1705232333/lighthousedetail_zeb1qf.jpg)

</details>

<details>
<summary>Register</summary>

![Register](https://res.cloudinary.com/duktk6qg0/image/upload/v1705248875/lighthousesignup_ewnow1.jpg)

</details>

<details>
<summary>Login</summary>

![Login](https://res.cloudinary.com/duktk6qg0/image/upload/v1705233085/lighthouselogin_epgkys.jpg)

</details>

<details>
<summary>Logout</summary>

![Logout](https://res.cloudinary.com/duktk6qg0/image/upload/v1705232333/lighthouselogout_c8gzx0.jpg)

</details>

<details>
<summary>Add Recipe</summary>

![Add Recipe](https://res.cloudinary.com/duktk6qg0/image/upload/v1705232333/lighthouseadd_gpss6j.jpg)

</details>

<details>
<summary>User Profile</summary>

![User Profile](https://res.cloudinary.com/duktk6qg0/image/upload/v1705232333/lighthouseprofile_dnqzg6.jpg)

</details>

<details>
<summary>Edit Profile</summary>

![Edit Profile](https://res.cloudinary.com/duktk6qg0/image/upload/v1705232333/lighthouseedit_pi7meq.jpg)

</details>

### Code Validation

#### HTML

The [W3C Markup Validator](https://validator.w3.org/) service was used to validate HTML.

- [Home](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsabor-asturiano-cd988cf2702b.herokuapp.com%2F)
- [Recipes](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsabor-asturiano-cd988cf2702b.herokuapp.com%2Frecipes%2F)
- [Recipes Detail](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsabor-asturiano-cd988cf2702b.herokuapp.com%2Frecipe%2Ffabada-asturiana%2F)
- [Register](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsabor-asturiano-cd988cf2702b.herokuapp.com%2Faccounts%2Fsignup%2F)
- [Login](https://sabor-asturiano-cd988cf2702b.herokuapp.com/accounts/login/)
- [Logout](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsabor-asturiano-cd988cf2702b.herokuapp.com%2Faccounts%2Flogout%2F)
- [Add Recipe](https://validator.w3.org/nu/?doc=https%3A%2F%2Fsabor-asturiano-cd988cf2702b.herokuapp.com%2Fadd_recipe%2F)

#### CSS

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) service was used to validate to ensure no errors occurred. See results [here](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fsabor-asturiano-cd988cf2702b.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en).

#### Python

All below py files were passed through the [CI Python Linter](https://pep8ci.herokuapp.com/).

##### blog app

<details>
<summary>admin.py</summary>

![admin.py](https://res.cloudinary.com/duktk6qg0/image/upload/v1705182314/adminblog_nievlq.jpg)

</details>

<details>
<summary>forms.py</summary>

![form.py](https://res.cloudinary.com/duktk6qg0/image/upload/v1705182314/formblog_wzpo0s.jpg)

</details>

<details>
<summary>models.py</summary>

![models.py](https://res.cloudinary.com/duktk6qg0/image/upload/v1705182314/modelblog_k1rb1d.jpg)

</details>

<details>
<summary>urls.py</summary>

![url.py](https://res.cloudinary.com/duktk6qg0/image/upload/v1705182314/urlblog_qmzzgm.jpg)

</details>

<details>
<summary>views.py</summary>

![views.py](https://res.cloudinary.com/duktk6qg0/image/upload/v1705182314/viewblog_lbkrxn.jpg)

</details>

##### saborasturiano

<details>
<summary>settings.py</summary>

![settings.py](https://res.cloudinary.com/duktk6qg0/image/upload/v1705182314/settingsabor_oklnqq.jpg)

</details>

<details>
<summary>url.py</summary>

![url.py](https://res.cloudinary.com/duktk6qg0/image/upload/v1705182314/urlsabor_o7orbg.jpg)

</details>

#### JavaScript

The [JSHint JavaScript Validator](https://jshint.com/) service was used to validate to ensure no errors occurred.

<details>
<summary>JSHint</summary>

![JSHint](https://res.cloudinary.com/duktk6qg0/image/upload/v1705184188/js_a993f4.jpg)

</details>

#### Features Testing

#### Home Page

All below actions function as expected.

- Click website heading to redirect to Home Page.
- Click 'Home' on the navigation bar to redirect to Home Page.
- Click 'Recipes' on the navigation bar to redirect to Recipes Page.
- Click 'Register' on the navigation bar to redirect to Sign Up Page.
- Click 'Login' on the navigation bar to redirect to Login Page.
- Sign Up now button on background image also redirects to Sign Up Page.
- Click on Github icon in the footer to redirect to Github.
- Click on LinkedIn icon in the footer to redirect to LinkedIn.
- The user is notified of their logged in status in the navigation bar.

#### Home Page (Logged In)

All below actions function as expected.

- After Login/Sign Up the Sign Up now button is not visible.
- After Login/Sign Up the navigation bar changes. An Add Recipe, Logout and Profile option is available.
- The user is notified of their logged in status in the navigation bar.

#### Sign Up Page

All below actions function as expected.

- Enter invalid email format. Form will not submit.
- Email is optional.
- Enter invalid passoword Error will inform user incorrect.
- Type valid password. Form will submit.
- Type different password for cpassword confirmation. Form will not submit.
- Enter valid details. Form will submit and direct to Home Page. Account is created.
  
#### Login Page

All below actions function as expected.

- Enter valid details. Form will submit and direct to Home Page. User is logged in.
- Enter invalid password or username. Form will not submit.

#### Logout Page

All below actions function as expected.

- Click Logout to redirect to Logout Page
- Confirm sign out. Reidirect to Home Page. User is logged out.

#### Recipe Page 

All below actions function as expected.

- Click on recipe card. Redirects to Recipe Detail.
- Click on Next button. Redirect to next page.
- Click on Prev button. Redirect to previous page.

#### Recipe Detail Page

All below actions function as expected.

- All recipe details are provided.
- Can view number of likes and reviews.
- Can view the reviews.

#### Recipe Detail Page (Logged In User)

All below actions function as expected.

- All recipe details are provided.
- Can view number of likes and reviews.
- Can view reviews.
- Can like recipe.
- Can review recipe.
- Can edit and delete reviews.

#### Add Recipe Page

All below actions function as expected.

- Can submit own recipe for approval.

#### User Profile Page

All below actions function as expected.

- Can input, edit, create or delete bio.

#### Admin Panel

All below actions function as expected.

- Can manage recipes (CRUD)
- Can manage review (CRUD).
- Can manage user accounts.

### Bugs

#### Fixed bugs

- I encountered difficulty testing responsiveness on Am I Responsive due to the X_FRAME_OPTIONS setting in my Django project's settings.py file. Initially, it was set to 'SAMEORIGIN' which restricted testing.
- To address this, I first removed the setting from my settings.py file, allowing Django to use its default. However, this defaulted to 'DENY', which was inaccurate.
- To resolve the issue and enable testing on Am I Responsive, I adjusted X_FRAME_OPTIONS to 'ALLOWALL'. This modification allowed me to successfully test the responsiveness of my site.

##### Error 500

- I encountered a 500 error while attempting to load my signup page, I identified the issue to be related to the version of django-allauth installed. The error was prevalent with version 0.57.0. To resolve this, I downgraded to version 0.54.0 and updated my requirements.txt accordingly. This alleviated the error, and my signup page is now functioning as expected.

##### Password Validation

- I faced an issue with the password validation on my signup page, which seemed to be connected to the shortening of AUTH_PASSWORD_VALIDATORS in my settings.py file. The modification was initially made to adhere to PEP8 guidelines. However, upon restoring the lines to their original length, the password validation started working as expected.

#### Unfixed bugs

## Deployment

#### Fork

To fork the reopsitory, follow these steps:

- Log into your [Github](https://github.com/).
- Navigate to [SaborAsturiano](https://github.com/Hugh1996/sabor-asturiano-pp4).
- Click on the Fork button/ It is located on the top right
- The process will begin and a confirmation message should appear.

#### Clone

For local development, you aan clone the repository by following these steps:

- Log into your [Github](https://github.com/).
- Navigate to [SaborAsturiano](https://github.com/Hugh1996/sabor-asturiano-pp4).
- Directly above the files on the top right, click the green 'Code' button.
- Copy the URL.
- In your preferred IDE, open a terminal session in the directory you want to clone the repository to.
- Type 'git clone' and paste the copied URL.
- Set up a virtual environment (not required if you are using the Code Institute template and GitPod or Codeanywhere - this will be already set up).
- Press Enter to create the clone.
- Install packages by running command pip3 install -r requirements.txt

#### Heroku

- Log in to the Heroku dashboard.
- Create a new app from the dashboard.
- Connect GitHub Repository
- In the Heroku app dashboard, navigate to the Deploy tab.
- Connect your GitHub repository to the Heroku app.

#### Environment Variables

- In the Settings tab, locate the Config Vars section.
- Add the following environment variables:

  - DJANGO_SECRET_KEY: Your Django project secret key.
  - DATABASE_URL: Your database connection URL.
  - Add any other necessary environment variables.

- Enable Automatic Deploys

  - In the Deploy tab, enable automatic deploys from your GitHub repository.

- Deploy the App

  - Manually deploy the app for the first time by clicking the "Deploy Branch" button in the Deploy tab.

- Open the App

  - Once the deployment is successful, click the "Open App" button to view your deployed app.

View the live website here - [SaborAsturiano](https://sabor-asturiano-cd988cf2702b.herokuapp.com/)

## Techologies Used

This section outlines the various technologies used throughout the project and the purpose each serves.

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](<https://en.wikipedia.org/wiki/Python_(programming_language)>)

### Databases

- [ElephantSQL](https://www.elephantsql.com/) - Postgres database
- [Cloudinary](https://cloudinary.com/) - Online static file storage

### Programs

- [Github](https://github.com/) - Used to create application repository and utilize agile functionaility.
- [Codeanywhere](https://app.codeanywhere.com/) - Coding environment.
- [Heroku](https://id.heroku.com/login) - Cloud based platform to deploy site.
- [Canva](https://www.canva.com/) - Image usage.
- [Google Fonts](https://fonts.google.com/) - Used for the typography.
- [Am I Responsive](https://ui.dev/amiresponsive) - Used to test responsiveness on all screen sizes.
- [W3C Validator](https://validator.w3.org/) - Used to validatr HTML.
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to validate CSS.
- [JSHint](https://jshint.com/) - Used to validate JavaScript.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python.

### Frameworks

- [Django](https://www.djangoproject.com/)
- [Boostrap 5.3](https://getbootstrap.com/)

## Credits

### Content

- The Recipe and Review models were implemented with guidance from the I Think There I Blog walkthrough, for which credit is duly given.
- The starter templates for base.html, index.html, and recipe_detail.html were sourced from the same walkthrough and have been adapted for our project.
- The style.css file, credited to the I Think There I Blog walkthrough, has been used with amendments as required to suit our project needs.
- Credit goes to www.directoalpaladar.com, www.bonviveur.es, lacocinadefrabisa.lavozdegalicia.es and www.recetinas.com for providing the recipe ingredients and intructions uploaded.

### Media

- Credit to www.uplabs.com for the recipes placeholder image.
- Credit to www.directoalpaladar.com, www.bonviveur.es, lacocinadefrabisa.lavozdegalicia.es and www.recetinas.com for providing for recipe images.
- Credit to www.canava.com for all images used on the Home page.
- Credit to www.icons8.com for use of the favicon.

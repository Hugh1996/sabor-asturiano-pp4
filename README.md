# SaborAsturiano

SaborAsturiano (AsturianTastes) is a website dedicated to Asturian cuisine, offering a mix of traditional and modern recipes. The project exists to celebrate and preserve the culinary heritage of Asturias, promoting local ingredients and seasonal content.

It caters to a community of Asturian food enthusiasts, providing a platform for exploration, reviews, and contributions. The website's purpose is to bring together individuals passionate about Asturian flavors, fostering a sense of community and sharing among those interested in the region's diverse culinary traditions.

![Am I Responsive?]()

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

- [Responsiveness Testing](#responsiveness-testing)
- [Manual Testing](#manual-testing)
- [General Testing](#general-testing)
- [Lighthouse](#lighthouse)
- [Code Validation](#code-validation)

  - [HTML](#html)
  - [CSS](#css)
  - [Python](#python)
  - [JavaScript](#javascript)

### [Bugs](#bugs)

### [Deployment](#deployment)

- [Heroku Deployment](#heroku-deployment)

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

#### Recipes

- Users have the ability to browse a list of recipes, each accompanied by an image and a brief excerpt that highlights the essence of the recipe.
- The author's name is prominently displayed, and users can also see the like and review counts, providing insights into the popularity of each recipe.

![Recipes](/static/images/readme/recipes.jpg)

- Upon selecting a recipe for viewing, users will be presented with a detailed page featuring a clear image of the recipe. The page includes a comprehensive list of ingredients and step-by-step instructions for users to try the recipe at home.
- Additionally, users can see the number of likes and reviews for the recipe, and they have the option to view the reviews themselves. If logged in, users can interact with the recipe by liking it or adding their own review, enhancing the overall user engagement with the platform.

![RecipeDetail](/static/images/readme/recipedetail.jpg)
![RecipeDetail2](/static/images/readme/recipedetail2.jpg)
![Reviews](/static/images/readme/review.jpg)

- Upon successfully adding a review, users will receive a notification confirming the successful addition and expressing gratitude for their feedback. Furthermore, users will have the option to both edit and delete their reviews, providing them with control and flexibility over their contributions.

![Reviews](/static/images/readme/reviewfeedback.jpg)

#### Register

- Users can sign up by entering a username and password, along with a password confirmation. An email field is also optional. Upon successful registration, users will be automatically logged in and directed to the home page.

![Register](/static/images/readme/register.jpg)

#### Login

- After successfully signing up for the application, users can securely log into their accounts by entering their username and associated password.
- The navbar will display a logged-in status for users who have successfully signed in.

![Login](/static/images/readme/login.jpg)

![Add Recipe](/static/images/readme/addrecipe.jpg)

#### Logout

- To log out, users can simply click on the logout button, which will then redirect them to a confirmation page where they can confirm their intention to log out.

![Logout](/static/images/readme/logout.jpg)

### Features Left to Implement

## Testing

### Manual Testing

### General Testing

### Lighthouse Testing

### Responsiveness Testing

### Code Validation

#### HTML

#### CSS

#### Python

#### JavaScript

## Bugs

## Deployment

### Heroku Deployment

- Heroku App Creation

  - Log in to the Heroku dashboard.
  - Create a new app from the dashboard.

- Connect GitHub Repository

  - In the Heroku app dashboard, navigate to the Deploy tab.
  - Connect your GitHub repository to the Heroku app.

- Set Environment Variables

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
- [Canva](https://www.canva.com/) - Used to create images.
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

- The Recipe and Comment models were implemented with guidance from the I Think There I Blog walkthrough, for which credit is duly given.
- The starter templates for base.html, index.html, and recipe_detail.html were sourced from the same walkthrough and have been adapted for our project.
- The style.css file, credited to the I Think There I Blog walkthrough, has been used with amendments as required to suit our project needs.
- Credit goes to www.directoalpaladar.com for providing the recipe ingredients and intructions uploaded.

### Media

- Credit to www.uplabs.com for the recipes placeholder image.
- Credit to www.directoalpaladar.com for providing images for uploaded recipes.
- Credit to www.canava.com for all images used on the Home page.
- Credit to www.icons8.com for use of the favicon.

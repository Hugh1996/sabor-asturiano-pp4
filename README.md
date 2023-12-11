SaborAsturiano is a website dedicated to Asturian cuisine, offering a mix of traditional and modern recipes. The project exists to celebrate and preserve the culinary heritage of Asturias, promoting local ingredients and seasonal content. 

It caters to a community of Asturian food enthusiasts, providing a platform for exploration, comments, and contributions. The website's purpose is to bring together individuals passionate about Asturian flavors, fostering a sense of community and sharing among those interested in the region's diverse culinary traditions.

![Am I Responsive?]()

# Table of Contents

# Project Background

# Features

## Existing Features

## Features Left to Implement

# Process

## Research

## Development

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

## Data Models

![DrawSQL]()

# Testing

## Automatic Testing

## Manual Testing

### Overview

### General Testing

### Lighthouse Testing

### Responsiveness Testing

### Code Validation

# Bugs

# Deployment

## Heroku Deployment

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

# Techologies Used

This section outlines the various technologies used throughout the project and the purpose each serves.

## Core Development Technologies

- Django - used as a full-stack framwork for developing the app.
- HTML/CSS + Django Template Language used for building out site pages.

## Python/Django Packages

- Gunicorn - provides HTTP server.
- psycopg2 - provides PostgreSQL connection.

## Infrastructural Technologies

- PostgreSQL (via ElephantSQL) - used for database.
- Heroku - used for hosting the application.
- Cloudinary - used for storing and media files.
- Git - as a version control system.

# Credits

## Content

-

## Media

-

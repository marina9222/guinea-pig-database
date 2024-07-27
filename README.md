# [GUINEA PIG DATABASE](https://flask-guinea-pig-database-ccd8a0a6a383.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/marina9222/guinea-pig-database)](https://github.com/marina9222/guinea-pig-database/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/marina9222/guinea-pig-database)](https://github.com/marina9222/guinea-pig-database/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/marina9222/guinea-pig-database)](https://github.com/marina9222/guinea-pig-database)


# Description 

Piggy Profiles & Pics Hub is a website for guinea pig owners or just a guinea pig lover to register and add their own pet.
Once added people can like the pet and if it gets the most likes it will come first in the row on the home page.
Even if the user don't have a guinea pig can still register and check out the other guinea pigs and read about different breeds.
It's basically a database where users can show their guinea pig with a photo and description.

![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://flask-guinea-pig-database-ccd8a0a6a383.herokuapp.com)

## UX

The homepage effectively displays profiles with images and key details (breed, age, character) in a grid layout. This helps users quickly look and identify guinea pigs that they like.
The layout adjusts well to different screen sizes, ensuring usability on both desktops and mobile devices.The primary navigation menu includes essential links (Home, Log In, Register) making it easy for users to find and access these features.Each guinea pig profile provides relevant information such as breed, age, character traits, and owner’s name.
The design is straightforward, allowing users to browse profiles without unnecessary steps.

### Colour Scheme

- `#c6b6a7` used for primary color.
- `#e7d3c3` used for secondary color.
- `#d7b3a1` used for tertiery color.
- `#342719` used for primary text color.
- `#00796b` used for button color.

I used [coolors.co](https://coolors.co/c6b6a7-e7d3c3-d7b3a1-342719-00796b) to generate my colour palette.

![screenshot](documentation/colors.png)

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
    
    --main-color: #c6b6a7;
    --secondary-color: #e7d3c3;
    --tertiery-color: #d7b3a1;
    --text-color-primary: #342719;
    --secondary-text-color: #000000;
    --button-color: #00796b;
    --button-hover: #0d6357;
}
```

### Typography

- [Roboto](https://fonts.google.com/specimen/Roboto) was used for the primary headers and titles.

- [Montserrat](https://fonts.google.com/specimen/Montserrat) was used for all the other secondary text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the ones in the Register/Login form and Add and Edit pet form.


## User Stories

### New Site Users

- As a new site user, I would like to easily create an account, so that I can log in and browse the guinea pigs profiles.
- As a new site user, I would like to be able to browse the guinea pig profiles, even without a registration.
- As a new site user, I would like to add my pet, so that people can see it and like it.
- As a new site user, I would like to have a like/unlike buttons, so that I can choose which guinea pigs I like and which guinea pigs I don't.
- As a new site user, I would like to be able to edit my pet, if I make a mistake when adding it the first time or I would like to change its picture.
- As a new site user, I would like to be able to delete my pet, if I decide to.
- As a new site user, I would like to have a page with all the guinea pig breeds with some information about each breed and see only the pets from each breed I choose to check.

### Returning Site Users

- As a returning site user, I would like to have a liked pets section, so that I can see only the pets I liked already.
- As a returning site user, I would like to have a search bar available on the home page, so that I can search a guinea pig by name/age/breed etc.
- As a returning site user, I would like to receive notifications if I enable them, so that I can know every time a person adds a new pet.
- As a returning site user, I would like to have the option to add multiple pictures of my guinea pig when adding one instead of only one.
- As a returning site user, I would like to have a carousel with all the pets, so that I can navigate with arrows and don't have to go all the way down the page to see all of them.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/mobile-home-1.png)

Home/Logged In
  - ![screenshot](documentation/wireframes/mobile-home-2.png)

Add Pet
  - ![screenshot](documentation/wireframes/mobile-add-pet.png)

Edit Pet
  - ![screenshot](documentation/wireframes/mobile-edit-pet.png)

Breeds
  - ![screenshot](documentation/wireframes/mobile-breeds.png)

Breed Details
  - ![screenshot](documentation/wireframes/mobile-breed-details.png)

My Pets
  - ![screenshot](documentation/wireframes/mobile-my-pets.png)

Register
  - ![screenshot](documentation/wireframes/mobile-register.png)

Log In
  - ![screenshot](documentation/wireframes/mobile-log-in.png)



</details>

### Tablet Wireframes

<details>
<summary> Click here to see the Tablet Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/tablet-home-1.png)

Home/Logged In
  - ![screenshot](documentation/wireframes/tablet-home-2.png)

Add Pet
  - ![screenshot](documentation/wireframes/tablet-add-pet.png)

Edit Pet
  - ![screenshot](documentation/wireframes/tablet-edit-pet.png)

Breeds
  - ![screenshot](documentation/wireframes/tablet-breeds.png)

Breed Details
  - ![screenshot](documentation/wireframes/tablet-breed-details.png)

My Pets
  - ![screenshot](documentation/wireframes/tablet-my-pets.png)

Register
  - ![screenshot](documentation/wireframes/tablet-register.png)

Log In
  - ![screenshot](documentation/wireframes/tablet-log-in.png)


</details>


### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>

Home
  - ![screenshot](documentation/wireframes/dekstop-home-1.png)

Home/Logged In
  - ![screenshot](documentation/wireframes/dekstop-home-2.png)

Add Pet
  - ![screenshot](documentation/wireframes/dekstop-add-pet.png)

Edit Pet
  - ![screenshot](documentation/wireframes/dekstop-edit-pet.png)

Breeds
  - ![screenshot](documentation/wireframes/dekstop-breeds.png)

Breed Details
  - ![screenshot](documentation/wireframes/dekstop-breed-details.png)

My Pets
  - ![screenshot](documentation/wireframes/dekstop-my-pets.png)

Register
  - ![screenshot](documentation/wireframes/dekstop-register.png)

Log In
  - ![screenshot](documentation/wireframes/dekstop-log-in.png)


</details>


## Features


### Existing Features


- **Register form**

    - Register form for a new user to register and be able to log in and use all the features of the website.

![screenshot](documentation/features/feature01.png)


- **Log In form**

    - Log In form for already registered users.

![screenshot](documentation/features/feature02.png)


- **Add Pet**

    - Add Pet feature allows a registered user to add their own pet to the database.

![screenshot](documentation/features/feature03.png)


- **Find guinea pigs by breed**

    - Help users to quickly find guinea pigs sorted by their breed.

![screenshot](documentation/features/feature04.png)


- **Breed information**

    - Showing the user only guinea pigs by the chosen breed and give them some information about the breed.

![screenshot](documentation/features/feature05.png)


- **My Pets**

    - Shows only the user's pets so the pet could be edited or deleted if desired.

![screenshot](documentation/features/feature06.png)


- **Edit Pet**

    - Allows registered user to edit their pet if desired.

![screenshot](documentation/features/feature07.png)


- **Delete Pet**

    - Allows registered user to delete their pet if desired.

![screenshot](documentation/features/feature08.png)


- **Unlike Pet**

    - Allows registered user to unlike a pet if liked by mistake.

![screenshot](documentation/features/feature09.png)


- **Like Pet**

    - Allows registered user to like a pet from the database.

![screenshot](documentation/features/feature10.png)


### Future Features

- Liked pets section
    - A section showing the registered user only the pets they liked.

- Search bar
    - Search bar on the home page allowing the user to search for a pet by name/age/breed/likes.

- Notifications
    - Allow registered user to receive notifications about new added pets by email or pop up.

- Multiple images when adding a new pet
    - User the be allowed to upload more than one picture of their pet when adding one.

- Images carousel
    - Carousel showing the images on the home page so it could be easier to go through all of them , instead of scrolling all the way down.


## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Flask](https://img.shields.io/badge/Flask-grey?logo=flask&logoColor=000000)](https://flask.palletsprojects.com) used as the Python framework for the site.
- [![MongoDB](https://img.shields.io/badge/MongoDB-grey?logo=mongodb&logoColor=47A248)](https://www.mongodb.com) used as the non-relational database management with Flask.
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) used for online static file storage.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.

## Database Design

My project uses a non-relational database with MongoDB, and therefore the database architecture
doesn't have actual relationships like a relational database would.

My database is called **guineaPigsDB**.

It contains 3 collections:

- **breeds**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | pet_breed | String | |
    | info | String | |
    | breed_image | String | |

- **pets**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | pet_name | String | |
    | pet_age | String | |
    | pet_breed | String | selected from *breeds* collection |
    | pet_character | String | |
    | image_url | String | |
    | owner | String | selected from the *users* collection |

- **users**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | username | String | |
    | password | String | uses Secure Hash Algorithm (SHA) |

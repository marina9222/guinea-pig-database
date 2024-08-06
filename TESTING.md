# Testing

> Return back to the [README.md](README.md) file.


## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| templates | add_pet.html | ![screenshot](documentation/validation/add-pet-html.png) | pass |
| templates | breed_details.html | ![screenshot](documentation/validation/breed-details-html.png) | pass |
| templates | breeds.html | ![screenshot](documentation/validation/breeds-html.png) | pass |
| templates | edit_pet.html | ![screenshot](documentation/validation/edit-pet-html.png) | pass |
| templates | login.html | ![screenshot](documentation/validation/login-html.png) | pass |
| templates | my_pets.html | ![screenshot](documentation/validation/my-pets-html.png) | pass |
| templates | pets.html | ![screenshot](documentation/validation/pets-html.png) | pass |
| templates | register.html | ![screenshot](documentation/validation/register-html.png) | pass |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | styles.css | ![screenshot](documentation/validation/css-validation.png) |pass |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | app.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/marina9222/guinea-pig-database/main/app.py) | ![screenshot](documentation/validation/python-validation.png) | pass |


## Browser Compatibility


I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Login | Register | Home/Logged in | Add Pet | Breeds | My Pets | Edit Pet | Breed Details | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-login.png) | ![screenshot](documentation/browsers/browser-chrome-register.png) | ![screenshot](documentation/browsers/browser-chrome-home-2.png) | ![screenshot](documentation/browsers/browser-chrome-add-pet.png) | ![screenshot](documentation/browsers/browser-chrome-breeds.png) | ![screenshot](documentation/browsers/browser-chrome-my-pets.png) | ![screenshot](documentation/browsers/browser-chrome-edit-pet.png) | ![screenshot](documentation/browsers/browser-chrome-breed-details.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-login.png) | ![screenshot](documentation/browsers/browser-firefox-register.png) | ![screenshot](documentation/browsers/browser-firefox-home-2.png) | ![screenshot](documentation/browsers/browser-firefox-add-pet.png) | ![screenshot](documentation/browsers/browser-firefox-breeds.png) | ![screenshot](documentation/browsers/browser-firefox-my-pets.png) | ![screenshot](documentation/browsers/browser-firefox-edit-pet.png) | ![screenshot](documentation/browsers/browser-firefox-breed-details.png) | Works as expected |
| Opera | ![screenshot](documentation/browsers/browser-opera-home.png) | ![screenshot](documentation/browsers/browser-opera-login.png) | ![screenshot](documentation/browsers/browser-opera-register.png) | ![screenshot](documentation/browsers/browser-opera-home-2.png) | ![screenshot](documentation/browsers/browser-opera-add-pet.png) | ![screenshot](documentation/browsers/browser-opera-breeds.png) | ![screenshot](documentation/browsers/browser-opera-my-pets.png) | ![screenshot](documentation/browsers/browser-opera-edit-pet.png) | ![screenshot](documentation/browsers/browser-opera-breed-details.png) | Works as expected |


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Login | Register | Home/Logged in | Add Pet | Breeds | My Pets | Edit Pet | Breed Details | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsiveness/responsive-mobile-home.png) | ![screenshot](documentation/responsiveness/responsive-mobile-login.png) | ![screenshot](documentation/responsiveness/responsive-mobile-register.png) | ![screenshot](documentation/responsiveness/responsive-mobile-home-2.png) | ![screenshot](documentation/responsiveness/responsive-mobile-add-pet.png) | ![screenshot](documentation/responsiveness/responsive-mobile-breeds.png) | ![screenshot](documentation/responsiveness/responsive-mobile-my-pets.png) | ![screenshot](documentation/responsiveness/responsive-mobile-edit-pet.png) | ![screenshot](documentation/responsiveness/responsive-mobile-breed-details.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsiveness/responsive-tablet-home.png) | ![screenshot](documentation/responsiveness/responsive-tablet-login.png) | ![screenshot](documentation/responsiveness/responsive-tablet-register.png) | ![screenshot](documentation/responsiveness/responsive-tablet-home-2.png) | ![screenshot](documentation/responsiveness/responsive-tablet-add-pet.png) | ![screenshot](documentation/responsiveness/responsive-tablet-breeds.png) | ![screenshot](documentation/responsiveness/responsive-tablet-my-pets.png) | ![screenshot](documentation/responsiveness/responsive-tablet-edit-pet.png) | ![screenshot](documentation/responsiveness/responsive-tablet-breed-details.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsiveness/responsive-desktop-home.png) | ![screenshot](documentation/responsiveness/responsive-desktop-login.png) | ![screenshot](documentation/responsiveness/responsive-desktop-register.png) | ![screenshot](documentation/responsiveness/responsive-desktop-home-2.png) | ![screenshot](documentation/responsiveness/responsive-desktop-add-pet.png) | ![screenshot](documentation/responsiveness/responsive-desktop-breeds.png) | ![screenshot](documentation/responsiveness/responsive-desktop-my-pets.png) | ![screenshot](documentation/responsiveness/responsive-desktop-edit-pet.png) | ![screenshot](documentation/responsiveness/responsive-desktop-breed-details.png) | Works as expected |
| Iphone 13 | ![screenshot](documentation/responsiveness/responsive-iphone13-home.png) | ![screenshot](documentation/responsiveness/responsive-iphone13-login.png) | ![screenshot](documentation/responsiveness/responsive-iphone13-register.png) | ![screenshot](documentation/responsiveness/responsive-iphone13-home-2.png) | ![screenshot](documentation/responsiveness/responsive-iphone13-add-pet.png) | ![screenshot](documentation/responsiveness/responsive-iphone13-breeds.png) | ![screenshot](documentation/responsiveness/responsive-iphone13-my-pets.png) | ![screenshot](documentation/responsiveness/responsive-iphone13-edit-pet.png) | ![screenshot](documentation/responsiveness/responsive-iphone13-breed-details.png) | Works as expected |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| Log In | ![screenshot](documentation/lighthouse/lighthouse-login-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-login-desktop.png) | Some minor warnings |
| Register | ![screenshot](documentation/lighthouse/lighthouse-register-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-register-desktop.png) | Some minor warnings |
| Home/Logged In | ![screenshot](documentation/lighthouse/lighthouse-home-2-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-2-desktop.png) | Slow load due to large images |
| Add Pet | ![screenshot](documentation/lighthouse/lighthouse-add-pet-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-add-pet-desktop.png) | Some minor warnings |
| Breeds | ![screenshot](documentation/lighthouse/lighthouse-breeds-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-breeds-desktop.png) | Some minor warnings |
| My Pets | ![screenshot](documentation/lighthouse/lighthouse-my-pets-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-my-pets-desktop.png) | Slow load due to large images |
| Edit Pet | ![screenshot](documentation/lighthouse/lighthouse-edit-pet-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-edit-pet-desktop.png) | Some minor warnings |
| Breed Details | ![screenshot](documentation/lighthouse/lighthouse-breed-details-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-breed-details-desktop.png) | Some minor warnings |

## Defensive Programming

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Register | | | | | |
| | Feature is expected to open a register form for the user to regiter an account | Tested the feature by doing it | The feature behaved as expected, and it did registered without problems| Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| Log In | | | | | |
| | Feature is expected to sign in the user when the form is filled and the user name and password match | Tested the feature by log in my account | The feature behaved as expected, and it did logged me in | Test concluded and passed | ![screenshot](documentation/features/feature02.png) |
| Add Pet | | | | | |
| | Feature is expected to add a new pet owned by the user when the form is filled | Tested the feature by adding a pet | The feature behaved as expected, and it did added the pet | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| Breeds | | | | | |
| | Feature is expected to do help the user find guinea pigs by breed | Tested the feature by clicking on every breed to check for the pets if they match | The feature behaved as expected, and it did show all the pets by breeds | Test concluded and passed | ![screenshot](documentation/features/feature04.png) |
| Breed Details | | | | | |
| | Feature is expected to view the pets from this breed and read some information about the chosen breed | Tested the feature by doing it | The feature behaved as expected, and it did show the pets and the information of every breed | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| My Pets | | | | | |
| | Feature is expected to show the user only their own pets and if they dont have any to show a message saying: You have not added any pets yet. | Tested the feature by doing it | Feature is expected and shows only my pets | Test concluded and passed | ![screenshot](documentation/features/feature06.png) |
| Edit Pet | | | | | |
| | Feature is expected to allow the user to edit their pet by clicking the edit button. | Tested the feature by trying to edit one of my pets. | The feature behaved as expected, and it opened a form to edit my pet. | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| Home/My Pets | | | | | |
| | Feature is expected to allow the user to delete their own pets if needed. | Tested the feature by trying to delete one of my pets. | The feature behaved as expected, and it deleted my pet. | Test concluded and passed  | ![screenshot](documentation/features/feature08.png) |
| Home | | | | | |
| | Feature is expected to allow a registered user to unlike a pet if clicked liked by mistake. | Tested the feature by clicking on unlike button. |  The feature behaved as expected, and it unliked a pet. | Test concluded and passed | ![screenshot](documentation/features/feature09.png) |
| Home | | | | | |
| | Feature is expected to allow a registered user to like a pet. | Tested the feature by clicking on like button. | The feature behaved as expected, and it liked the chosen pet. | Test concluded and passed | ![screenshot](documentation/features/feature10.png) |


## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to easily create an account, so that I can log in and browse the guinea pigs profiles. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to be able to browse the guinea pig profiles, even without a registration.| ![screenshot](documentation/features/feature11.png) |
| As a new site user, I would like to add my pet, so that people can see it and like it. | ![screenshot](documentation/features/feature03.png) |
| As a new site user, I would like to have a like/unlike buttons, so that I can choose which guinea pigs I like and which guinea pigs I don't. | ![screenshot](documentation/features/feature09.png) |
| As a new site user, I would like to be able to edit my pet, if I make a mistake when adding it the first time or I would like to change its picture. | ![screenshot](documentation/features/feature07.png) |
| As a new site user, I would like to be able to delete my pet, if I decide to. | ![screenshot](documentation/features/feature08.png) |
| As a new site user, I would like to have a page with all the guinea pig breeds with some information about each breed and see only the pets from each breed I choose to check. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to have a liked pets section, so that I can see only the pets I liked already. | future features |
| As a returning site user, I would like to have a search bar available on the home page, so that I can search a guinea pig by name/age/breed etc. | future features | 
| As a returning site user, I would like to receive notifications if I enable them, so that I can know every time a person adds a new pet. | future features | 
| As a returning site user, I would like to have the option to add multiple pictures of my guinea pig when adding one instead of only one. | future features | 
| As a returning site user, I would like to have a carousel with all the pets, so that I can navigate with arrows and don't have to go all the way down the page to see all of them. | future features | 


## Bugs

- Python : values for both 'fields' and 'body' error when try to upload picture using Cloudinary


    - To fix this, I updated cloudinary with the latest version.

- Python TypeError: 'Collection' object is not callable.

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I changed the code line `mongo.db.pets.update_one({"_id":ObjectId(pet_id)},submit) to mongo.db.pets.update_one({"_id":ObjectId(pet_id)},{"$set":update_data})`.


- Python jinja : UndefinedError

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I added another pet object so it can access the nested object structure.

- Materialize : Cards bug

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I have to transform my whole project from Materialize to Bootstrap as Materialize has a bug in the framework so you actually can't have a responsive layout.

    ![screenshot](documentation/bugs/fixed.png)

    

## Unfixed Bugs
 
> There are no remaining bugs that I am aware of.

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


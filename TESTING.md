# Testing

Return back to the [README.md](README.md) file.


## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page  | Screenshot | Notes |
| ---|  --- | --- |
| Home|![Home](static/documents/screenshots/home-html.png)|pass(No Errors)|
| About|![About](static/documents/screenshots/about-html.png) |Pass (No Errors)|
| Search|![Search](static/documents/screenshots/search-html.png) | Pass(No Errors) |
| Login|![Login](static/documents/screenshots/login-html.png) |Pass(No Errors)|
|Logout|![Logout](static/documents/screenshots/logout-html.png)|Pass(No Errors)|
|Register|![Register](static/documents/screenshots/rigister-html.png) | Errors form Django Form(not visible in template ) |
|Create-post|![Create](static/documents/screenshots/create-html.png )| Errors form Django Form(not visible in template, its caused by editor) |
|Create-post|![Create](static/documents/screenshots/createpost-html.png) |Pass(No Error after uninstalling Editors)|
|Update-Post|![Update](static/documents/screenshots/update-post-html.png) |Pass(No Errors)|
|Update-Post|![Update](static/documents/screenshots/update 2-html.png )|Errors form Django Form(not visible in template, its caused by editor)|
|Delete-Post|![Delete](static/documents/screenshots/delete-html.png)|Pass(No Errors)| 
|Post-Detail|![Post-detail](static/documents/screenshots/post-setail-html.png) |Errors(Not visible in templete) |
|Contact-us|![Contact-us](static/documents/screenshots/contact-html.png)|Pass(No Errors)|
|Profile|![Profile](static/documents/screenshots/profile-html.png) |Pass(No Errors)|
|Password-reset 1|![Password-reset-1](static/documents/screenshots/password-1-html.png)|Pass(No Errors)|
|Password-reset 2|![Password-reset-2](static/documents/screenshots/password-2-html.png)|Pass(No Errors)|
|Password-reset 3|![Password-reset-3](static/documents/screenshots/password-3-html.png) |Pass(No Errors)|
|Password-reset 4|![Password-reset-4](static/documents/screenshots/password-final-html.png) |Pass(No Errors)|





### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Screenshot | Notes |
| --- | --- | --- | 
|Parentingram|![css-validation](static/documents/screenshots/Css-Validation.png) |Pass(No Errors)|


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| comments.js | ![comments.js](static/documents/screenshots/comments.png) | Pass: No Errors |
| create-post.js | ![screenshot](static/documents/screenshots/create-js.png) | Pass: No Errors |
| sign-up.js | ![screenshot](static/documents/screenshots/signuu-js.png) | Pass: No Errors |



### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Validation For Parentingram
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| asgi.py | [PEP8 CI]() | ![asgi](static/documents/screenshots/asgi-py.png) | Pass: No Errors |
| settings.py | [PEP8 CI]() | ![setting](static/documents/screenshots/setting-py.png) | Pass: No Errors |
| urls.py | [PEP8 CI]() | ![url](static/documents/screenshots/perentingram-url-py.png) | : 1 Errors(Long Line Error) |
| wsgi.py | [PEP8 CI]() | ![wsgi](static/documents/screenshots/wsgi-py.png) | Pass: No Errors |

#### Validation For blog App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI]() | ![admin](static/documents/screenshots/blog-admin-py.png) | Pass: No Errors |
| apps.py | [PEP8 CI]() | ![app](static/documents/screenshots/blog-app-py.png) | Pass: No Errors |
| forms.py | [PEP8 CI]() | ![form](static/documents/screenshots/blog-form-py.png) | Pass: No Errors |
| models.py | [PEP8 CI]() | ![model](static/documents/screenshots/blog-model-py.png) | :  No Errors |
| views.py | [PEP8 CI]() | ![view](static/documents/screenshots/blog-url-py.png) | : Error 501(line too long) |
| urls.py | [PEP8 CI]() | ![url](dstatic/documents/screenshots/blog-url-py.png) | : Error 501(line too long) |

#### Validation For about App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI]() | ![admin](static/documents/screenshots/about-admin-py.png) | Pass: No Errors |
| apps.py | [PEP8 CI]() | ![app](static/documents/screenshots/about-app-py.png) | Pass: No Errors |
| models.py | [PEP8 CI]() | ![model](static/documents/screenshots/about-model-py.png) | Pass: No Errors |
| urls.py | [PEP8 CI]() | ![url](static/documents/screenshots/about-url-py.png) | Pass: No Errors |
| views.py | [PEP8 CI]() | ![view](static/documents/screenshots/about-view-py.png) | Pass: No Errors |


#### Validation For contact-us App
| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [PEP8 CI]() | ![admin](static/documents/screenshots/contact-admin-py.png) | Pass: No Errors |
| apps.py | [PEP8 CI]() | ![app](static/documents/screenshots/contact-app-py.png) | Pass: No Errors |
| models.py | [PEP8 CI]() | ![model](static/documents/screenshots/contact-model-py.png) | Pass: No Errors |
| form.py | [PEP8 CI]() | ![form](static/documents/screenshots/contact-form-py.png) | Pass: No Errors |
| urls.py | [PEP8 CI]() | ![url](static/documents/screenshots/contact-url-py.png) | Pass: No Errors |
| views.py | [PEP8 CI]() | ![view](static/documents/screenshots/contact-view-py.png) | :  Errors 501(line too long) |


## Browser Compatibility


I've tested my deployed project on  browsers to check for compatibility issues.

* It was working fine on safari.((home page is little slow to load))
* it was working fine on chorome.(home page is little slow to load)


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.


![responsive](static/documents/screenshots/responsiveness.png)


I have cheked responsivness on various screen, here are the results for Desktop, Tablet and Mobile Phone.

|Screen|Result|
|---|---|
|Desktop|![desktop](static/documents/screenshots/desktop.png)|
|Tablet|![Tablet](static/documents/screenshots/ipad.png)|
|Mobile phone|![Mobile](static/documents/screenshots/mobile.png)|



## Lighthouse Testing:

### Website App Templates -Testing
| Page |Screenshot | ---|
| --- | --- | --- |
| Home |  ![Home](static/documents/screenshots/lighthouse-home1.png) | 
| About |  ![About](static/documents/screenshots/lighthouse-about.png) | 
| Contact-us |  ![contact-us](static/documents/screenshots/lighthouse-contactus.png) | 
| Create-post | ![create-post](static/documents/screenshots/lighthouse-create.png) | 
| Update-post |  ![Update-post](static/documents/screenshots/lighthouse-update.png) | 
| Post-Detail | ![Post-detail](static/documents/screenshots/lighthouse-postdetail.png) | 
| Delete-post | ![Delete-post](static/documents/screenshots/lighthouse-delete.png) |
| Seach-post | ![Serach-post](static/documents/screenshots/lighthouse-search.png) | 
| Login | ![Login](static/documents/screenshots/lighthouse-signin.png) |
| Logout |  ![Logout](static/documents/screenshots/lightlouse-logout.png) | 
| Register  |  ![Register](static/documents/screenshots/lighthouse-register.png) | 
| Profile| ![Profile](static/documents/screenshots/lighthouse-profile.png)|
| Password-1| ![Password-1](static/documents/screenshots/lighthouse-password-1.png)|
| Password-2| ![Password-2](static/documents/screenshots/lighthouse-password-2.png)|
| Password-3| ![Password-3](static/documents/screenshots/lighthouse-password-3.png)|
| Password-4| ![Password-4](static/documents/screenshots/lighthouse-password-4.png)|

#### Note:

("I have warnings in Lighthouse due to two Bootstrap CSS files. I use Summernote for the admin panel and CKEditor for creating and updating posts on the front-end. I could not Fixed it due to shortage of time.")


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
|Home| Click on Home link in navbar | Redirection to Home page | Pass | |
|About| Click on About link in navbar | Redirection to About page | Pass | |
|Register| Click on Register link in navbar | Redirection to Register page | Pass | |
|Sign-in| Click on Login link in navbar | Redirection to sign-in page | Pass | |
|Feature image | Click on post Image | Redirection to that post details page | Pass | |
|Next| Click on Pagination next double arrow | Redirection to next pagination page | Pass | |
|Previous | Click on Pagination previus double arrow | Redirection to previous pagination page | Pass | |
|Search | Click on Search button in navbar |redirects to search page |Pass | |
|Create| click on Create link in navbar is only visible when user is loggedin| open Create post page|  Pass|  |
|Profile| click on Profile link in navbar is only visible when user is loggedin| open Profile page|  Pass|  |




## Submit Form Validation:
 |Form name|Pass/Fail|
 |----|-----|
 |Register:| Pass|
 |Sign In:| Pass|
 |Forgot Password:| Pass|
 |password Reset:| Pass|
 |Create post:| Pass|
 |Update post:| Pass|
 |Contact Us:| Pass|
 |Delete Post:| Pass|


 ## Custom Error Pages:

I have added added 4 error pages in all of the apps:

* 403 Error
* 404 Error
* 405 Error
* 500 Error

![error](static/documents/screenshots/error1.png)


## Bugs and Fixes:


-  Home page:  
homepge  page was not opening.

   
- Sulution:
     To fix this, i logged in in admin pannel and deleted the last post(with out slug), and then it started working.

-  Author:

    
Bug:
   I have an author field on my create post page which have foriegn key and was display all the user names as option.

Solution:
    To fix it, I removed author field form form and added it in create post view.



 - Slug-field: 

 Bug: 
    I have slug field in my create post form, but users were unaware of slug term.

 solution:
    I hide slug field using form label to empty string and used java script to target input field, then I added in the model to slugify title of the post and add it in the form.



- Search:


 Bug:
  I had error 404 for search page.


 solution:
        I fixed it by changing the order of url paths



- Error 404:

Bug:
  There was an error opening the post detail.

solutioon: 
    I fixed it by fixing the url postion.



 - Data base error:

Bug:
  There was an error i was unable to access my website.


    ![programming](static/documents/screenshots/programing-error.png)  


 solution:
    I was able to fix it with the help of tutor support, who advised me to delete all migrations and then use a new data base.


-  Footer:

Bug:
  on some pages Footer was float at top, i tried position(stickey,fixed,absolute,static). But they all were not working same on all pages.

solutions:
    I fixed footer by adding margin-top in css.




## Unfixed Bugs

* There are few bug in Django formm and sumernote that are seen in html validation. I was unable to clear them.

* There are Two errors in the terminal that i am unable to fix they are from gitpod."ms-toolsai.vscode-jupyter-slideshow extension is not synced, but not added in .gitpod.yml".


![Bugs](static/documents/screenshots/unfixed-bugs.png)










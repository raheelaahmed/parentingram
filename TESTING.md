# Testing:


## HTML Validation:







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
|Register|  --- | --- |
|Create-post|  --- | --- |
|Update-Post|  --- | --- |
|Delete-Post|  --- | --- |
|Post-Detail|  --- | --- |
|Contact-us|  --- | --- |




### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Screenshot | Notes |

| --- | --- | --- | 

|Parentingram|![css-validation](static/documents/Css-Validation.png) |Pass(No Errors)|


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |

| comments.js | ![comments.js](static/documents/screenshots/comments.png) | Pass: No Errors |
| create-post.js | ![screenshot](static/documents/screenshots/create-js.png) | Pass: No Errors |


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

* It was working fine on safari.
* it was working fine on chorome.


## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.


![responsive](static/documents/screenshots/responsive.png)


## Lighthouse Testing:

### Website App Templates - Desktop Testing
| Page |Screenshot | ---|
| --- | --- | --- |
| Home |  ![Home](static/documents/screenshots/lighthouse.png) | 
| About |  ![About](static/documents/screenshots/lighthouse-about.png) | 
| Contact-us |  ![contact-us](static/documents/screenshots/lighthouse-contactus.png) | 
| Create-post | ![create-post](static/documents/screenshots/lighthouse-create.png) | 
| Update-post |  ![Update-post](static/documents/screenshots/lighthouse-updatepost.png) | 
| Post-Detail | ![Post-detail](static/documents/screenshots/lighthouse-postdetail.png) | 
| Delete-post | ![Delete-post](static/documents/screenshots/lighthouse-deletepost.png) |
| Seach-post | ![Serach-post](static/documents/screenshots/lightouse-search.png) | 
| Login | ![Login](static/documents/screenshots/lighthouse-signin.png) |
| Logout |  ![Logout](static/documents/screenshots/lighthouse-logout.png) | 
| Register  |  ![Register](static/documents/screenshots/lighthouse-register.png) | 
| Custom Error page| ![Error-page] | No warnings |




## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Nav links | | | | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Click on About link in navbar | Redirection to About page | Pass | |
| | Click on Register link in navbar | Redirection to Register page | Pass | |
| | Click on Login link in navbar | Redirection to Login page | Pass | |
| | Click on post Image | Redirection to that post details page | Pass | |
| | Click on Pagination next double arrow | Redirection to next pagination page | Pass | |
| | Click on Pagination previus double arrow | Redirection to previous pagination page | Pass | |
| | Click on Search button in navbar |redirects to search page |Pass | |
| | click on Create link in navBar is only visible when user is loggedin| open Create post page|  Pass|  |
| Register | | | | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| Login | | | | |
| | Enter valid password| Field will only accept password format | Pass| |
| | Click Login button|  Redirects user to home page | Pass| |
| Logout | | | | |
| | Click Logout button | Logs out user, Redirects user to logout page | Pass |



## User Story Testing

| User Story | Screenshot |
| --- | --- |













## Bugs


-   homepge  page was not opening.

   

    - To fix this, i logged in in admin pannel and deleted the last post(with out slug), and then it started working.

- Author:

    
     - I have an author field on my create post page which have foriegn key and was display all the user names as option.



          - To fix it, I removed author field form form and added it in create post view.



 - Slug-field: 

       - I have slug field in my create post form, but users were unaware of slug term.


           - I hide slug field using form label to empty string and used java script to target input field, then I added in the model to slugify title of the post and add it in the form.



- Search:


     -  I had error 404 for search page.


          - I fixed it by bring the url on 2nd line of url path.



- Error 404:


       - There was an error opening the post detail.


       ![post](static/documents/screenshots/error 404.png)


       - I fixed it by fixing the url postion.



 - Data base error:

    - There was an error i was unable to access my website.


    ![programming](static/documents/screenshots/programing error.png)  


    - I was able to fix it with the help of tutor support, who advised me to delete all migrations and then use a new data base.








    
## Unfixed Bugs

There are few bug in Django formm and sumernote that are seen in html validation. I was unable to clear them.








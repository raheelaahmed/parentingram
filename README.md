i used this bootstrap template for the project https://github.com/StartBootstrap/startbootstrap-one-page-wonder/blob/master/dist/index.html

https://github.com/startbootstrap/startbootstrap-one-page-wonder?tab=readme-ov-file#start-bootstrap---one-page-wonder



pictures from Shuttersstocks,pexels
post from 
https://www.psychologytoday.com/ie/basics/parenting#:~:text=Ultimately%2C%20parents%20should%20strive%20to,Essential%20Reads

helthy habits artical from https://mentalhealthcenterkids.com/blogs/articles/healthy-habits-for-kids#:~:text=Good%20habits%20to%20develop%20include,gratitude%2C%20and%20self%2Dcare.

worksheet from here. https://www.worksheetplace.com/index.php?function=DisplayCategory&showCategory=Y&links=2&id=376&link1=31&link2=376&cn=Feelings_Activities


website i used for data:
https://kidshealth.org/en/parents/homework.html

https://www2.hse.ie/pregnancy-birth/preparing-for-a-new-baby/





# Parentingram 

![home-page](static/documents/screenshots/Home-page.png)


As the name suggests, Parentingram is a community platform designed for parents. It's a place where parents can come together to share ideas, tips, and experiences related to parenting. You can find a variety of content, including healthy recipes, lunch ideas, educational posts, activity sheets, and information about local events and sports.
The platform also allows you to engage with other parents by commenting on posts and expressing your likes or dislikes.

## UX

The design philosophy was to create a simple blog where user can see post and share posts and share their comment on other posts. 

### Colour Scheme


The color scheme uses bright full of life colors like(pink, orange, red, white and black color for footer) which is present throughout the site.


I used a bootstrap template to bring colors to my website which is linked below:

[Bootstrap Template](https://github.com/StartBootstrap/startbootstrap-one-page-wonder/tree/master)






## User Stories

All user stories can be found in a linked GitHub project [here](https://github.com/users/raheelaahmed/projects/4)


## Features:

Parentingram is community blog it has a number of features:

* User can see posts
* User can search the post in search bar by post title,content and authors name.
* After logging in user canlike or dislike the posts.
* After logging in User can comment on posts post.
* After logging in User can make their own post using post form, update and delete their post.(user can only update or delete their own posts)
* After loggin in User can send message to Admin.

## Nav bar:

Nav bar 6 items when user is not logged in.

* PARENTINGRAM LOGO:

logo is on the left side on Nav bar.

* HOME:

Home is the link for the homepage, when all the posts are displayed.

* ABOUT:

About the blog and its purpose.

* REGISTER :

Register page has a form so user can sign up for the form.

* LOGIN:

If your already a user you can lonin from this page or you can sign up as anew user as well.

* SEARCH:

This feature allows the user to search for the posts.

![nav-bar](static/documents/screenshots/nav-bar-logout.png)


Once you are loggedin then Create feature apears on Navbar.

![nav-bar2](static/documents/screenshots/navbar-login.png)

* LOGOUT:

now you can see Logout, you can logout using this feature.

* CREATE:

This is very important feature of website, you can create your own post using this button. it only appears if you are loggedin on the website.

### Site Pages

- **Homepage**

    - The main homepage for the site. All the posts are displayed on the this page, you can scroll up and down to see post, using next button you can go on next page to see more posts.
    post images are displayed, user can open the post by clicking on the image.

![Home](static/documents/screenshots/home.png)

- **About Page**

    - About page. Gives users essential information about the blog and the purpose of the blog.

![About](static/documents/screenshots/about.png)

- **Create Page**

    - User can create a post using create post form, Post have 4 Fields(Image, Title, Author and content ). it is important to include first 3 fields other wise form will not work. User can publish the post on page after slecting published from  status list. your post will be posted on home page on clicking create Post button. you will recieve a success message with a link to view the post on home page.

  ![create-post](static/documents/create-post.png)  




- **Post_detail**


User can see the post-detail page once click or taps on the post image on home page. It has post title, date when the post was created, author's name , image and content.
if user is logged in then he can like or dislike the post and can make a comment on the post as well. If user is the author of the post he can edit or delete the post as well.
If user is not logged in, he can see the post and deils but can not like, dislike and comment.



![post-detail1](static/documents/post-deatil1.png)


![post-detail2](static/documents/screenshots/post-deatil2.png)



- **Update-post**

If user is the author of the post then he can edit the post on clicking edit button on post detail page.
once user click editpost button a new page is displayed with an update form on it ,user can make necessary changes and click on update button post will be updated and post detail will be opeded where user can see his updated post and a success message that you post ahve been updated.









- **Contact Page**


    - Contact Page. Users can see contact information for the tennis club, including 
    a contact email address and location information. An embedded Google Maps widget allows users to see the club's exact location.

![screenshot](documentation/features/sitepages/contact.png)

- **Register Page**

    - Register Page. Displays a form that new users of the site can fill in and make an account. The form is short, simple, and clean to encourage users to use it.

![screenshot](documentation/features/sitepages/register.png)

- **Login Page**

    - Login Page. Displays a login form that existing users can use to log in to the site. Two simple input fields for username and password make it easy for users to log in to their account. A Forgot Password link takes users to another page where they can recover their password. A sign up button at the bottom of the page lets users who do not yet have an account easily find the register page

![screenshot](documentation/features/sitepages/login.png)

- **Profile Page**

    - Profile page. Displays a user's profile information. Lets a user see their relevant profile information in a clean and simple way, and contains an update form that users can use to update their profile information.

![screenshot](documentation/features/sitepages/profile.png)


- **My Reservations Page**

    - My reservations page. Displays a formatted table populated with the user's upcoming court reservations. Users can easily see details of their reservations as well as links to a detail page of each reservation where it can be deleted if the user wishes.

![screenshot](documentation/features/sitepages/my-reservations.png)

- **Logout Page**

    - Logout Page. A simple page confirming that the user has logged out of their account. Displays a log in again button in case the user wishes to log back in.

![screenshot](documentation/features/sitepages/logout.png)

- **Reservation Page**

    - Court reservation page. Displays a form for users to reserve a court at the tennis club. The form is simple and easy to use, with only two steps, letting the user quickly and easily make bookings. 

![screenshot](documentation/features/sitepages/reservation-page.png)




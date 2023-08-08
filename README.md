# Sweet Chariot Singers

<p align="center">
  <!-- <img src="readme-images/website_mockup.png" alt="Mockup of how the website looks on desktop, laptop, tablet and mobile"/> -->
</p>

[Link to Website]

[GitHub Repo]


***

## About

<br>
Sweet Chariot Singers is a website built to publicise and administrate a new choir. The site enables users to learn about the choir, keep up to date with news and events, find out rehearsal venue and times and get to know the leadership team. 

Singers can sign up to join the choir using the online membership form, that organises a subscription monthly payment. Members can then have access to music the choir sings for them to print and practice.

***
<br>

## Index - Table of Contents

* [User Experience R&D](#user-experience-research-and-design)
    * [Strategy](#strategy)
    * [Scope](#Scope)
    * [Structure](#Structure)
    * [Skeleton](#Skeleton)
    * [Surface](#Surface)
* [Data Model](#Data-Model) 
* [Features](#Features)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits](#Credit)

<br>

***
<br>

## User Experience Research and Design

<br>

### User Requirements

Choir members of Sweet Chariot Singers need a hub to which they can go to get all the information and ethos relating to being part of the choir. They need to be able see what is going on and when, and have it linked to their social media. They need to know who is running what, and the roles they play. They need to be able to learn the music. Signing up for the choir needs to be a simple form containing all the information necessary for their profile, with a simple way of setting up monthly membership fee payments.

Other users who are not choir members will require a way of knowing when the choir is performing by signing up to a email list. This can create a followers list and enlarge the scope and reach of the choir in the community and beyond.

<br>

### Objective

The objective of the site is to meet each of these user requirements. Fundamentally, the site needs to evoke a friendly, trustworthy feel and be easy to use. The layout needs to be uncluttered and simple with clear action points for signing up, joining the choir and navigating to information.

<br>

### Design 

The design of the site considers four key user types and their requirements:

<details><summary><b>User Types</b></summary>
  <img src="#" alt="User Types; First time, Fan or Follower, Choir Member, Choir Admin"/>
</details><br>

#### First Time User
    A first time user will be attracted by the striking logo on the homepage. 

#### Fan or Follower


#### Choir Member


#### Choir Admin

This phase led to User Stories being drafted complete with Acceptance Criteria and initial Tasks for the development phase. User Stories have been added to GitHub [here](https://github.com/users/RickofManc/projects/4/views/2) and are being tracked through to completion. Due the deadline for MVP release some User Stories have been archived and will be assessed for the Product Backlog and the next release.


#### Strategic Opportunities

The chart below highlights the features roadmap assessed by importance versus viability/feasibility of development for the MVP (Minimal Viable Product). This analysis will ensure the features that will provide immediate user benefit will be development first.

<p align="center">
  <img src="readme-images/fresh-casts-features-roadmap.png" alt="Strategic Opportunities Roadmap"/>
</p>

<br>

Furthermore a MoSCoW assessment had been performed but omitted from the original version of the README given the opportunities versus feasibility above.

<p align="center">
  <img src="readme-images/MoSCoW_assessment.png" alt="MoSCoW Assessment"/>
</p>

<br>

### Scope

An agile approach of keeping the in scope features simple and aligned to the strategy for the MVP will be adopted. Below is a list of the leading features for the Fresh Casts MVP.


#### In Scope Features
* Create an accessible website that follows convention for sites built to inform.
* Conventionally the site will have a fixed Header, Navbar and Footer.
* Main Menu will be accessible through a hamburger icon.
* By default, the homepage will show the latest posts in ascending order.
* A clickable link will enable Fresh Casters to find out more information on the post.
* Podcasts will be able ot click through to listen to shows in their host site.
* A user account will provide access to Commenting, Liking, Posting.
* Fresh Casters will be able to edit their own posts.
* A 'Contact Us' page will enable Fresh Casters to get in touch with Site Admin.
* An Accessibility Statement will inform of how Fresh Casts cares about accessibility.
* The site will be responsive across differing devices, from mobile first design through to large +2300px wide screens supported.


#### Out of Scope Features - for future release
* Search and learn - Using keywords, Fresh Casters will be able to search and hone in their choices.
* Recent activity - Compiling users activity data from across the site into their profile page.
* Podcast downloading - enabling Fresh Casters to listen offline.
* Preferred app - allowing Fresh Casters to listen to a podcast in their favourite listening app.
* Fresh Casters will be supported with a page dedicated to FAQ's.
* Single Sign On (SSO) - Use social apps such as Google, Facebook and Twitter to sign-in.
* Connecting Fresh Casters - Provide chat service to allow the community to interact directly.

<br>

### Structure

This website will be structured with the following design considerations.

* A Hub and Spoke structure, where the main content will be the homepage hub, and spokes are the pages to find out more information on a post. The spokes will also house useful pages such as Sign-up, Contact Us, About Us etc.
* Each post will be displayed in a shortened list view for the homepage with just enough information to entice the user. The post image and title will be clickable to open in a new page with full post details.
* Users wishing to add a comment or like will be asked to first create a user account. Once a brief form has been completed and submitted, users will have immediate access to all features. 
* Having a user account will allow users to interact with the site, adding comments, likes and being able to post their own content.
* All site visitors will be able to contact Fresh Casts through a contact form available from the Main Menu or Footer. 
* All pages will be available to users consistently through either the Main Menu or Footer - this should ensure users are never two clicks away from where they would like to be.


[Lucid Spark](https://lucidspark.com/) has been used to illustrate the Hub and Spoke structure for Fresh Casts website. Pages and features will be available from a single click from the Hub. The final structure for the MVP may differ slightly as development progresses, and from user feedback and testing.


<details>
    <summary><b>Site Structure</b></summary>
    <p align="center">
        <img src="readme-images/fresh-casts-site-structure.png" alt="Fresh Casts Site Structure"/>
    </p>
</details><br>


### Skeleton

Key to the UX attributes is the speed and ease for which users can learn about new podcasts, or what fellow users think about a podcast. 

The 'Hub and Spoke' structure should provide users with content from their initial landing, and allowing their intrigue to click on a post and find out more, or refine the content by choosing one of five categories located conveniently in the NavBar Menu, Footer or by clicking a category within the posts listed on the homepage.

Aesthetically pages will be clean to promote the information, and allow users to flow between differing categories and expanding posts to learn more and add contribute. Convention from popular information based sites will be adopted so users feel at home and therefore capture their engagement within the first few seconds.


#### Wireframes

As part of this phase wireframes for mobile and desktop devices have been produced using [Balsamiq](https://balsamiq.com/wireframes/) (see image below - the wireframes are located within the project [Repo](wireframes)).

The website is responsive through differing screen widths being designed for mobile first to a max-width of 767px. Tablets are responsive from 768px through to 1023px, laptops from 1023-1440px, and desktops from 1440px upward. 

<details>
    <summary><b>Wireframes</b></summary>
    <p align="center">
        <img src="readme-images/fresh-casts-mobile-wireframes.png" alt="Fresh Casts wireframe for mobile devices" />
    </p>
</details><br>


### Surface 

In consideration that accessibility is a key design criteria, the visual language offers contrast using a simple colour palette, readable font and clear layout. Throughout the website this language has been applied consistently to promote intuitive behaviour with the most important links and information easily recognised.


#### Colour

This palette has been carefully selected to bring high contrasting colours to improve accessibility to visually impaired users. As the primary aim of the site is to inform, Black text on a White background is adopted throughout. The Teal based accents will be used to highlight buttons, points of reference or navigation and other key pieces of user information.

<details>
    <summary><b>Colour Palette</b></summary>
    <p align="center">
        <img src="readme-images/fresh-casts-colour-palette.png" alt="Fresh Casts Colour Palette"/>
    </p>
</details>
<br>


#### Logo

The logo has been selected from [Adobe Stock](https://stock.adobe.com/uk/contributor/208909039/2arm?load_type=author&prev_url=detail&asset_id=430392467). The design by **2arm** is being used under a  paid license with Adobe Stock. The design appealed as for it's clean design that identifies key components of podcasting; a microphone, projecting sound and listeners typically through headphones. I have applied Fresh Casts colour theme to the Vector using the free app [Photopea](https://www.photopea.com/).

<p align="center">
    <img src="readme-images/fresh-casts-b-and-g-logo_380px.png" alt="Fresh Casts Logo"/>
</p>
<br>

#### Fonts

**Roboto Flex and Roboto Condensed**

I've selected this popular [font family](https://fonts.google.com/share?selection.family=Roboto%20Condensed:ital,wght@0,400;0,700;1,400;1,700%7CRoboto%20Flex:opsz,wght@8..144,100;8..144,300;8..144,400;8..144,500;8..144,600;8..144,700) for its clean lines and legibility, being widely used on news and information based websites. It also offers a condensed style which can be used for larger text headers to offer some contrast to body text.

<p align="center">
    <img src="readme-images/fresh-casts-roboto-flex-font.png" alt="Fresh Casts Font"/>
</p>
<br>

***

<br>

## Data Model

As part of the project planning phase a high-level design of the site [structure](#Structure) has been designed to understand the main entities, and the relationship between these entities set within a Hub and Spoke design.
This led to understanding the next level down through mapping out the tables, columns and attributes required for the database. The initial draft in Excel has been mapped into a data schema below using [draw.io](https://www.draw.io/index.html) to help understand how the entities and data will relate across the site.


In consideration of the a requirement for the data to be searchable, and in time understand patterns and trends in user behaviour, an Object-Relational Database using MVT architecture has been selected. I've opted for a PostgreSQL DBMS (Database Management System) as it can support the aforementioned requirements, PostgreSQL can also support multiple programming languages and libraries that which will be used to build the Fresh Casts application.

The diagram below shows the entity relationships between a blog post and their 'comments'. The Post Model is used by the Comment Model to ensure the right blog post is being commented on. The diagram also highlights that one blog post can have many comments. 

The key component in this relationship is the user. I have used the default Django User Model for ease, and whilst this is not declared in the models.py file, I have included within the diagram for clarity. 

Equally one user can add many likes throughout the site, however this functionality is built within the Post Model itself so has not been declared within this class level diagram. 

There are five categories created within the Django Admin panel. These are displayed to the user as a dropdown field choice when adding a blog post.

The diagram highlights the following relationships:
* One blog post can have one author (User)
* One blog post can have one category
* One blog post can have many comments
* One blog post can have many likes 
* One user can add one log post like
* One user can add many comments to one blog post

The Contact App data model does not yet have a relationship with the Blog App, however I have included for awareness towards future development.

 
<p align="center">
    <img src="readme-images/fresh-casts-data-schema.png" alt="Data schema for Fresh Casts"/>
</p>
<br>



### Data Security

Specific steps have been taken to ensure the security of users data and the websites integrity. These are as follows;
* The use of an env.py file to store key variables for accessing secure environments i.e. Postgres Database.
* A gitignore file has been incorporated to ensure the env.py file is never committed to production. Therefore retaining the security of these key variables.
* Additionally, these variables are stored within the Config Variables in Heroku to ensure GitPod and Heroku can synchronise securely.
* Cross Site Request Forgery (CSRF) tokens have been applied to all HTML Forms. Their application provides protection from malicious attacks where users maybe performing certain actions or sending data when logged-in.
* Django's inbuilt User Authentication has been applied to several key areas to ensure only approved Users can Add, Comment, Like blog posts. A further layer of security has been applied to ensure the ability to Edit or Delete a blog post can only be performed by the User who has authored the blog post.


### Meta data

Meta data is included within the HTML head element to increase the traffic to the website. Additionally, site pages are titled appropriately as another method of informing users of their location.


***

<br>

## Technologies


### Languages

* HTML5
* CSS3
* Python


### Frameworks & Libraries

* [Django 3.2](https://docs.djangoproject.com/en/4.0/releases/3.2/) has been adopted as more preferable over the newest beta Django 4 to rapidly and securely develop this application.
* [ElephantSQL](https://elephantsql.com/) as a free service providing a configured and optimized PostgreSQL database.
* [dj_database_url](https://pypi.org/project/dj-database-url/) library used to allow Database urls to connect to the Postgres database.
* [Psycopg2](https://pypi.org/project/psycopg2/) supports the connection to the Postgres database.
* [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku.
* [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) used for addressing user authentication, registration and account management.
* [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used to build responsive web pages.
* [Summernote](https://summernote.org/) provides WYSIWYG editing of blog post descriptions on the admin side. An option was considered to allow users to edit the styles of their posts, however in practice this led to poor accessibility with differing font sizes and colours used.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) is simplifying rendering on several forms.
* [Cloudinary](https://cloudinary.com/products/programmable_media) has been used to store the images uploaded by users for their blog posts.


### Software & Web Applications

* [Balsamiq](https://balsamiq.com/) to build wireframes in the Skelton phase.
* [Lucid Spark](https://lucidspark.com/) for the high-level site structure.
* [draw.io](https://www.draw.io/index.html) to diagram data schema/model.
* [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) Used as the primary method for developing the sites responsiveness and identifying bugs.
* [GitPod](https://gitpod.io/) used for the IDE and [GitHub](https://github.com/) as a hosting repository. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking them on a Kanban board.
* [Heroku](https://dashboard.heroku.com/) to host the Fresh Casts website, including database.
* [Wave](https://wave.webaim.org/) - Accessibility Testing to ensure content is readable for all users.
* [HTML Validator](https://validator.w3.org/) validates HMTL code.
* [W3 CSS Validator](https://jigsaw.w3.org/css-validator/validator) validates CSS code.
* [CI Python Linter for Python](https://pep8ci.herokuapp.com/) validates Python code.
* [JSHint](https://jshint.com/) validates JavaScript code.
* [Code Beautify](https://codebeautify.org/) validates the code formatting for browser reading.
* [LambdaTest](https://www.lambdatest.com/) for cross browser testing, specifically macOS Safari and Opera.


***

<br>

## Features


### Current Features

- __Homepage__
    
    All site visitors land with content visible. Blog posts are sorted in latest added date first and paginate with six per page.

<p align="center">
    <img src="readme-images/F05F08_Homepage.png" alt="Homepage features"/>
</p>
<br>


- __NavBar with Collapsing Menu__

    Utilising Bootstraps NavBar, users have three distinct sections to reach features.
    The left hand side uses the conventional hamburger menu icon to reveal a menu that offers access to user features, blog post categories and other useful pieces of information.
    Centrally the Fresh Casts name and logo takes a leading role to convey the brand as well as acting as a link back to the homepage.
    Whilst on the right hand side the resource profile icon provides a short menu with access to user features.
    The menu collapses either with a user choosing a menu item, by clicking the menu button or after a short time period.
    Features available to users within the menus depend on their login status e.g. if a user is logged in they will see options to Add Post and Edit Profile.

<p align="center">
    <img src="readme-images/F01F02F03_Header_NavMenu.png" alt="NavBar features"/>
</p>
<br>


- __Fixed Footer__

    Similar to the NavBar Main Menu, users have three distinct sections to reach features from the Footer.

<p align="center">
    <img src="readme-images/F04_Footer.png" alt="Footer features"/>
</p>
<br>


- __Create a Blog Post__

    Registered users have the ability to add to Fresh Casts content through creating a blog post. A simple form asks for basic details, including a link to the hosting URL. On form submission, users are informed the post will be reviewed by Site Admin and hopefully published if deemed appropriate within 24 hours.
    Users can also upload an image to support the post, if an image is not uploaded at the time, the Fresh Casts logo will be displayed. Users can update the post with an image once live. This feature currently works best on a desktop application, with a future feature using a podcast API to retrieve the URL and featured image automatically to the Form using search functionality.

<p align="center">
    <img src="readme-images/F41_Create_Posts.png" alt="Create Blog Post Feature"/>
</p>
<br>


- __Read a Blog Post__

    When a user chooses a blog post from the main homepage list view or category page, they are taken through to a single page that displays all posted details and further features.
    All site visitors will be able to read about the shared podcast, and use the 'Listen' button to hear/see the show from the host site. Development work is going on to enable users to listen to the show within the site page.
    If users are registered and logged in they will be able to add a like or comment in the conventional manner, a counter provides an indication on how favoured a post is. If users have posted the item further options to Edit or Delete their post will be visible.

<p align="center">
    <img src="readme-images/F09F17F14_Post_Details.png" alt="Blog Post Features"/>
</p>
<br>


- __Commenting__

    A key feature for Fresh Casts is enabling the community to share their views with one another. All site visitors will be able to read a blog posts comments just below the main post content. Registered users will be able to add comments to kick start, or join in a conversation about a particular podcast.

<p align="center">
    <img src="readme-images/F14_Comments.png" alt="Blog Post Commenting Feature"/>
</p>
<br>


- __Update a Blog Post__

    Those users who have contributed by creating a blog post will have control over the content should they wish to make changes. This feature will only be visible to them on the Post in Detail page as an 'Edit' button. A simple form awaits with a Submit or Cancel button (should they have navigated there in error).

<p align="center">
    <img src="readme-images/F21_Update_Post.png" alt="Update Blog Post Feature"/>
</p>
<br>


- __Delete a Blog Post__

    Those users who have contributed by creating a blog post will have control over whether to keep the post active or not. This feature will only be visible to them on the Post in Detail page as a 'Delete' button. The user will be asked on a new page to confirm they wish to remove the post in knowledge that it cannot be retrieved. There is a Cancel button (should they have navigated there in error).

<p align="center">
    <img src="readme-images/F23_Delete_Post.png" alt="Delete Blog Post Feature"/>
</p>
<br>


- __Update Profile__

    In addition to being able to update content they have posted, registered users will be able to update key account details i.e. Username, Email Address, First and Last Name. This option will only be visible in the Main Menus and Footer when a user is logged in. The next release will allow users to delete their profile. As a temporary solution, users can use the 'Contact Us' form to request this action.
    Passwords can also be updated - due to the sensitive and secure nature of this action, users wishing to update their password are taken through to another screen.

<p align="center">
    <img src="readme-images/Edit_Profile.png" alt="Edit Profile Feature"/>
</p>
<br>


- __Contact Us__

    An essential feature is a method for Fresh Casters to contact the team. This can be performed with a direct email or by submitting a short form available from the Main Menu or Footer. The form requests some basic information and allows users to describe the reason for contact.
    Once received, the team can process the form in the backend and utilise a checkbox for status to mark when a response has been sent.

<p align="center">
    <img src="readme-images/F32_Contact_Page.png" alt="Contact Fresh Casts Feature"/>
</p>
<br>


### Future Features

Features that will be added to the backlog for future releases are as follows:

* Search for blog posts through a search bar located in the NavBar. 
* Allow registered users to like other users comments.
* Enable registered users to delete their own posts.
* Provide an FAQ page to support users understanding and navigation of Fresh Cast features.
* Integrate a podcast API that will ease the adding of blog posts through automatically generated show images, URL's etc.
* Provide options for users to share blog posts on their socials.
* Enable site visitors to download a podcast to listen offline, or play in their preferred app.
* Allow registered users to update their own comments.
* Build a user profile page that informs of recent activity, posts viewed, likes and comments.
* Integrate a chat function that allows registered users to connect and discuss the post when listening at the same time, or just for general conversation.


***

<br>


## Testing

Following a largely manual process for development and deployment, I have chosen to primarily perform manual testing.
Testing procedures will ensure the deployed site aligns to the site in development through covering the following aspects:

* User stories - validate that the user requirements have been delivered for the MVP release.
* User Acceptance Testing (UAT) - ensuring the website is meeting real world expectations.
* Page validation - check all features and links from across the site are working as designed and developed.
* Responsiveness - ensuring each page is responsive through the three media queries covering mobiles, tablets-laptops and desktop monitors.
* Accessibility - each page is tested for compliance with accessibility guidelines using the WAVE online assessment tool.
* Performance - using Chrome's developer tool 'Lighthouse Testing' pages are tested for performance, best-practice, SEO and accessibility.
* Browser - pages are tested for layout, features and general performance across Chrome, Firefox, Edge, Safari and Opera.
* Device - manual testing will be performed on an iOS and Android mobile, Tablet, Laptop and Desktop to ensure all users have a positive experience no matter which device or browser they prefer to use. 
* Code validation - ensuring the code base is validated using industry standard tools for HTML, CSS and Python code.

As the size of results tables as summaries is quite large, I've opted to document this in a separate file.

[Navigate to TESTING.md](TESTING.md)

***

<br>

## Deployment

This project was deployed using the steps below with version releasing active. Please do not make any changes to files within this repository as any changes pushed to the main branch will be automatically reflected on the live website. Instead, please follow the steps below which guide you to forking the website where changes can be made without impact to the live website. Thanks!


### Fork and Deploy Locally with GitHub

<details>
    <summary></summary>

To fork this website to either propose changes or to use as an idea for another website, follow these steps:
1. If you haven't yet, you should first set up Git. Don't forget to set up authentication to GitHub.com from Git as well.
1. Navigate to the [Fresh Casts](https://github.com/RickofManc/fresh-casts).
1. Click the 'Fork' button on the upper right part of the page. It's in between 'Watch' and 'Star'.
1. You will now have a fork of the Fresh Casts repository added to your GitHub profile. Navigate to your own profile and find the forked repository to add the required files.
1. Above the list of forked files click the 'Code' button.
1. A drop-down menu will appear providing a choice of cloning options. Select the one which is applicable to your setup.
</br>
Further details on completing the last step can be found on GitHub's [Fork a Repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo) page

To deploy locally with GitHub, follow these steps:
1. Log into your GitHub repository, create a GitHub account if necessary
1. Click 'Settings' in the main Repository menu
1. Click 'Pages' from the left-hand side navigation menu
1. Within the Source section, click the "Branch" button and change from 'None' to 'Main'
1. The page should automatically refresh with a url displayed
1. Test the link by clicking on the url
1. From this point you can push code to this page using the following steps from with GitPod;
    1. With the application open, open the command line terminal (CLI)
    1. Stage any changes using the command 'git add .' or by specifying the file with changes i.e 'git add settings.py'
    1. Commit the changes to GitHub by adding a commit message describing the changes i.e. 'git commit -m "Update docbook dependency and generate epub"
    1. Finally add the command 'git push' which will push all the code to GitHub. You can view the deployed code using the url generated within the steps above.
    1. Additionally if you would like to run the application locally pre/post any changes, from the terminal type 'python3 manage.py runserver'.
    1. A dialog box should open asking you to open port 8000, click 'Open' and navigate to the opened tab/window which should allow you to view the running application.
    1. If the dialog box does not automatically appear, find the 'Remote Explorer' section of the left hand navbar within GitPod and click on the port '8000' and the internet/globe icon to the right which should open the running application.
</details>


### PostgreSQL Database

<details>
    <summary></summary>

ElephantSQL replaced the originally selected free Heroku add-on PostgreSQL database due to the Heroku version becoming a chargeable service.
Post MVP release I followed steps provided by the Code Institute to migrate the database from the Heroku version to Elephant. Dependant on your circumstances you may wish to use Heroku, Elephant or another service for your database. 

1. If using Elephant, navigate to elephantsql.com and click 'Get a managed database today'. When presented with options for differing plans, I chose the free 'Tiny Turtle' plan.
1. Select “Log in with GitHub” and authorize ElephantSQL with your selected GitHub account.
1. In the Create new team form:
    * Add a team name (your own name is fine).
    * Read and agree to the Terms of Service.
    * Select Yes for GDPR.
    * Provide your email address.
    * Click “Create Team”.
1. Your account should now be created.
1. Now you will need to create your database. Navigate to your elephantsql.com dashboard, and click "Create New Instance".
1. Set up your plan:
    * Give your plan a Name (this is commonly the name of the project).
    * Select the Tiny Turtle (Free) plan.
    * You can leave the Tags field blank.
1. Select a data center near you.
1. Then click "Review".
1. Check your details are correct and then click "Create Instance".
1. Return to the ElephantSQL dashboard and click on the database instance name for this project.
1. You will return to this projects dashboard as part of the steps to 'Deploy with Heroku' as you will need the DATABASE_URL.
</details>


### Deploy with Heroku

<details>
    <summary></summary>

1. Log in to Heroku at https://heroku.com - create an account if needed.
1. From the Heroku dashboard, click the Create new app button. For a new account an icon will be visible on screen to allow you to Create an app, otherwise a link to this function is located under the New dropdown menu at the top right of the screen.
1. On the Create New App page, enter a unique name for the application and select region. Then click Create app.
1. On the Application Configuration page for the new app, click on the Resources tab.
1. Next, click on Settings on the Application Configuration page and click on "Reveal Config Vars".
1. Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1, and click Add to save it. Remove this when releasing for Production.
1. Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols, and click Add to save it.
1. Add a new Config Var called DATABASE_URL and paste in the value for your ElephantSQL database, and click Add to save it.
1. The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

        DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

        SECRET_KEY = os.environ.get('SECRET_KEY')

1. In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate
1. Update the requirements.txt file with all necessary supporting files by entering the command : pip freeze > requirements.txt
1. Commit and push any local changes to GitHub.
1. In order to be able to run the application on localhost, add SECRET_KEY and DATABASE_URL and their values to env.py

Connect GitHub Repo to Heroku App

1. Navigate to Application Configuration page for the application on Heroku and click on the Deploy tab.
1. Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter and search for the required repository, then click on Connect to link them up..
1. Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - I chose the latter for the initial deployment to watch the build and then opted for Automatic Deployment.
1. The application can be run from the Application Configuration page by clicking on the Open App button.
1. Each time you push code from your GitHub Repo it will be automatically reflected in your Heroku App.

The url for this website can be found here https://freshcasts.herokuapp.com/
</details>


### Pre Production Deployment

<details>
    <summary></summary>

When you are ready to move to production, the following steps must be taken to ensure your site works correctly and is secure.

In GitPod:
1. Set DEBUG flag to False in settings.py
1. Check the following line exists in settings.py to enable Summernote to work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'
1. Update the requirements.txt file with all necessary supporting files by entering the command : pip freeze > requirements.txt
1. Commit and push code to GitHub
In the Heroku App:
1. Settings > Config Vars : Delete environment variable : DISABLE_COLLECTSTATIC
1. Deploy : Click on deploy branch
</details>
    

***

<br>

## Credit


### Acknowledgements

* Mentor Brian Macharia for continuing to guide and feedback throughout the projects lifecycle, especially on how to improve UX and my code.


### Code

Support with how to develop ideas into code also came from various online resources:

* In general the coding and testing has relied on the Code Institutes walkthrough projects "Hello Django" and "I Think Therefore I Blog" as part of their Full Stack Frameworks module.
* [W3schools](https://www.w3schools.com/) as a source of 'How to...' information throughout the build primarily on Django.
* [Django Project Docs](https://docs.djangoproject.com/en/4.0/ref/models/fields/) were referenced many times, especially in how to reference fields correctly across differing py files.
* [Codemy](https://codemy.com/) provided insight on blog building in Django.
* [GeekforGeeks](https://www.geeksforgeeks.org/urlfield-django-models) for using dynamic URL fields in html tags.
* [Code Grepper](https://www.codegrepper.com/code-examples/whatever/bootstrap+card+with+image+on+left+and+text+on+right) guided me on how to align the post image to the left of text for the homepage list view.
* [Jordan Raychev at Medium](https://medium.com/geekculture/django-tutorial-building-a-portfolio-application-contact-application-ac128d7b7b89) who provided an article on building a Contact app.
* [Wolterskluwer](https://www.wolterskluwer.com/en/solutions/kluwerlawinternational/user-agreement) for information on Blog User Agreements.
* [John Harbison](http://johnharbison.net/make-a-form-a-cancel-button) provided guidance on creating a Cancel Button as an input tag within a Form.
* [StackOverflow](https://stackoverflow.com/questions/18407832/how-to-create-a-html-cancel-button-that-redirects-to-a-url) page that provided a fix for a JavaScript error that appeared against the code of my cancel buttons.
* [Stack Overflow](https://stackoverflow.com/questions/10615872/bootstrap-align-input-with-button) how to align an Input tag as a button using Bootstrap.
* [Stack Overflow](https://stackoverflow.com/questions/48356012/how-to-close-the-first-menu-collapse-when-the-second-one-is-open) provided the code to close an open nav menu before the other one opens.
*[Stack Overflow](https://stackoverflow.com/questions/65761250/pylint-django-raising-error-about-django-not-being-configured-when-thats-not-th#:~:text=Finding%20foreign%2Dkey%20relationships%20from,settings%60%20.) helped with configuring pylint plugin which in turn removed an error from all python files (Bug 14).
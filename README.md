# Chatters

**[Live site](https://cipp4-eryk.herokuapp.com/)**

---

<span id="top"></span>

## Index

- <a href="#context">Context</a>
- <a href="#ux">UX</a>
  - <a href="#ux-stories">User stories</a>
  - <a href="#ux-strategy">Strategy</a>
  - <a href="#ux-scope">Scope</a>
  - <a href="#ux-structure">Structure</a>
  - <a href="#ux-wireframes">Wireframes</a>
  - <a href="#ux-design">Design</a>
- <a href="#features">Features</a>
  - <a href="#features-design">Design Features</a>
  - <a href="#features-existing">Existing Features</a>
  - <a href="#features-future">Still to implement</a>
- <a href="#technologies">Technologies Used</a>
- <a href="#testing">Testing</a>
  - <a href="#testing-manual">User Stories</a>
  - <a href="#testing-manual">Manual</a>
  - <a href="#testing-unresolved">Unresolved issues</a>
  - <a href="#testing-bugs">Known bugs</a>
- <a href="#deployment">Deployment</a>
- <a href="#credits">Credits</a>

---

<span id="context"></span>

# **Context**

Chatters, a website where you can chat with other people about anything and everything. It is a community platform in the form of a blog where users can
interact with other users posts and share their opinions. Users can create an account where they can edit their profile image, their bio and other
settings.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="ux"></span>

# **UX**

<span id="ux-stories"></span>

## **User stories**

- As a **User** I want to be able to browse all posts and sort them by their tags.
- As a **User** I want to be able to see the amount of votes and comments on each post.
- As a **User** I want to be able to preview authors profile.
- As a **User** I want to be able to see the time of the posts and comments.
- As a **User** I want to be able to comment on posts and have the option to edit or delete them.
- As a **User** I want to be able to add posts with different tags and get option to publish or draft them.
- As a **User** I want to be able to react to users posts by upvoting or downvoting them.
- As a **User** I want to be able to edit my profile and upload an avatar.
- As a **User** I want to be able to search through all posts.

- As a **Admin** I want to be able to control all of user settings on one page.


<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

## **Strategy**

<span id="ux-strategy"></span>

### **Site Aims**

My main aim for the website was to let user to be able to save their posts for future reference as well as interacting with other users. I wanted to create a community where people can quickly access any type of topics they are interested in be it gaming or world news.

The website needs to let user to:

- Sort posts to their needs.
- Create and set up their account.
- Create posts with either published or draft status.
- Upvote or downvote each post.

### **Opportunities**

With the user stories in mind, I have made a table below to narrow down and prioritize the scope of intended strategy.

![Opportunities](docs/opportunities.png)

## **Scope**

<span id="ux-scope"></span>

A scope was defined to identify what was needed to be done in order to match the strategy outlined before.

- Content Requirements
  - The UX must address
    - A list of posts
    - Posts being sorted into categories (tags)
    - A list of users comments on posts
  - The UX should accommodate
    - Easy navigation
    - Ability to vote and comment

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

## **Structure**

<span id="ux-structure"></span>

I've created a flow charts to help me visualize what the navigation should feel like. I have also made one with the database scheme to guide me throughout the site progression.

![Structure](docs/site-structure.png)
![Database](docs/database.png)

As you can see in aboves images, my database scheme ended up quite accurate but there is one field currently not being used but will be in future implementations. The field I am talking about is in Post model and is **Updated_On**. I have plans to also add one for comments to be able to preview if the post was edited.

## **Wireframes**

<span id="ux-wireframes"></span>

The wireframes were successfully converted into a live functioning website across all devices.

The full suite of wireframes for **desktop**, **tablet** and **mobile** devices, can be accessed [here](wireframes/).

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

## **Design**

<span id="ux-design"></span>

### **Colour Scheme**

After looking through different reddits and my preference of all websites I browse, I concluded that the best color scheme would be a simple **Dark Theme**. With plans in feature to implement a switch for light theme I though this can be a good idea. The below is the colours I have used the most.

![Coolors](docs/coolors.png)

### **Typography**

For fonts I decided to go with what reddit is using. The fonts are as follows, Verdana, Arial, Helvetica and Sans-serif. I think it gives site nice and clear look and ease of readability.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

<span id="features"></span>
# Features

## Design Features

<span id="features-design"></span>

Every page consits of top navigation bar and a side column with consitent and responsive design.
- The top navigation bar contains a site name which brings user back to index page. A search bar to search throughout all published posts and account management buttons such as log in, edit account and log out.
- The side column contains buttons which bring users to their published posts or drafts as well as a button to let them add posts.

## Existing Features

<span id="features-existing"></span>

### **Sitewide**

**Navigation Bar**
- The navigation bar consists of a search input and button.
- It also contains of a sign up and log in button if user is not logged in which changes afterwards to an icon which gives the user option of either login out or editing their account.

![Search](docs/features/search.png)
![Login Register Buttons](docs/features/login-register-account.png)
![Account Icon](docs/features/manage-account.png)

**Side Column Menu**
- The side column consists of buttons which let users add posts and view their either published posts or drafts.

![Side Column](docs/features/side-column.png)

### **Index**
- The index page has a list of posts sorted by date and the option to sort posts by tags to their needs.
- The post card has options for users if they are the authors as per image. They can delete or edit them.
- As per options on each post, users can upvote or downvote each post to give visible feedback and the amount of comments are also visible.
- The post **tag**, the author and the date is given in each post.

![Index Post](docs/features/post.png)
![Sort Bar](docs/features/sort-bar.png)

### **Post**
- The post has the same options as stated above in **Index** section.
- The additional features are the ability for users to comment and preview other users comments.
- The full post length is also visible in comparison to **Index** view.
- Add post page contains a simple form layout with necessary fields such as title, tag, content and status.
- The edit post page has the same form layout as previously mentioned add post page with the fields being pre filled.
- The author of the post has ability to delete comments.

![Main Post](docs/features/main-post.png)
![Add Post](docs/features/add-post.png)

### **User Profile**
- The user can edit their profile fields such as their first and last name, their bio and their image.
- Users can access other users profile by pressing on their names in either post author and comment name.
- User profile preview page does not show fields that user has blank in their settings.

![Edit Profile](docs/features/edit-profile.png)
![User Profile](docs/features/user-profile.png)

### **Other**
- The users published post and draft sections are comparable to **Index** page. Only difference is they can not sort them by tags as of now.
- The delete post feature is a simple page with notifying the user before their decision has been made.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

## **Features still to implement**

<span id="features-future"></span>

- The ability to edit your own passwords within user settings page.
- The option to upload images into posts and comments and to be able to customize your posts more.
- Add more sorting options such as sort by amount of votes or the amount of comments.
- Add a 'light theme' styling as a button to switch in between.

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

# Technologies

<span id="technologies"></span>

### **Main Languages Used**
- HTML5
- CSS
- Python

### **Frameworks, Libraries and Programs Used**
- Django
- Bootstrap
- Cloudinary
- Crispy Forms
- GitHub
- GitPod

<div align="right"><a style="text-align:right" href="#top">Go to index :arrow_double_up:</a></div>

# Testing

## User Stories

- As a **User** I want to be able to browse all posts and sort them by their tags.
  - The first thing you see are all posts sorted by the date. There is a button on top of page which gives the option to sort throughout the specific tags.
- As a **User** I want to be able to see the amount of votes and comments on each post.
  - On each post card there is a column on left side which shows the exact amount of votes. There is an icon and amount of comments on each post card also with the comments being only visible on the actual post link.
- As a **User** I want to be able to preview authors profile.
  - Users profile can be accessed by either pressing on the name in comment section or the post author.
- As a **User** I want to be able to see the time of the posts and comments.
  - 








- As a **User** I want to be able to comment on posts and have the option to edit or delete them.
- As a **User** I want to be able to add posts with different tags and get option to publish or draft them.
- As a **User** I want to be able to react to users posts by upvoting or downvoting them.
- As a **User** I want to be able to edit my profile and upload an avatar.
- As a **User** I want to be able to search through all posts.

- As a **Admin** I want to be able to control all of user settings on one page.
# Surfshop
Surfshop is an online store where users can buy water sports clothing and equipment. There is many online stores that provide users with the opportunity to buy water sports clothing or equipment but there is very few where users can buy both in one place. Surfshop also provides store admins with the ability to add, edit  and delete products with ease.

## UX
### User Goals
The majority of user will into the following two categories:
* A user looking to purchase water sports gear.
* A store admin that wants to add, edit or remove products

### User Stories
1. As a shopper, I want to view a list of all products to select an item to purchase.
2. As a shopper, I want to be able to view single product details to see the price, product rating and available sizes.
3. As a shopper, I want to be able to view the total of my purchase at any time to avoid spending too much.
4. As a site user, I want to be able to register an account so that i can have a personal account and be to view my profile.
5. As a site user, I want to be able to easliy login or out so that i can access my personal account information.
6.  As a site user, I want to be able to receive an email confirmation after registering so that i can verify my account registration was successful.
7. As a site user, I want to have a personalized user profile to view my personal order history and confirmations and save my payment information.
8. As a shopper, I want to be able to add items to my wishlist so I can come back and purchase them in the future.
9. As a shopper, I want to be able seach for a product by name or description so that i can find a specific product id like to purchase.
10. As a shopper, I want to be able to see what ive searched for and the number of results so that i can quickly decide whether the product i want is available.
11. As a shopper, I want to be able to select the size and quantity of a product when purchasing it so that i can make sure i don't accidentally select the wrong product quantity or size.
12. As a shopper, I want to be able to view items in my bag to be purchased so that i can identify the total cost of my purchase and all items i will receive.
13. As a shopper, I want to be able to adjust the quantity of items in my bag so that i can easliy make changes to my purchase before checkout.
14. As a shopper, I want to be able to feel my personal information is safe and secure so that i can confidently provide the needed information to make a purchase.
15. As a shopper, I want to be able to enter my payment information so that i can checkout quickly with no hassle.
16. As a shopper, I want to be able to view an order confirmation after checkout so that i can verify that I haven't made any mistakes.
17. As a shopper, I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my records.
18. As a shopper, I want to be able to get in contact with store owners if I have an issue with one of my orders.
19. As a store owner, I want to be able to add a product so that i can add new items to my store.
20. As a store owner, I want to be able edit/update a product so that i can change product prices, descriptions, images and other product criteria.
21. As a store owner, I want to be able to delete a product so that i can remove items that are no longer for sale.

### Wirefames
[here](https://github.com/joe6894/surfshop/tree/master/wireframes) are my designs for the site.

The wireframes were made using [whimsical](https://whimsical.com/)

I made some changes from the initial design, they are:
* I added a contact page.
* I reduced the amount of brands available on the home page.

## Features
* Navigation menu: Allows users to navigate to any page on the site.
* Search bar: Allows users to search all products on the site.
* User registration: Allows users to sign up to the site by providing a valid email and secure password.
* User authentication: Users can log in by providing their email and password.
* Best selling: Allows users to view the best selling products on the home page.
* Safety equipment area: brings users to all the safety equipment available on the site.
* Top brands: Allows users to view products by the top brands available on the site.
* Water equipment: Allows users to view all the surfboards, wakeboards and kayaks available on the site.
* Contact page: Allows users to get in contact with site owners if they have any issues.
* Bag: Allows users to view items in their bag and also remove unwanted items.
* Checkout: Users can purchase items in their bag. If users are authenticated their delivery information will be prefilled in the form.
* Profile: Allows users to store their payment information if registered.
* Wishlist: Allows users to store items they may want to purchase in the future.
* Product Management: Allows store owners to add, edit and delete products from the site.

### Features left to implement
* 404.html page would allow users to navigate back to home page if there was an error.
* Gallery: Would allow users to images or videos of them partaking in water sports.
* Forum: Would allow users to discuss news and locations related to water sports.
* Weather app: Would inform users on what conditions are like for surfing and other sport activities
* Rating: Would give users the ability to rate products.

## Technologies Used
 
 * [HTML5](https://en.wikipedia.org/wiki/HTML5)
	 * The project uses html5 to provide structure and content to the site.
 * [CSS3](https://en.wikipedia.org/wiki/CSS)
	 * Used to style the site.
 * [Javascript](https://www.javascript.com/)
	 * Used javascript for the interactive elements on the site.
 * [Python](https://www.python.org/)
	 * Used to run the application.
 * [Bootstrap](https://getbootstrap.com/)
	 * Used for layout and responsiveness.
 * [Fontawesome](https://fontawesome.com/)
	 * Used for the icons on the site.
 * [Django](https://www.djangoproject.com/)
	 * Used as the framework for the site.
 * [Amazon s3](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Categories=categories%23storage&trk=ps_a134p000006gAELAA2&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_IE&sc_publisher=Google&sc_category=Storage&sc_country=IE&sc_geo=EMEA&sc_outcome=acq&sc_detail=amazon%20s3&sc_content=S3_e&sc_matchtype=e&sc_segment=474686644518&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Storage|S3|IE|EN|Text&s_kwcid=AL!4422!3!474686644518!e!!g!!amazon%20s3&ef_id=CjwKCAiA57D_BRAZEiwAZcfCxeGOWec8LCYEkFw716DO6_94v8Q4OnA0x8ed2mZHFV8bZ3bf2QDmzBoCb7gQAvD_BwE:G:s&s_kwcid=AL!4422!3!474686644518!e!!g!!amazon%20s3)
	 * Used to store static and media files.
 * [Stripe](https://stripe.com/en-ie)
	 * Used for checkout payments.
 * [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
	 * Used for authentication on the site.
* [Git](https://git-scm.com/)
	* Used for version control.
* [Github](https://github.com/)
	* Used to host the repository.
* [Heroku](https://www.heroku.com/home)
	* Used to host the site.
* [EmailJS](https://www.emailjs.com/)
	* Used to send emails on the site.

## Testing
### Browser
I tested the website on three different browsers to see if the application works and looks like it should.
| Browser               | Microsoft Edge | Google Chrome | Firefox |
|-----------------------|----------------|---------------|---------|
| index.html            | pass           | pass          | pass    |
| products.html         | pass           | pass          | pass    |
| Product_details.html  | pass           | pass          | pass    |
| add_product.html      | pass           | pass          | pass    |
| edit_product.html     | pass           | pass          | pass    |
| bag.html              | pass           | pass          | pass    |
| checkout.html         | pass           | pass          | pass    |
| checkout_success.html | pass           | pass          | pass    |
| profiles.html         | pass           | pass          | pass    |
| wishlist.html         | pass           | pass          | pass    |
| logout.html           | pass           | pass          | pass    |
| login.html            | pass           | pass          | pass    |
| register.html         | pass           | pass          | pass    |

### Device Sizes
To test the site on different devices I used all the sizes on google developer tools to test its appearance and its responsiveness.

| Device            | index.html | products.html | product_detail.html | add_product.html | edit_product.html | bag.html | checkout.html | checkout_success.html | profile.html | wishlist.html | logout.html | login.html | register.html |
|-------------------|------------|---------------|---------------------|------------------|-------------------|----------|---------------|-----------------------|--------------|---------------|-------------|------------|---------------|
| Moto G4           | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Galaxy S5         | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Pixel 2           | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Pixel 2 XL        | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Iphone 5/SE       | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Iphone 6/7/8      | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Iphone 6/7/8 plus | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Iphone X          | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Ipad              | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Ipad Pro          | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Surface Duo       | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |
| Galaxy Fold       | pass       | pass          | pass                | pass             | pass              | pass     | pass          | pass                  | pass         | pass          | pass        | pass       | pass          |

### Online Validation
#### CSS3
| File         | Valid |
|--------------|-------|
| base.css     | pass  |
| checout.css  | pass  |
| profiles.css | pass  |

#### Javascript 
| File              | Valid |
|-------------------|-------|
| CountryField.js   | pass  |
| stripe_element.js | pass  |

#### HTML5
| File                  | Valid |
|-----------------------|-------|
| index.html            | pass  |
| products.html         | pass  |
| product_details.html  | pass  |
| add_product.html      | pass  |
| edit_product.html     | pass  |
| bag.html              | pass  |
| checkout.html         | pass  |
| checkout_success.html | pass  |
| profile.html          | pass  |
| wishlist.html         | pass  |
| logout.html           | pass  |
| login.html            | pass  |
| register.html         | pass  |

#### Python

| App         | Bag  |
|-------------|------|
| contexts.py | pass |
| models.py   | pass |
| urls.py     | pass |
| views.py    | pass |

| App       | contact |
|-----------|---------|
| admin.py  | pass    |
| models.py | pass    |
| forms.py  | pass    |
| urls.py   | pass    |
| views.py  | pass    |
| apps.py   | pass    |

| App       | Home |
|-----------|---------|
| apps.py   | pass    |
| models.py | pass    |
| views.py  | pass    |
| urls.py   | pass    |

| App       | profiles |
|-----------|----------|
| admin.py  | pass     |
| forms.py  | pass     |
| models.py | pass     |
| urls.py   | pass     |
| views.py  | pass     |

| App                | checkout |
|--------------------|----------|
| admin.py           | pass     |
| forms.py           | pass     |
| models.py          | pass     |
| signals.py         | pass     |
| urls.py            | pass     |
| views.py           | pass     |
| webhook_handler.py | pass     |
| webhooks.py        | pass     |

| App        | products |
|------------|----------|
| admin.py   | pass     |
| apps.py    | pass     |
| forms.py   | pass     |
| models.py  | pass     |
| urls.py    | pass     |
| views.py   | pass     |
| widgets.py | pass     |

| App       | wishlist |
|-----------|----------|
| admin.py  | pass     |
| models.py | pass     |
| urls.py   | pass     |
| views.py  | pass     |

| App         | surfshop |
|-------------|----------|
| settings.py | pass     |
| urls.py     | pass     |

### User Story Tests
* View list of products:
	* Go to the products page
	* All products are available
* View the details of a product:
	* When on products page click on a product.
	* All the details for that product are available.
* View the total of a purchase:
	* When on a products detail page click add to bag button.
	* Total price updates.
* Create an account to view profile:
	* Click on my account button.
	* Click register.
	* Enter required details.
	* Go to email address to verify email.
	* Click confirm.
	* Click on profile 
	* User can view their profile.
* Login to an account to view profile:
	* Click the my account button
	* Provide login details
	* Click on my profile
	* User can view their profile.
* Receive a confirmation email when registering:
	* Click on the my account button.
	* Click register.
	* Enter required details.
	* Go to email address
* Personalized profile with order history:
	* When registered complete an order.
	* Click the profile button in the my account Dropdown.
	* Click my profile.
	* Order History displayed.
* Sort available products by price, rating and alphabetically:
	*   Navigate to products page.
	* On products page click the 'sort by' dropdown.
	* Click the desired filter.
* Add items to personal wishlist: 
	* When logged in navigate to products page.
	* Click on a product.
	* Click on 'add to wishlist' button.
	* Click my account dropdown.
	* Click on wishlist.
	* Items are displayed.
* Search products by name or description:
	* Type surf in search bar.
	* Click the search button.
	* Returns items with surf in name or description.
* See what I have Searched for:
	* Type surf into search bar.
	* Click the search button.
	* To the left of the products page number of items and search term are displayed.
* Select size and quantity of item: 
	* On products detail page click the size of product from sizes dropdown.
	* Click the plus or minus to increase or decrease quantity.
* View items in the bag: 
	* Add item to bag.
	* Click shopping bag icon in top right.
	* Subtotal is displayed.
* Adjust quantity of items in my bag:
	* Add item to bag.
	* Click the bag icon in the top right.
	* Click remove item button to remove item 
	* Click the minus to decrease quantity and plus to increase quantity
	* Click update to change quantity.
* View an order confirmation after checkout:
	* Add items to bag.
	* Go to checkout.
	* Fill out delivery info and payment details.
	* Click the complete order button.
	* User is brought to checkout success that displays an order confirmation.
* Receive confirmation email:
	* complete an order.
	* Go to email inbox of email that was provided.
* Get in contact with store owners:
	* Go to contact page
	* Complete form
	* Click submit.
	* Admin receives an email.
* Add product: 
	* Sign in as superuser.
	* Click my account dropdown.
	* Click product Management.
	* Complete Add product Form.
	* Click add product button.
* Edit/Update product:
	* Sign in as a superuser.
	* Navigate to products page.
	* Click edit button on product card.
	* Make desired changes to product.
	* Click the update button.
* Delete  product: 
	* Sign in as superuser:
	* Navigate to products page
	* Click Delete button on product card
	* Product is deleted.

### Bugs
1. When site was deployed to heroku some of the images stored in s3 where not loading. I fixed this by switching the images from html < img > tag to background images in css.

## Deployment
To deploy this page to heroku the following steps were taken.
1. Go to heroku and create a new app with the region set to your closest region.
2. In settings tab of your app click reveal config vars.
3. Enter the following required environment variables,  AWS_ACCESS_KEY_ID,  AWS_SECRET_ACCESS_KEY,  DATABASE_URL,  EMAIL_HOST_PASS,  EMAIL_HOST_USER,  SECRET_KEY,  STRIPE_PUBLIC_KEY,  STRIPE_SECRET_KEY,  STRIPE_WH_SECRET  and finally set  USE_AWS  to  True.
4. In your IDE of choice create an  env.py  containing  all  of the variables from step 3 and add it to the  .gitignore.
5. In your IDE of choice create a  requirements.txt  by using the command  pip freeze -local > requirements.txt.
6. 1.  In your IDE of choice create a  Procfile  by using the command  echo web: gunicorn surfshop.wsgi:application app.py > Procfile.
7. Go to the Deploy  tab and select Heroku Git.
8. In your IDE of choice use the command  git push heroku master.

To deploy this site locally:
1. Under the repository name, click "Clone or download".
2. In the Clone with HTTPs section, copy the clone URL for the repository.
3. Open your IDE of choice.
4. Change the current working directory to the location where you want the cloned directory to be made.
5. Type git clone, and then paste the URL you copied in Step 2.
6. Press Enter. Your local clone will be created.
7. In environment settings you will need to add the environment variables from step 3 in deploying to heroku.

## Credits
### Content
* The [code Institute](https://github.com/ckz8780/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) project Boutique Ado was followed during development and much of the layout is based off of it.

### Media
* Background Images were Taken from [freepik.com](https://www.freepik.com/)
* Brand images and product images were taken from Google images.

### Acknowledgements
* Precious my mentor for helping me through out the project. 

 
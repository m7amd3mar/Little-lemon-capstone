# Meta: Back-End Developer Capstone

▷ This is the final assignment of the Meta Backend Developer Professional Certificate on Coursera

Throughout this project, I've explored various aspects of back-end development, including database management, API design, authentication, and optimization. By tackling real-world challenges and implementing industry best practices, I've honed my abilities to architect and deploy back-end solutions that meet the needs of modern applications.

Thanks for taking the time to review this project! My hope is that it sparks inspiration and provides helpful guidance for other aspiring back-end developers as they navigate their own paths in the exciting world of software development.

## Content Guide 🗺️

▷ Feel free to navigate around using the content button located in the top right corner—it's a breeze for moving through the content.

## API Endpoints testing 🔄 

▷ The API app comes with a total of 4 endpoints, plus you'll find Djoser endpoints ready to use as well.

- Check out all the menu items or craft a unique addition
```
http://127.0.0.1:8000/api/menu/items
```

| Method | Action                  | TOKEN AUTH | STATUS CODE |
|--------|-------------------------|------------|-------------|
| GET    | Retrieve all menu items | No         | 200         |
| POST   | Create a menu item      | No         | 201         |

- Discover, update, partially modify, or bid farewell to that special dish
```
http://127.0.0.1:8000/api/menu/items/{itemId}
```

| Method | Action                           | TOKEN AUTH | STATUS CODE |
|--------|----------------------------------|------------|-------------|
| GET    | Retrieves the menu item details  | No         | 200         |
| PUT    | Update the menu item             | No         | 200         |
| PATCH  | Partially update the menu item   | No         | 200         |
| DELETE | Delete the menu item             | No         | 200         |

- Explore, update, partially adjust, or remove that special table
```
http://127.0.0.1:8000/api/booking/tables
```

| Method | Action                 | TOKEN AUTH | STATUS CODE |
|--------|------------------------|------------|-------------|
| GET    | Retrieve all bookings  | Yes        | 200         |
| POST   | Create a booking       | Yes        | 201         |

- Check it out, update, partially modify, or bid farewell to that one special table
```
http://127.0.0.1:8000/api/booking/tables/{bookingId}
```

| Method | Action                        | TOKEN AUTH | STATUS CODE |
|--------|-------------------------------|------------|-------------|
| GET    | Retrieve the booking details  | Yes        | 200         |
| PUT    | Update the booking            | Yes        | 200         |
| PATCH  | Partially update the booking  | Yes        | 200         |
| DELETE | Delete the booking            | Yes        | 200         |

## Peer review 🧐

▷ I've got a couple of folks looking over my code, and before they grade it, they're checking out things like:

- Did I use Django to dish out those web pages?
- Did I stash Ir project in a Git repo?
- Does Ir app link up the backend with MySQL?
- Did I hook up those menu and table booking APIs?
- Have I set things up so folks can sign up and log in?
- Did I write some unit tests for your app?
- And can someone fire up Insomnia and give your API a spin?

## Grades
▷ There's always room for improvement, and I'm steadily climbing towards that perfect score of 100%.

### Starting the Project
![Module #1](https://github.com/mistersouza/little-lemon/blob/main/static/img/grades/capstone_grad_module%231.png)

### Project Functionality
![Module #2](https://github.com/mistersouza/little-lemon/blob/main/static/img/grades/capstone_grad_module%232.png)

### Security and Testing
![Module #3](https://github.com/mistersouza/little-lemon/blob/main/static/img/grades/capstone_grad_module%233.png)

### Final Graded Assessment
![Final Assessment](https://github.com/mistersouza/little-lemon/blob/main/static/img/grades/capstone_grad_module%234.png)
# Meta: Back-End Developer Capstone

▷ This is the final assignment of the Meta Backend Developer Professional Certificate on Coursera

Throughout this project, I've explored various aspects of back-end development, including database management, API design, authentication, and optimization. By tackling real-world challenges and implementing industry best practices, I've honed my abilities to architect and deploy back-end solutions that meet the needs of modern applications.

Thanks for taking the time to review this project! My hope is that it sparks inspiration and provides helpful guidance for other aspiring back-end developers as they navigate their own paths in the exciting world of software development.

## Content Guide 🗺️

▷ Feel free to navigate around using the content button located in the top right corner—it's a breeze for moving through the content.

## API Endpoints

▷ The API app comes with a total of 4 endpoints, plus you'll find Djoser endpoints ready to use as well.

```
http://127.0.0.1:8000/api/menu/items
```

| Method | Action                  | TOKEN AUTH | STATUS CODE |
|--------|-------------------------|------------|-------------|
| GET    | Retrieve all menu items | No         | 200         |
| POST   | Create a menu item      | No         | 201         |

```
http://127.0.0.1:8000/api/menu/items/{itemId}

```

| Method | Action                              | TOKEN AUTH | STATUS CODE |
|--------|-------------------------------------|------------|-------------|
| GET    | Retrieves the menu item details     | No         | 200         |
| PUT    | Update the menu item                | No         | 200         |
| PATCH  | Partially update the menu item      | No         | 200         |
| DELETE | Delete the menu item                | No         | 200         |

```
http://127.0.0.1:8000/api/booking/tables
```

| Method | Action                    | TOKEN AUTH | STATUS CODE |
|--------|---------------------------|------------|-------------|
| GET    | Retrieve all bookings     | Yes        | 200         |
| POST   | Create a booking          | Yes        | 201         |


```
http://127.0.0.1:8000/api/booking/tables/{bookingId}
```

| Method | Action                             | TOKEN AUTH | STATUS CODE |
|--------|------------------------------------|------------|-------------|
| GET    | Retrieve the booking details       | Yes        | 200         |
| PUT    | Update the booking                 | Yes        | 200         |
| PATCH  | Partially update the booking       | Yes        | 200         |
| DELETE | Delete the booking                 | Yes        | 200         |



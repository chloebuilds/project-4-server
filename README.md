

# Project-4: Zenith

#### General Assembly SEI Project-4 | Zenith | Full-stack app | 10-day sprint | 3-person team

Deployed version of our app can be found here: - https://ga-zenith.netlify.app/

To access all of the features you can register or use the following credentials to login:

email: chloe-test@email.com password: password

<p>
<img src="images/homepage.png" alt="homepage"/>
</p>

## Overview

This was the final project on General Assembly's Software Engineering Immersive. As a group, we were tasked with building a full-stack application of our choice; using Django REST Framework and PostgreSQL on the backend and React on the frontend.

As a team, we shared an interest in wellbeing and personal development and wanted our project to reflect that. We noticed that despite how effective Agile methodology is, there aren't many resources that will help people to incorporate it into their personal development. We wanted to leverage this gap and create an app for developers who are already accustomed to working in sprints, to apply it to their daily lives and personal goals.

To access the backend repository please [click here.](https://github.com/chloebuilds/zenith-server)

## Collaborators

- Alara Ayan - [alaraayan](https://github.com/alaraayan)
- Elsa Guibert- [Elsa245](https://github.com/Elsa245)

## Brief

The brief given was to:

- **Build a full-stack application** by making your own backend and your own frontend.
- **Use a Python Django API** using Django REST Framework to serve your data from a Postgres database.
- **Consume your API with a separate front-end** built with React.
- **Be a complete product** which most likely means multiple relationships and CRUD functionality for at least a couple of models.
- **Implement thoughtful user stories/wireframes** that are significant enough to help you know which features are core MVP and which you can cut.
- **Be deployed online** so it's publicly accessible.

## Technologies Used

**Frontend**

- HTML5
- CSS3, Sass and Styled Components
- React.js
- JavaScript(ES6)
- Dependencies installed: styled-components, react-router-dom, react-toastify, react-loader-spinner, hamburger-react
- [GIPHY API](https://developers.giphy.com/)
- [Open Weather API](https://openweathermap.org/api)

**Backend**

- Python
- Django
- Django REST Framework

**Database**

- PostgreSQL

**Dev Tools**

- Git
- GitHub
- Google Chrome Dev Tools
- VScode
- ESlint
- Insomnia

## Process

### Preparation & Organisation

Our whole project revolved around the dashboard so we started by determining how we wanted it to look and feel. After the wireframing stage we worked on our ERD. At first it seemed very complex, all the daily, weekly and monthly tasks etc. but once we realised everything was actually tied to the user and the current sprint it all clicked.

Final stage of our preparation was setting up our Trello board. We were all already familiar with working with Trello and it helped keep all our tasks organised. We set it up so we would have a few stages for every task to generate a better flow.

We had daily standups within our group and worked together throughout the day. We merged our Git branches every evening, tested the app and assigned new tasks for the next day. Although we worked on our separate tasks, because the functionalities were very similar we were often collaborating, especially while building the backend.

###### Our Trello board:

<img src="images/trello.png" alt="trello board"/>

###### Our wireframe showing the dashboard and all its components:

<img src="images/wireframe.png" alt="wireframe"/>

###### Our ERD showing how everything is connected to the sprint which is connected to the user:

<img src="images/erd.png" alt="erd diagram"/>

### Backend

After the planning stage was done our Trello board was populated with backend tasks. Same as project-3 we wanted to finish the backend completely before moving on to the frontend. Being new to Python and Django we decided to divide functionalities up evenly so we were were each responsible for certain features and building them from start to finish – covering models, views, serializers and templates. I took on the challenge to build on the user, the daily gratitude and weekly intention features. 

The model for a to-do item looked like this:

```python
class DailyGratitude(models.Model):
    daily_gratitude = models.CharField(max_length=200)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    sprint = models.ForeignKey(
            Sprint,
            related_name="daily_gratitudes",
            on_delete=models.PROTECT,
            null=True
        )
    def __str__(self):
        return f"{self.daily_gratitude}"
```

Because everything was individually connected to the sprint, creating the relationships within serializers was fairly simple. Here's our `PopulatedSprintSerializer`:

```python
class PopulatedSprintSerializer(SprintSerializer):
    owner = UserSerializer()
    sprint_goals = SprintGoalSerializer(many=True)
    sprint_habits = SprintHabitSerializer(many=True)
    weekly_intentions = WeeklyIntentionSerializer(many=True)
    moods = DailyMoodSerializer(many=True)
    energy_levels = DailyEnergySerializer(many=True)
    to_dos = DailyToDoSerializer(many=True)
    daily_gratitudes = DailyGratitudeSerializer(many=True)
```

Getting our views done proved to be more difficult. We wanted each item to have an end date calculated automatically depending on whether it was a daily item or a sprint habit – each of which is supposed to end with each 4 week sprint. To achieve this we used `timedelta`. We would then run a check to reset if an item's end date has been reached in the frontend.

```python
request.data["end_date"] = date.today() + timedelta(days=6)
```

### Frontend

Once we were certain our backend was working fully, we started working on the frontend. Being comfortable with React by this point, we knew what we wanted to do and all of us were really excited to bring all of the components together in the dashboard. We needed to make sure that only logged in users would be able to access certain URLs and a user won't be able to see another user's dashboard even if they accidentally put in the correct URL. We decided to keep things light throughout Zenith and I created custom 401 and 404 pages the user would be sent to if they made an incorrect request.

In the frontend I took on the opportunity to build the dashboard, user registration and login components, daily gratitudes, weekly intention, inspirational quote and . With the user's experience in mind, I wanted the user to create a sprint step by step in order to not feel overwhelmed. A logged in user would be directed to the new sprint page if they were not in an active sprint -`currentSprint ? history.push('/dashboard') : history.push('/sprints/new')`-. Only once the sprint is created a user is able to access their dashboard, which is reset every time the user is logged in, checking and removing expired data accordingly. Since everything is derived from the user, to achieve this functionality we created a `UserContext`. With the `UserContext` we were able to get only relevant data and therefore update the dashboard as needed automatically every time a user logged in.

We also used Styled Components for this project. None of us had used it before and were very intrigued. I took on the task of putting together the styling and the look and feel of the app. I was very influenced by glassmorphism :) 

## Screenshots

###### Logged in user is guided through to create a sprint:

<img src="images/new-sprint.png" alt="new user redirection"/>
<img src="images/sprint-start-1.png" alt="new sprint naming"/>

###### Only users with active sprints are able to access their dashboard:

<img src="images/dashboard.png" alt="dashboard"/>

###### Error handling:

<img src="images/401.png" alt="authorisation error"/>
<img src="images/404.png" alt="page not found error"/>

## Challenges

- Zenith became a lot more complex than we initially thought and as we started to put together the ERD and thing about the relationships and how they would be displayed on the frontend, we realised we had taken on quite the challenge. Building our backend was the most time consuming part but it was also both challenging and rewarding as we learned a lot about SQL and relational databases. 
- `time delta`: Working with time and having time dependent tasks was incredibly challenging. It was not something we had worked with before and so it took extra time of learning and understanding in order to be able to successfully implement it. 
- React `useContext`: neither of us had used or learned about the `useContext` hook and so this was new and exciting to us. We knew we needed to share the data from the backend across multiple components in the dashboard based on whether a user was logged in and in a current sprint and so `useContext` helped us with that.
- `styled-components`: I have a love for styling and I wanted a challenge on this project on the styling. I had heard a lot about styled components and decided to make it work in zenith. Once I got started I really enjoyed it and was able to explain it to Alara and Elsa. However, it slowed me down to do this.
- Overall, zenith was incredibly challenging to build and there were moments where we could have taken easier routes but we were each determined to not compromise certain key aspects of the project. While there are still features we’d love to add; I am very proud of where we got it to in a week.


## Wins

- Without wanting to sound cliche I really feel that the entire project was a win. We took on A LOT, learned a a lot and challenged ourselves a lot - but we did it and we all worked together incredibly well. Each of the challenges above became wins by the end.
- UX: We managed to create a seamless user journey from registration through to the end of the sprint. The dashboard is clean, clear and easy to use with instant feedback and visibility to the user about their current sprint.
- UI: We built a user dashboard that we are proud of and that we each want to use ourselves.
- We really used React to its advantage with implementation of the deshboard displaying multiple components. The user can interact with each component while on their dashboard. Also, using conditional rendering and the ternary operator I was able to conditionally show parts of a component to the user, giving the illusion of moving from one page to the next while actually staying in the same one. 


```javascript
<div className={isStartingNewSprint ? 'no-show' : ''}>
  <h2>Hey {user.name},</h2>
  <h4>Welcome to Zenith!</h4>

  <p>
    It looks like you&apos;re not currently in an active sprint.{' '}
  </p>
  <p>Begin your new sprint now. </p>
  <button onClick={handleStartToggle}>New sprint</button>
 </div>
<div className={isStartingNewSprint ? '' : 'no-show'}>
  <form onSubmit={handleNewSprint}>
    <p>
      First things first, let&apos;s give your sprint a name..
    </p>

  <Input
    placeholder="My awesome sprint..."
    onChange={handleChange}
    name="sprintName"
    value={formData.sprintName}
    />
  {formErrors.sprintName && <p>{formErrors.sprintName}</p>}

  <button>Done</button>
  </form>
</div>
```

## Key Learnings

<p>The scope of this project felt overwhelming to us all at times and we had to work well together as a unit to overcome this. We kept a very organised Trello board. We also categorised the project and all of us worked on one leg of the current category, so we faced the problems together instead of each person being responsible for an entire functionality. This was a new approach and I believed worked very well for this project.

The biggest challenge we faced as a team on this project was to incorporate time into the app. We wanted certain aspects of the dashboard to refresh daily, weekly or stay the same for 28 days. We ended up using React Context which gave us the ability to also have extra validation and prevent logged-in users from accessing other users' dashboards by manipulating the URL.

The main takeaway for me was that I got to develop the muscle of switching between programming languages. All our previous projects were built using JavaScript and for this project, we had to go back and forth between JavaScript and Python. This felt challenging at first, but felt more and more natural with time and ended up being helpful to differentiate logic.

We worked incredibly well together as a team and complemented each other's strengths and in the end, have a project we are proud of.</p>

## Future Features

If we had more time on this project we would add:

- Responsiveness design
- Dark mode / light mode.
- Drag and drop functionality for the dashboard components.
- Ability to mark tasks as 'done' manually.
- View past sprints.
- See and filter tasks in the calendar component.

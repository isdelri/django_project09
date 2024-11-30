# Django Blogging Project

This is a simple blogging application built with Django, where users can create posts, categorize them, and view them through an admin interface and a public-facing website. This project also includes login/logout functionality and an admin dashboard for managing content.

## Features
The blogging detail view doesn't accept POST requests, so there will be no need to create a `post` method in the blogging detail view.
When you're done, the front page should continue to display only published posts and it should continue to display posts in reverse-chronological order. 
To accomplish this, you'll be providing a `queryset` class attribute in your list view instead of a `model` class attribute. See https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-display/#viewing-subsets-of-objectsLinks to an external site. 
for examples of filtering and sorting querysets. You'll want to apply both `filter` (or `exclude`) and `order_by` methods to your `Post.objects` queryset.

---

## Installation and Setup

### Prerequisites
- Python 3.8+ installed on your system.
- `pip` (Python package manager) installed.
- Git installed.
- A web browser.

---

### 1. Clone the Repository
Run the following command to clone the repository:
```bash
git clone https://github.com/isdelri/django-blogging.git
cd django-blogging

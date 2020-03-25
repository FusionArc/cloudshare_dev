# cloudshare_dev
Web Application codebase for cloudshare.space.
Built with Django 3.04 and Python 3.8.
This application is to perform as a repository/gallery for User Awards, Achievements and Certificates.
Where each individual User account will be a showcase of their own certificates and achievements accuired 
throughout their careeer. 
Each showcase can be shared publicly via a shortlink URL, and given to prospective employers, investors etc.
The sole purpose of this application is to provide Achievers & Viewers of Achievers, a clean and concise portfolio 
of the many possible achievments and certificates that need to be shown or viewed respectively.

# Roadmap 
Deployment: 
Google compute engine, Ubuntu 18.04
Gunicorn wsgi server & NGINX web server
PostgresQL / GraphQL integration
CI / CD with git web hooks
Media Uploads via django-storages to GCS bucket
Static files Stored persistantly on server SSD for better performance
Social Login/Authentication itegration with Google / GitHub
Uploaded media from Google Drive / Third Party URL

# AI Integration
Cloud Vision API for validating documents as certificates
Automatically recognizing documents matching known certificates and awards
Categorizing of awards/activities/awarding bodies/occupations/education paths/ etc 

# Web Scraping Chron Jobs:
Scrape the web every 7 days for 1 hour, 
searching for new/unregistered awards/awarding bodies,
update the database / cloud storage accordingly,
render new results within the application

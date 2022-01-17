# GarageMonitoring

Monitoring entrances to a house is key for safety. Most standard houses use alarm safety systems to check the status of doors that lead into the house. However, some entry points, such as garage doors, remain unmonitored. By identifying the pincode sent to open your garage, anyone else could gain entry into your home.

Using only a low-cost ESP Microprocessor and a bluetooth beacon, this project aims to solve this issue in an accessible way.

Presentation of primary components: https://docs.google.com/presentation/d/1W_Gj4mmGI37sbpLe8FZXNkh5qJL8ZnENnBcXSSq-JtQ/edit?usp=sharing

*Imported from Arduino IDE and Pycharm IDE



Update (v2.0):
* prometheus service updated
* moved to grafana labs for visualization
* configured for and tested as docker containers on gcp (individual containers and preconfigured images for 
  python app and prometheus)

Running the application via Docker as two containers (using an ubuntu and prometheus image) ensures
isolation of the application. If one of the processes fails, the other is able to keep running. 
Additionally, scaling this application to many users is made much easier.

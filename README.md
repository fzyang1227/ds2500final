# ds2500final
https://github.com/fzyang1227/ds2500final

We are shifting through Kickstarter data


Dataset:
https://webrobots.io/kickstarter-datasets/

Presentation:
https://docs.google.com/presentation/d/1q78R2EHl_tyBju1rvtcOUOWHf-lSQpRu3eQ6fTZe0Ig/edit?usp=sharing

Final Project Report:
https://docs.google.com/document/d/1Xq4d1JQZHa-z0q1LOc7k06F22_q4qG2dkCed29LZP04/edit?usp=sharing

## Quick Description of clean_data columns:
- backers_count: # of backers (int)
- blurb: description of Kickstarter (string)
- category: (string)
- country_displayable_name: full name of country (string)
- creator: name of creator (string)
- goal: amount of money needed for project (int)
- location: city, state (string)
- name: (string)
- pledged: amount of money pledged (int)
- slug: name in lowercase and cleaned (string)
- spotlight: whether or not spotlighted (Boolean)
- staff_pick: whether or not picked by staff (Boolean)
- state: current state (string of specific values)
  - failed, successful, live, cancelled
    
- urls: url of project (string)
- usd_pledged: amount pledged (int)
- preview_time: amount of days between creation and launch time (int)
- fundraising_time: amount of days between launch and deadline (int)
- state_change: amount of days between launch and state change time (int)
  
### *note: all these are formatted as strings when retrieved from csv file

# <p style="text-align:center">Web Scrapper</p>

## :pushpin: About the Project

- Scrapping [iNeuron Courses][ineuron] and storing them in MongoDB.
- Scrapping using Beautiful Soup python module.
- Flask based web application.

Deployed on Heroku and Azure.  
[Scrapper on Heroku][scrapper-heroku]  
[Scrapper on Azure][scrapper-azure]

---

## :pushpin: Challenge

- [iNeuron Courses][ineuron] is developed using NextJs (Dynamic Website).
- Dynamic Website cannot be loaded as html without javascript engine at client side.
- Beautiful Soup does scrapping without javascript engine, hence we have to deal with json data (props) from `script` tag. It can be selected with `soup.find("script", src=None)` and converting json to python dictionary.
- For converting we use `json.loads(soup.find("script", src=None).text)`

---

## :pushpin: Another way to tackle

- We can use `Selenium` to load the page with headless browser and then scrap this data with the help of `Beautiful Soup` or continue with `Selenium`.
- Here we get an HTML and not json data as `Selenium` loads the page with the help of javascript engine.

---

## :hammer_and_wrench: Technologies and Tools Used

### :hammer:Technologies

[![Language | HTML5](https://img.shields.io/badge/html5-eeeeee?style=for-the-badge&logo=html5&logoColor=ffffff&labelColor=E34F26)][html5]
[![Language | CSS3](https://img.shields.io/badge/CSS3-eeeeee?style=for-the-badge&logo=css3&logoColor=ffffff&labelColor=1572B6)][css3]
[![Language | Python](https://img.shields.io/badge/Python-eeeeee?style=for-the-badge&logo=python&logoColor=ffffff&labelColor=3776AB)][python]
[![Language | MongoDB](https://img.shields.io/badge/Mongo_DB-eeeeee?style=for-the-badge&logo=mongodb&logoColor=47A248&labelColor=fefefe)][mongodb]
[![Framework & Library | Flask](https://img.shields.io/badge/Flask-eeeeee?style=for-the-badge&logo=flask&logoColor=000000&labelColor=fefefe)][flask]

### :wrench: Tools

[![Tools | Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-eeeeee?style=for-the-badge&logo=visual-studio-code&logoColor=007ACC&labelColor=2C2C32)][visual_studio_code]
[![Tools | Git](https://img.shields.io/badge/Git-eeeeee?style=for-the-badge&logo=git&logoColor=F05032&labelColor=f0efe7)][git]
[![Tools | GitHub](https://img.shields.io/badge/Github-eeeeee?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=181717)][github]
[![Tools | Postman](https://img.shields.io/badge/Postman-eeeeee?style=for-the-badge&logo=postman&logoColor=FF6C37&labelColor=fefefe)][postman]
[![Tools | Heroku](https://img.shields.io/badge/Heroku-eeeeee?style=for-the-badge&logo=heroku&logoColor=ffffff&labelColor=430098)][heroku]
[![Tools | Microsoft Azure](https://img.shields.io/badge/Microsoft_Azure-eeeeee?style=for-the-badge&logo=microsoft-azure&logoColor=ffffff&labelColor=0078D4)][microsoft_azure]

---

## :round_pushpin: Reach

[![Shivam Panchal | LinkedIn](https://img.shields.io/badge/Shivam_Panchal-eeeeee?style=for-the-badge&logo=linkedin&logoColor=ffffff&labelColor=0A66C2)][reach_linkedin]
[![GodWin1100 | GitHub](https://img.shields.io/badge/Godwin1100-eeeeee?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=181717)][reach_github]
[![shivamjpanchal1 | G Mail](https://img.shields.io/badge/shivamjpanchal1-eeeeee?style=for-the-badge&logo=gmail&logoColor=ffffff&labelColor=EA4335)][reach_gmail]

<!-- Links  -->

[ineuron]: https://courses.ineuron.ai/
[scrapper-heroku]: https://scrapper-task.herokuapp.com/
[scrapper-azure]: https://scrapper-task.azurewebsites.net/

<!-- Technology -->

[html5]: https://developer.mozilla.org/en-US/docs/Web/HTML
[css3]: https://developer.mozilla.org/en-US/docs/Web/CSS
[python]: https://www.python.org/
[mongodb]: https://www.mongodb.com/
[flask]: https://flask.palletsprojects.com/en/2.1.x/

<!-- Tools -->

[visual_studio_code]: https://code.visualstudio.com/
[postman]: https://www.postman.com/
[git]: https://git-scm.com/
[github]: https://github.com/
[heroku]: https://www.heroku.com/
[microsoft_azure]: https://azure.microsoft.com/en-in/features/azure-portal/

<!-- Reach  -->

[reach_linkedin]: https://www.linkedin.com/in/shivam-panchal-godwin1100
[reach_gmail]: mailto:shivamjpanchal1@gmail.com?subject=GitHub%20Hello
[reach_github]: https://github.com/GodWin1100

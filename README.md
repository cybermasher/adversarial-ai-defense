
<div align="center">

  <img src="assets/cyber-banner-image.jpg" alt="adversarial-ai-banner-image" width="1280" height="auto" />
  <h1>Adversarial-AI-Defense</h1>
  
  <p>
    A project in development (pre-alpha) written in Python and optimized with optuna using venv, tensorflow, numpy, pandas, scikit-learn, and matplotlib that uses deep machine learning to defend against potential adversarial AI threats. 
  </p>
  
  
<!-- Badges -->
<p>
  <a href="https://github.com/Louis3797/awesome-readme-template/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Louis3797/awesome-readme-template" alt="contributors" />
  </a>
  <a href="">
    <img src="https://img.shields.io/github/last-commit/Louis3797/awesome-readme-template" alt="last update" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/network/members">
    <img src="https://img.shields.io/github/forks/Louis3797/awesome-readme-template" alt="forks" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/stargazers">
    <img src="https://img.shields.io/github/stars/Louis3797/awesome-readme-template" alt="stars" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/issues/">
    <img src="https://img.shields.io/github/issues/Louis3797/awesome-readme-template" alt="open issues" />
  </a>
  <a href="https://github.com/Louis3797/awesome-readme-template/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/Louis3797/awesome-readme-template.svg" alt="license" />
  </a>
</p>
   
<h4>
    <a href="https://github.com/cybermasher/adversarial-ai-defense">View Demo</a>
  <span> · </span>
    <a href="https://github.com/cybermasher/adversarial-ai-defense">Documentation</a>
  <span> · </span>
    <a href="https://github.com/Louis3797/awesome-readme-template/issues/">Report Bug</a>
  <span> · </span>
    <a href="https://github.com/Louis3797/awesome-readme-template/issues/">Request Feature</a>
  </h4>
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  * [Screenshots](#camera-screenshots)
  * [Tech Stack](#space_invader-tech-stack)
  * [Features](#dart-features)
  * [Color Reference](#art-color-reference)
  * [Environment Variables](#key-environment-variables)
- [Getting Started](#toolbox-getting-started)
  * [Prerequisites](#bangbang-prerequisites)
  * [Installation](#gear-installation)
  * [Running Tests](#test_tube-running-tests)
  * [Run Locally](#running-run-locally)
  * [Deployment](#triangular_flag_on_post-deployment)
- [Usage](#eyes-usage)
- [Roadmap](#compass-roadmap)
- [Contributing](#wave-contributing)
  * [Code of Conduct](#scroll-code-of-conduct)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)

  

<!-- About the Project -->
## :star2: About the Project

I wanted to build my own learning model that would help defend against adversarial AI threats and attacks. Piecing together this project with the help of my own coding expierence, Chat GPT, and the awesome programming community, my goal is to create an open source program that will prevent AI chatbots, and other applications from meliciously breaching an organization's defenses.   

<!-- Screenshots 
### :camera: Screenshots

<div align="center"> 
  <img src="https://placehold.co/600x400?text=Your+Screenshot+here" alt="screenshot" />
</div>


 TechStack 
### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
    <li><a href="https://nextjs.org/">Next.js</a></li>
    <li><a href="https://reactjs.org/">React.js</a></li>
    <li><a href="https://tailwindcss.com/">TailwindCSS</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.typescriptlang.org/">Typescript</a></li>
    <li><a href="https://expressjs.com/">Express.js</a></li>
    <li><a href="https://go.dev/">Golang</a></li>
    <li><a href="https://nestjs.com/">Nest.js</a></li>
    <li><a href="https://socket.io/">SocketIO</a></li>
    <li><a href="https://www.prisma.io/">Prisma</a></li>    
    <li><a href="https://www.apollographql.com/">Apollo</a></li>
    <li><a href="https://graphql.org/">GraphQL</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.mysql.com/">MySQL</a></li>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
    <li><a href="https://redis.io/">Redis</a></li>
    <li><a href="https://neo4j.com/">Neo4j</a></li>
    <li><a href="https://www.mongodb.com/">MongoDB</a></li>
  </ul>
</details>

<details>
<summary>DevOps</summary>
  <ul>
    <li><a href="https://www.docker.com/">Docker</a></li>
    <li><a href="https://www.jenkins.io/">Jenkins</a></li>
    <li><a href="https://circleci.com/">CircleCLI</a></li>
  </ul>
</details>
-->
<!-- Features -->
### :dart: Features

- Feature 1
- Feature 2
- Feature 3

<!-- Getting Started 
## 	:toolbox: Getting Started
-->
<!-- Prerequisites
### :bangbang: Prerequisites
-->

<!-- Installation -->
### :gear: Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
   
<!-- Run Locally -->
### :running: Run Locally

Clone the project

```bash
  git clone https://github.com/cybermasher/adversarial-ai-defense.git
```

Go to the project directory

```bash
  cd adversarial-ai-defense
```

Setup Virtual Environment Using Venv

```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

Install Required Libraries

```bash
 pip install numpy pandas scikit-learn tensorflow matplotlib optuna

```

Create Project Structure

```bash
mkdir data models notebooks src
touch README.md requirements.txt .gitignore

```

<!-- Usage -->
### :eyes: Usage

To train the model run:

```bash
  python src/train_model.py

```
To generate adversarial examples run:

```bash
  python src/adversarial_attack.py

```
For Adversarial model training run:

```bash
  python src/defense_mechanism.py

```

<!-- Roadmap -->
## :compass: Roadmap

* [x] Launch alpha version
* [ ] Test and bug fix
* [ ] Gather feedback and feature requests
* [ ] Modify and retrain model algorithms
* [ ] Launch beta version
* [ ] Test, Bug fix, and patch
* [ ]   


<!-- Contributing -->
## :wave: Contributing

<a href="https://github.com/Louis3797/awesome-readme-template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Louis3797/awesome-readme-template" />
</a>


Contributions are always welcome!

See [Contributions](https://github.com/cybermasher/adversarial-ai-defense/contributing.md) to learn how you can add your expertise to the project.


<!-- Code of Conduct -->
### :scroll: Code of Conduct

Please read the [code of Conductt](https://github.com/cybermasher/adversarial-ai-defense/CODE_OF_CONDUCT.md)

<!-- FAQ -->
## :grey_question: FAQ

- Question 1

  + Answer 1

- Question 2

  + Answer 2


<!-- License -->
## :warning: License

Distributed under the GPL-3.0 license. See LICENSE.txt for more information.


<!-- Contact -->
## :handshake: Contact
<a href="https://github.com/cybermasher/adversarial-ai-defense">
  <img src="images/cybermasher.jpg" alt="cybermasher avatar" width="125" height="125" />
</a>
<br>
Dustin Schmidt - [@dankpeace](https://twitter.com/dankpeace) - dschmidt2020[at]gmail[dot]com

Project Link: [https://github.com/cybermasher/adversarial-ai-defense](https://github.com/cybermasher/adversarial-ai-defense)


<!-- Acknowledgments -->
## :gem: Acknowledgements

 - [NumPy](https://numpy.org/)
 - [Pandas](https://pandas.pydata.org/)
 - [Scikit-Learn](https://scikit-learn.org/stable/)
 - [TensorFlow](https://www.tensorflow.org/)
 - [Matplotlib](https://matplotlib.org/)
 - [Optuna](https://optuna.org/)

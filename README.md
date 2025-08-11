# IS 601 M13 - JWT Login/Registration with Client-Side Validation & Playwright E2E

This project is for the IS 601 summer semester.

# How to install the program and run the front end

- 1: have postgres and all its dependencies installed on your computer.
- 2: have python 3.12 or later installed on your computer.
- 3: activate a python virtual environment on your computer.
- 4: install all dependencies listed in requirements.txt.
- 5: run the following in your terminal: uvicorn app.main:app --host 127.0.0.1 --port 8000
- 6: enter http://localhost:8000/login on your web browser.
- 7: enjoy!

# How to execute playwright tests

- 1: in your terminal, activate your virtual environment.
- 2: run the following command in your terminal: python3 -m pytest
- Note: there is one test with the 'slow' tag on it. to run that in the test suite, run the following command: python3 -m pytest --run-slow

# Reflection

I feel like this was a prime example of an assignment that generated an unjustifiable quantity of stress before I began implementing it. This is, more likely than not, due to the fact that shortly into my work on it, when I was dealing with an annoying bug very early on and little had been saved to GitHub, my computer BSODed on me and I was left without the ability to work on this project for a week.

That said, after fixing my computer, the second attempt was much more fluid and stress-free. I felt that I understood this project very well and was not concerned or intimidated by any part of the process.

# Links

docker hub: https://hub.docker.com/repository/docker/eg396/is601-m13/general
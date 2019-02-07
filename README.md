As you can see in requirements.txt file, you need to install flask. to run this whole program.
You will see two python files, which is 'lab3_code.py' and 'si507_project_1.py'. The file 'lab3_code.py' is essential source code for running 'si507_project_1.py' file.


<What 'lab3_code.py' contains>
1. It defines classes named 'Currency', and 'Bank'.
2. It defines 'Dollar', 'Yuan', and 'Pound' as subclasses of Class 'Currency'.
3. Class 'Currency' has function named 'conversion' for dollar, yuan, and pound.
4. Subclass 'Dollar', 'Yuan', or 'Bank' has string method which shows "value and units"
5. Class 'Bank' has a string method showing the name of the bank and the amount of money that the bank hold with the certain currency. Also, it has function named 'deposit' which is able to add deposited money with initial money and shows whether it is successful or not depends on the currency that user uses.


<About 'si507_project_1.py'>
1. First of all, it requires Flask to route URLs.
2. Also, it requires 'lab3_code.py' file to run the code using classes defined in that file.
3. There are total six routes.
  - http://localhost:5000/
    You will see "Welcome to the banking application!"
  - http://localhost:5000/bank/<name>
    You will see "Welcome to <name>!"
  - http://localhost:5000/dollar/<amt>
    You will see "<amt> Dollar(s)!"
  - http://localhost:5000/yuan/<amt>
    You will see "<amt> Yuan(s)!"
  - http://localhost:5000/pound/<amt>
    You will see "<amt> Pound(s)!"
  - http://localhost:5000/bank/<name>/<currency>/<value>
    You will see "Welcome to the <name> bank! <name> Bank holds the <currency> currency and currently holds <value> of <currency>."
4. Depends on what you put in the URL, the sentence will vary.


<HOW TO RUN>
To run this program in the virtual environment,
1. Open terminal or any command prompt you have.
First of all, we have to make and activate the virtual environment.
2. Type: python3 -m venv project1-env
3. Type: source project1-env/bin/activate
4. Type: pip install -r requirements.txt
Since 'requirements.txt' contains Flask, now you will have flask app in your virtual environment.
To run 'si507_project_1.py' file,
5. Type: python SI507_project_1.py runserver
Then, open Chrome or Safari and go to http://localhost:5000/
You will see 'Welcome to the banking application!' in the window.

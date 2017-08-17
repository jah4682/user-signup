# ---------------------- Assignment User Signup  ------------------------
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


# welcome screen function
@app.route("/welcome", methods=["POST"])
def welcome():

    # request form information
    username = request.form['username_f'] # get user name
    pwd = request.form['password_f']
    verify = request.form['verify_f']
    email = request.form['email_f']

    # declare error variables. default empty.
    error_username = ''
    error_pwd = ''
    error_pwdVerify = ''
    error_email = ''



    # validate username
    if username == '':                                          # if null
        error_username = 'username must be filled in'
    elif ' ' in username:                                       # if space
        error_username = 'username cannot contain a space'
    elif len(username) < 3 or len(username) > 20:               # if out of range 3 to 20
        error_username = 'username must be between 3 and 20 characters long'


    # validate password
    if pwd == '':                                               # if null
        error_pwd = 'password must be filled in'
    elif ' ' in pwd:                                            # if space
        error_pwd = 'password cannot contain a space'
    elif len(pwd) < 3 or len(pwd) > 20:                         # if out of range 3 to 20
        error_pwd  = 'password must be between 3 and 20 characters long'


    # validate password confirmation
    if pwd != verify:
        error_pwdVerify = 'your passwords do not match'

    # extracting letters from email before the '@' symbol
    email_at_index = email.find('@')            # find the index of '@'
    email_len_b4at = email[:email_at_index]     # splice to get letters before '@' using index of '@'


    # validate email only if it is not left blank, otherwise skip this validation.
    if email != '':
        if "@" not in email and "." not in email and ' ' in email:
            error_email = "email field must contain an '@' and '.' symbol and cannot contain a space"
        elif ' ' in email and "@" not in email:
            error_email = "email field must contain an '@' symbol and cannot contain a space"
        elif ' ' in email and "." not in email:
            error_email = "email field must contain an '.' symbol and cannot contain a space"
        elif "@" not in email and "." not in email:
            error_email = "email field must contain an '@' AND '.' symbol"
        elif "@" not in email:
            error_email= "email field must contain an '@' symbol"
        elif '.' not in email:
            error_email = "email field must contain an '.' symbol"
        elif ' ' in email:
            error_email = "email field cannot contain a space"
        elif len(email_len_b4at) < 3 or len(email_len_b4at) > 20: # range is between 3 and 20 return true
            error_email = "email must be between 3 and 20 characters long"
        else:
            error_email = ''

    # if successful pass to welcome page
    # by default empty strings are boolean false.
    # empty string tells us no errors occured and can safely move to next page
    # turn empty error message to be true with NOT operator.

    if not error_username and not error_pwd and not error_pwdVerify and not error_email:
        return render_template('welcome.html', username_fw=username)
    else:
        #passing into the return the form and the error message for each field. and the value of email and user name field to keep persistence in the text box
        # error_f and _val means it's the variable inside the form.html. without _f means it's the error inside the if statements
        return render_template('form.html',error_email_f=error_email,email_val=email,error_username_f=error_username,username_val=username,error_pwd_f=error_pwd,error_pwdVerify_f=error_pwdVerify)

# index page function
@app.route("/")
def index():

    return render_template('form.html')

app.run()

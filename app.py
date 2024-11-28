#!/usr/bin/env python3

from flask import Flask, render_template, redirect, request, session
from rbac import check_role, get_user_role
from mfa import send_mfa_code, verify_mfa_code
from audit_log import log_event

app = Flask(__name__)
app.secret_key = ''
('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        

        if username == 'admin' and password == 'admin123':
            session['username'] = username
            
            # Send MFA Code
            mfa_code = send_mfa_code(username)
            return render_template('mfa_verify.html', mfa_code=mfa_code)
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# MFA Verification
@app.route('/mfa', methods=['POST'])
def mfa_verify():
    code = request.form['mfa_code']
    if verify_mfa_code(code):
        session['authenticated'] = True
        log_event(session['username'], 'Login Success with MFA')
        return redirect('/dashboard')
    else:
        log_event(session['username'], 'MFA Failed')
        return render_template('mfa_verify.html', error="Invalid MFA Code")

# User Dashboard
@app.route('/dashboard')
def dashboard():
    if not session.get('authenticated'):
        return redirect('/')
    
    user_role = get_user_role(session['username'])
    if user_role == 'admin':
        return render_template('admin_dashboard.html')
    else:
        return render_template('user_dashboard.html')

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

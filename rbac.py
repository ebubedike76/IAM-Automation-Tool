#!/usr/bin/env python3

def check_role(username, role):
    # Placeholder for checking if a user has a specific role
    roles = {
        'admin': ['view_dashboard', 'manage_users', 'review_logs'],
        'user': ['view_dashboard']
    }
    return role in roles.get(username, [])

def get_user_role(username):
    # Example user roles, replace with DB or dynamic check
    if username == 'admin':
        return 'admin'
    return 'user'

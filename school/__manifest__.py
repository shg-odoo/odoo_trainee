{
    'name': 'School & Student',
    'version': '1.0',
    'description': 'Details of students and their school',
    'depends': ['base', 'mail', 'website'],
    'data': [
        'security/student_security.xml',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'wizard/school_wizard_view.xml',
        'reports/student_report.xml',
        'views/web_controller_template.xml',
    ],
    'application': True,
}

# in data key sequence of file in list is matter a lot for 
# example security file path must be on top also first we need to create group
# and then we can assign those group so security.xml file comes first and then
# security.csv file came. If sequence in not in proper order we may get an error like
# -----------------------------------------------------------------------------
# No matching record found for external id 'student.grp_admin' in field 'Group'
# No matching record found for external id 'student.grp_user' in field 'Group'
# we are getting this error because we are trying to use group before creating it means
# wrong sequence of security files.
# -----------------------------------------------------------------------------
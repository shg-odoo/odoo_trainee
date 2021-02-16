{
    'name':'Student',
    'version':'0.1',
    'category':'Extra Tools',
    'author':'Vivek Patel (vpt)',
    'website':'http://www.odoo.com/',
    'summary':'Student Management Software',
    'description':'A student management software to manage students and their records',
    'depends':['base','mail'],
    'data':['views/views.xml','wizard/school_wizard.xml','report/student_report.xml','data/sequence.xml'],
    
    'application':True,
    
}
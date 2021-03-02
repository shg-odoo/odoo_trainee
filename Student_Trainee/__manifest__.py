{
    'name':'School Management',
    'version':'0.1',
    'category':'Extra Tools',
    'author':'Vivek Patel (vpt)',
    'website':'http://www.odoo.com/',
    'summary':'School Management Software',
    'description':'A student management software to manage students and their records',
    'depends':['base','mail','website'],
    'data':['security/security.xml','security/ir.model.access.csv','views/views.xml','views/template.xml','wizard/school_wizard.xml','report/student_report.xml','data/sequence.xml','report/report_inherit.xml'],
    
    'application':True,
    
}
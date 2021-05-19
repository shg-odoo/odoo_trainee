from odoo import api,fields,models

class StudentDetails(models.Model):
    _name = 'student.details'
    _description = 'student information'
    _rec_name = 'student_name'
    
    student_name = fields.Char(string="Name",required=True)
    student_age = fields.Integer()
    student_percentage = fields.Float(compute='_compute_pname',store=True)
    student_birthdate = fields.Date()
    current_date = fields.Date(default=fields.Date.today)
    branch = fields.Char()
    gender = fields.Selection([('male','Male'),('female','Female'),],string="Gender",default='male')
    image = fields.Binary(string="Profile",attachment=True)
    college_id = fields.Many2one('college.details',string="College")
    hobbies = fields.Many2many('student.hobbies')
    fy_marks = fields.Integer(string="First Year Marks")
    sy_marks = fields.Integer(string="Second Year Marks")
    ty_marks = fields.Integer(string="Third Year Marks")
    total_marks = fields.Integer(string="Total Marks")
    
    @api.onchange('fy_marks','sy_marks','ty_marks')
    def _onchange_total(self):
        self.total_marks = self.fy_marks + self.sy_marks + self.ty_marks
        
    @api.depends('fy_marks','sy_marks','ty_marks')
    def _compute_pname(self):
        self.student_percentage = ((self.fy_marks + self.sy_marks + self.ty_marks)/300)*100

    # @api.model
    # def _name_search(self,name='',args=None,operator='ilike',limit=100):
    #     if args is None:
    #         args = []
    #     domain = args + [('student_name',operator,name)]
    #     return super(StudentDetails,self).search(domain,limit=limit)

    def action_confirm(self):
        for x in self:
            students = self.env['student.details'].search([])
            print("students---------->",students)
            
            female_students = self.env['student.details'].search([('gender','=','female')])
            print("female students---------->",female_students)
            
            male_students = self.env['student.details'].search([('gender','=','male')])
            print("male students---------->",male_students)
            
            female_students_and_age = self.env['student.details'].search([('gender','=','female'),('student_age','>=','20')])
            print("female students and age---------->",female_students_and_age)
            
            female_students_or_age = self.env['student.details'].search(['|',('gender','=','female'),('student_age','>=','20')])
            print("female students or age---------->",female_students_or_age)
            
            cout_stud = self.env['student.details'].search_count([])
            print("students count---------->",cout_stud)

            cout_female_stud = self.env['student.details'].search_count([('gender','=','female')])
            print("students female count---------->",cout_female_stud)

            studs_browse = self.env['student.details'].browse([3,4])
            print(studs_browse)

            stud_browse = self.env['student.details'].browse(4)
            if stud_browse.exists():
                print(stud_browse)
                for x in stud_browse:
                    print(x.student_name)
                    print("display name-------->",x.display_name)
                    
            else:
                print("Record Doesn't exists")

            #CREATE

            # vals = {
            #     "student_name": "Prachi",
            #     "student_age" : 21,
            #     "branch":"Computer", 

            # }
            # create_stud = self.env['student.details'].create(vals)
            # print("New Record created",create_stud)

            #Write
            # stud_update = self.env['student.details'].browse(9)
            # if stud_browse.exists():
            #     vals = {
            #     "student_name": "Prachi",
            #     "student_age" : 21,
            #     "branch":"Computer", 
            #     }
            #     stud_update.write(vals)
            # else:
            #     print("Record Doesn't exists")

            #COPY
            # stud_browse = self.env['student.details'].browse(4)
            # stud_browse.copy()

            #UNLINK or Delete
            # stud_browse = self.env['student.details'].browse(11)
            # stud_browse.unlink()



class CollegeDetails(models.Model):
    _name = 'college.details'
    _description = 'College information is stored here'
    _rec_name = 'college_name'
    
    college_name = fields.Char(string="College Name")
    college_city = fields.Char(string="City")
    stud_record = fields.One2many('student.details','college_id',string="Student Records")

    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id,'%s - %s' % (rec.college_name,rec.college_city)))
        return res

    @api.model
    def _name_search(self,name='',args=None,operator='ilike',limit=100):
        if args is None:
            args = []
        domain = args + [('student_name',operator,name)]
        return super(StudentDetails,self).search(domain,limit=limit).name_get()

class StudentHobbies(models.Model):
    _name = 'student.hobbies'
    _description = 'Students Hobbies list'

    name = fields.Char(string="Hobbies")

class StudentEmail(models.Model):
    _inherit = 'student.details'

    email = fields.Char(string="Email")
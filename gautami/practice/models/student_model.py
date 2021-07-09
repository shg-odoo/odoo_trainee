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

    def name_get(self):
        res = []
        for analytic in self:
            name = analytic.student_name
            res.append((analytic.id, name))
        return res 

    def action_confirm(self):
        for x in self:
            students = self.env['student.details'].search([])
            print("students---------->",students)
            print("students---------->",students.ids)
            print("students---------->",students.mapped(lambda r:r.student_name))
            print("students---------->",students.sorted(lambda r:r.student_age).mapped(lambda r:r.student_name))
            print("students---------->",students.sorted(lambda r:r.student_age,reverse=True).mapped(lambda r:r.student_name))
            print("students---------->",students.filtered(lambda r:r.student_age>20 and r.student_age<30).mapped(lambda r:r.student_name))
            print("students---------->",students.default_get(['gender']))
            print("students---------->",students.read(['student_name','student_age']))
            print("students---------->",students.name_get())
            # print("students---------->",students.get_metadata())
            print("students---------->",students[3].ensure_one())
            
            

            # female_students = self.env['student.details'].search([('gender','=','female')])
            # print("female students---------->",female_students)
            
            # male_students = self.env['student.details'].search([('gender','=','male')])
            # print("male students---------->",male_students)
            
            # female_students_and_age = self.env['student.details'].search([('gender','=','female'),('student_age','>=','20')])
            # print("female students and age---------->",female_students_and_age)
            
            # female_students_or_age = self.env['student.details'].search(['|',('gender','=','female'),('student_age','>=','20')])
            # print("female students or age---------->",female_students_or_age)
            
            # cout_stud = self.env['student.details'].search_count([])
            # print("students count---------->",cout_stud)

            # cout_female_stud = self.env['student.details'].search_count([('gender','=','female')])
            # print("students female count---------->",cout_female_stud)

            # studs_browse = self.env['student.details'].browse([3,4])
            # print(studs_browse)

            # stud_browse = self.env['student.details'].browse(4)
            # if stud_browse.exists():
            #     print(stud_browse)
            #     for x in stud_browse:
            #         print(x.student_name)
            #         print("display name-------->",x.display_name)
                    
            # else:
            #     print("Record Doesn't exists")

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
        for analytic in self:
            name = analytic.college_name
            city = analytic.college_city
            res.append((analytic.id, '%s (%s)' % (name,city)))
        return res

    @api.model
    def name_create(self,college_name):
        rtn = self.create({'college_name':college_name})
        return rtn.name_get()[0]

    @api.model
    def name_search(self,name,args=None,operator='ilike',limit=100):
        args = args or []
        if name:
            records = self.search([('college_name',operator,name)])
            return records.name_get()
        return self.search([('college_name',operator,name)],limit=limit).name_get()

class StudentHobbies(models.Model):
    _name = 'student.hobbies'
    _description = 'Students Hobbies list'

    name = fields.Char(string="Hobbies")


class StudentEmail(models.Model):
    _inherit = 'student.details'

    email = fields.Char(string="Email")
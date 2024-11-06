from django.db import models

class OfferLetter(models.Model):
    salutation = models.CharField(max_length=10, default="Dear")
    name = models.CharField(max_length=100)
    email_id = models.EmailField()
    mobile = models.CharField(max_length=15)
    dob = models.DateField()
    address = models.TextField()
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    working_hours = models.CharField(max_length=50, default="9 AM - 5 PM")
    probation_period = models.CharField(max_length=50, default="Not Specified")
    company_name = models.CharField(max_length=100, default="Unknown Company")
    report_manager = models.CharField(max_length=100, default="Unknown Manager")
    manager_name = models.CharField(max_length=100, default="Unknown Manager")
    department_name = models.CharField(max_length=100, default="Unknown Department")
    benefits = models.TextField(default="No benefits specified")
    acceptance_deadline = models.DateField(null=True)



class JoiningLetter(models.Model):
    salutation = models.CharField(max_length=10, default="Dear")
    employeeName = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    joiningDate = models.DateField()
    companyName = models.CharField(max_length=100)
    managerName = models.CharField(max_length=100)

    def __str__(self):
        return self.employeeName
    

class ExperienceLetter(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    startDate = models.DateField()
    endDate = models.DateField()
    companyName = models.CharField(max_length=255)
    managerName = models.CharField(max_length=255)
    performance = models.TextField()

    def __str__(self):
        return self.name
    
class InterviewcallLetter(models.Model):
    salutation = models.CharField(max_length=10,default="Dear")
    candidateName = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    interviewDate = models.DateField()
    interviewTime = models.TimeField()
    companyName = models.CharField(max_length=255)
    contactPerson = models.CharField(max_length=255)

    def __str__(self):
        return self.candidateName
    

class PromotionLetter(models.Model):
    salutation = models.CharField(max_length=10)
    employeeName = models.CharField(max_length=100)
    currentPosition = models.CharField(max_length=100)
    newPosition = models.CharField(max_length=100)
    effectiveDate = models.DateField()
    salaryIncrement = models.DecimalField(max_digits=10, decimal_places=2)
    managerName = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)

    def __str__(self):
        return self.employeeName
    
class SalaryIncreaseLetter(models.Model):
    salutation = models.CharField(max_length=10)
    employeeName = models.CharField(max_length=255)
    currentSalary = models.DecimalField(max_digits=10, decimal_places=2)
    newSalary = models.DecimalField(max_digits=10, decimal_places=2)
    effectiveDate = models.DateField()
    managerName = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)

    def __str__(self):
        return self.employeeName
    
class TransferLetter(models.Model):
    salutation = models.CharField(max_length=10)
    employeeName = models.CharField(max_length=100)
    currentDepartment = models.CharField(max_length=100)
    newDepartment = models.CharField(max_length=100)
    newLocation = models.CharField(max_length=100)
    effectiveDate = models.DateField()
    managerName = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)

    def __str__(self):
        return self.employeeName
    

class LeaveApproval(models.Model):
    salutation = models.CharField(max_length=10, default="Mr.")
    employeeName = models.CharField(max_length=100)
    leaveType = models.CharField(max_length=50)
    startDate = models.DateField()
    endDate = models.DateField()
    managerName = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)

    def __str__(self):
        return self.employeeName
    
class ResignationLetter(models.Model):
    salutation = models.CharField(max_length=10)
    employeeName = models.CharField(max_length=100)
    resignationDate = models.DateField()
    lastWorkingDay = models.DateField()
    managerName = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)

    def __str__(self):
        return self.employeeName
    
class TerminationLetter(models.Model):
    employeeName = models.CharField(max_length=100)
    terminationDate = models.DateField()
    position = models.CharField(max_length=100)
    terminationReason = models.TextField()
    finalDetails = models.TextField()
    managerName = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)

    def __str__(self):
        return self.employeeName
    

class SeparationAgreementLetter(models.Model):
    salutation = models.CharField(max_length=10)
    employeeName = models.CharField(max_length=255)
    terminationDate = models.DateField()
    finalSettlement = models.CharField(max_length=255)
    confidentialityTerms = models.TextField()
    managerName = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)

    def __str__(self):
        return self.employeeName
    
class WarningLetter(models.Model):
    salutation = models.CharField(max_length=10)
    employee_name = models.CharField(max_length=255)
    issue_description = models.TextField()
    warning_date = models.DateField()
    consequences = models.TextField()
    manager_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)

    def __str__(self):
        return self.employee_name
    
class PerformanceReviewLetter(models.Model):
    salutation = models.CharField(max_length=10)
    employeeName = models.CharField(max_length=100)
    reviewPeriod = models.CharField(max_length=100)
    reviewSummary = models.TextField()
    strengths = models.TextField()
    areasForImprovement = models.TextField()
    managerName = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)

    def __str__(self):
        return self.employeeName
    
class ReferenceLetter(models.Model):
    salutation = models.CharField(max_length=10)
    employeeName = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    employmentPeriod = models.CharField(max_length=100)
    managerName = models.CharField(max_length=100)
    managerContact = models.CharField(max_length=20)
    managerEmail = models.EmailField()
    companyName = models.CharField(max_length=100)   

    def __str__(self):
        return self.employeeName
    

class OffLetter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    offer_date = models.DateField()
    acceptance_date = models.DateField()
    joining_date = models.DateField()
    joining_time = models.TimeField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    other_allowances = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
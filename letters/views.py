from .models import OffLetter
from django.http import JsonResponse
from django.utils.text import capfirst
from django.views.decorators.csrf import csrf_exempt
from .models import JoiningLetter
from .models import ExperienceLetter,OffLetter
from .models import InterviewcallLetter,PromotionLetter,SalaryIncreaseLetter,PerformanceReviewLetter,ReferenceLetter
from .models import TransferLetter,LeaveApproval,ResignationLetter,TerminationLetter,SeparationAgreementLetter,WarningLetter

from django.shortcuts import render, redirect

def capitalize_words(text):
    return ' '.join([word.capitalize() for word in text.split()])

#def offer_letter_view(request):
    if request.method == 'POST':
        offer_letter = OfferLetter(
            salutation=request.POST['salutation'],
            name=capitalize_words(request.POST['name']),
            email_id=request.POST['email'],
            mobile=request.POST['mobile'],
            dob=request.POST['dob'],
            address=capitalize_words(request.POST['address']),
            position=capitalize_words(request.POST['position']),
            salary=request.POST['salary'],
            start_date = request.POST['startDate'],
            working_hours=request.POST['workingHours'],
            probation_period=request.POST['probationPeriod'],
            company_name=request.POST['companyName'],
            report_manager=capitalize_words(request.POST['reportManager']),
            manager_name=capitalize_words(request.POST['managerName']),
            department_name=capitalize_words(request.POST['departmentName']),
            benefits=request.POST['benefits'],
            acceptance_deadline=request.POST['acceptanceDeadline'],
        )
        offer_letter.save()
    
    return render(request, 'offer_letter.html')



def joining_letter_view(request):
    if request.method == 'POST':
        joining_letter = JoiningLetter(
            salutation=request.POST['salutation'],
            employeeName=capitalize_words(request.POST['employeeName']),
            designation=capitalize_words(request.POST['designation']),
            department=capitalize_words(request.POST['department']),
            joiningDate=request.POST['joiningDate'],
            companyName=capitalize_words(request.POST['companyName']),
            managerName=capitalize_words(request.POST['managerName'])
        )
        joining_letter.save()
    
    return render(request, 'join_letter.html')

def index_page(request):
    return render(request, 'index.html')

def experience_letter_view(request):
    if request.method == 'POST':
        experience_letter = ExperienceLetter(
            salutation=request.POST['salutation'],
            name=capitalize_words(request.POST['name']),
            designation=capitalize_words(request.POST['designation']),
            startDate=request.POST['startDate'],
            endDate=request.POST['endDate'],
            companyName=capitalize_words(request.POST['companyName']),
            managerName=capitalize_words(request.POST['managerName']),
            performance=capitalize_words(request.POST['performance'])
        )
        experience_letter.save()

    return render(request, 'experience_letter.html')

@csrf_exempt
def interviewcall_letter_view(request):
    if request.method == 'POST':
        interviewcall_letter = InterviewcallLetter(
            salutation=request.POST['salutation'],
            candidateName=capitalize_words(request.POST['candidateName']),
            position=capitalize_words(request.POST['position']),
            interviewDate=request.POST['interviewDate'],
            interviewTime=request.POST['interviewTime'],
            companyName=capitalize_words(request.POST['companyName']),
            contactPerson=capitalize_words(request.POST['contactPerson'])
        )
        interviewcall_letter.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    return render(request, 'interviewcall_letter.html')
    

def promotion_letter_view(request):
    if request.method == 'POST':
        promotion_letter = PromotionLetter(
            salutation=request.POST['salutation'],
            employeeName=capitalize_words(request.POST['employeeName']),
            currentPosition=capitalize_words(request.POST['currentPosition']),
            newPosition=capitalize_words(request.POST['newPosition']),
            effectiveDate=request.POST['effectiveDate'],
            salaryIncrement=request.POST['salaryIncrement'],
            managerName=capitalize_words(request.POST['managerName']),
            companyName=capitalize_words(request.POST['companyName'])
        )
        promotion_letter.save()
        
    return render(request, 'promotion_letter.html')



def salary_increase_letter_view(request):
    if request.method == 'POST':
        # Capture form data and save to the database
        salary_increase_letter = SalaryIncreaseLetter(
            salutation=request.POST['salutation'],
            employeeName=capitalize_words(request.POST.get('employeeName')),
            currentSalary=request.POST.get('currentSalary'),
            newSalary=request.POST.get('newSalary'),
            effectiveDate=request.POST.get('effectiveDate'),
            managerName=capitalize_words(request.POST.get('managerName')),
            companyName=capitalize_words(request.POST.get('companyName'))
        )
        salary_increase_letter.save()  # Save data to the database
       
    return render(request, 'salaryincrease_letter.html')



def transfer_letter_view(request):
    if request.method == 'POST':
        # Capture form data and save it to the database
        transfer_letter = TransferLetter(
            salutation=request.POST['salutation'],
            employeeName=capitalize_words(request.POST.get('employeeName')),
            currentDepartment=request.POST.get('currentDepartment'),
            newDepartment=capitalize_words(request.POST.get('newDepartment')),
            newLocation=capitalize_words(request.POST.get('newLocation')),
            effectiveDate=request.POST.get('effectiveDate'),
            managerName=capitalize_words(request.POST.get('managerName')),
            companyName=capitalize_words(request.POST.get('companyName'))
        )
        transfer_letter.save()  

    return render(request, 'transfer_letter.html')


def leave_approval_view(request):
    if request.method == 'POST':
        # Capture form data and save it to the database
        leave_approval = LeaveApproval(
            salutation=request.POST['salutation'],
            employeeName=capitalize_words(request.POST.get('employeeName')),
            leaveType=capitalize_words(request.POST.get('leaveType')),
            startDate=request.POST.get('startDate'),
            endDate=request.POST.get('endDate'),
            managerName=capitalize_words(request.POST.get('managerName')),
            companyName=capitalize_words(request.POST.get('companyName'))
        )
        leave_approval.save()

    return render(request, 'leaveapproval_letter.html')

def resignation_letter_view(request):
    if request.method == 'POST':
        # Capture form data and save it to the database
        resignation_letter = ResignationLetter(
            salutation=request.POST['salutation'],
            employeeName=capitalize_words(request.POST.get('employeeName')),
            resignationDate=request.POST.get('resignationDate'),
            lastWorkingDay=request.POST.get('lastWorkingDay'),
            managerName=capitalize_words(request.POST.get('managerName')),
            companyName=capitalize_words(request.POST.get('companyName'))
        )
        resignation_letter.save()

    return render(request, 'resignation_letter.html')

def termination_letter_view(request):
    if request.method == 'POST':
        # Capture form data and save it to the database
        termination_letter = TerminationLetter(
            employeeName=request.POST.get('employeeName'),
            terminationDate=request.POST.get('terminationDate'),
            position=request.POST.get('position'),
            terminationReason=request.POST.get('terminationReason'),
            finalDetails=request.POST.get('finalDetails'),
            managerName=request.POST.get('managerName'),
            companyName=request.POST.get('companyName')
        )
        termination_letter.save()

    return render(request, 'termination_letter.html')

def separation_letter_view(request):
    if request.method == 'POST':
        
        separation_agreement_letter = SeparationAgreementLetter(
            salutation=request.POST['salutation'],
            employeeName=capitalize_words(request.POST.get('employeeName')),
            terminationDate=request.POST.get('terminationDate'),
            finalSettlement=request.POST.get('finalSettlement'),
            confidentialityTerms=capitalize_words(request.POST.get('confidentialityTerms')),
            managerName=capitalize_words(request.POST.get('managerName')),
            companyName=capitalize_words(request.POST.get('companyName'))
        )
        separation_agreement_letter.save()

    return render(request, 'separation_letter.html')

def warning_letter_view(request):
    if request.method == "POST":
        warning_letter = WarningLetter(
            salutation=request.POST['salutation'],
            employee_name=capitalize_words(request.POST.get('employeeName')),
            issue_description=capitalize_words(request.POST.get('issueDescription')),
            warning_date=request.POST.get('warningDate'),
            consequences=capitalize_words(request.POST.get('consequences')),
            manager_name=capitalize_words(request.POST.get('managerName')),
            company_name=capitalize_words(request.POST.get('companyName'))
        )
        warning_letter.save()
    return render(request, 'warning_letter.html')


def performance_letter_view(request):
    if request.method == 'POST':
        # Capture form data and save it to the database
        performance_review = PerformanceReviewLetter(
            salutation=request.POST['salutation'],
            employeeName=capitalize_words(request.POST['employeeName']),
            reviewPeriod=request.POST['reviewPeriod'],
            reviewSummary=capitalize_words(request.POST['reviewSummary']),
            strengths=capitalize_words(request.POST['strengths']),
            areasForImprovement=capitalize_words(request.POST['areasForImprovement']),
            managerName=capitalize_words(request.POST['managerName']),
            companyName=capitalize_words(request.POST['companyName'])
        )
        performance_review.save()  
    return render(request, 'performance_letter.html')

def reference_letter_view(request):
    if request.method == 'POST':
        
        reference_letter = ReferenceLetter(
            salutation=request.POST['salutation'],
            employeeName=capitalize_words(request.POST['employeeName']),
            position=capitalize_words(request.POST['position']),
            companyName=request.POST['companyName'],
            employmentPeriod=request.POST['employmentPeriod'],
            managerName=capitalize_words(request.POST['managerName']),
            managerEmail=request.POST['managerEmail'],
            managerContact=request.POST['managercontact']
        )
        reference_letter.save() 

    return render(request, 'reference_letter.html')

def index_letter_view(request):
    return render(request, 'index_letter.html')



def off_letter_view(request):
    if request.method == 'POST':
        # Creating an OfferLetter instance using POST data
        off_letter = OffLetter(
            name=request.POST.get('name'),
            location=request.POST.get('location'),
            role=request.POST.get('role'),
            manager=request.POST.get('manager'),
            offer_date=request.POST.get('date'),
            acceptance_date=request.POST.get('acceptanceDate'),
            joining_date=request.POST.get('joiningDate'),
            joining_time=request.POST.get('joiningTime'),
            salary=request.POST.get('salary'),
            hra=request.POST.get('hra'),
            other_allowances=request.POST.get('other-allowances')
        )
        # Saving the form data to the database
        off_letter.save()

    return render(request, 'off_letter.html')

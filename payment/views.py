from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, Template,RequestContext
import datetime
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required,user_passes_test
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators import csrf
from recruit.models import *
from registration.models import *
#from django.core.context_processors import csrf
import Config as config
import datetime

def home():
    data = {}
    return render(request, "payment/home.djt", data)

@login_required(login_url='/register')
def GoToTransaction(request):
    MERCHANT_KEY = config.KEY
    key = config.KEY
    SALT = config.SALT
    PAYU_BASE_URL = config.PAYU_BASE_URL
    action = ''
    posted={}
    profile = UserProfile.objects.get(user=request.user)
    posted["firstname"] = request.user.first_name
    posted["email"] = request.user.email
    posted["phone"] = profile.contact
    # Merchant Key and Salt provided y the PayU.
    for i in request.POST:
        posted[i]=request.POST[i]
        #print posted[i]
    hash_object = hashlib.sha256(str(randint(0,9999)).encode("utf-8"))
    txnid=hash_object.hexdigest().lower()[0:32]
    hashh = ''
    posted['txnid'] = txnid
    posted["pdate"] = str(datetime.datetime.now().date())
    hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
    posted['key']=key
    posted["surl"] = config.PAYU_SUCCESS_URL
    posted["furl"] = config.PAYU_FAILURE_URL
    
    hash_string=''
    hashVarsSeq=hashSequence.split('|')
    for i in hashVarsSeq:
        try:
            hash_string+=str(posted[i])
        except Exception:
            hash_string+=''
        hash_string+='|'
    hash_string+=SALT
    hashh=hashlib.sha512(hash_string).hexdigest().lower()
    action =PAYU_BASE_URL
    data = {"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":PAYU_BASE_URL }
    data1= {"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"." }
    if(posted.get("key")!=None and posted.get("txnid")!=None and posted.get("productinfo")!=None and posted.get("firstname")!=None and posted.get("email")!=None):
        #print "Dummy Code ",posted.get("key")," - ", posted.get("txnid")," - ",posted.get("productinfo")," - ",posted.get("firstname")," - ",posted.get("email")
        print "Hello ",hash_string, " ",posted.get("phone")
        pay_data = PaymentDetails.objects.get(appID=profile.applicationID)
        pay_data.payType = posted.get('paytype')
        if pay_data.payType == 'SC/ST/PWD':
            pay_data.amount = 'Rs.0'
        elif pay_data.payType == 'GEN/OBC':
            pay_data.amount = 'Rs.1000'
        elif pay_data.payType == 'abroad':
            pay_data.amount = '$25'
        pay_data.save()
        if(posted["amount"] == "0"):
           app_data = Appdata.objects.get(user=request.user)
           app_data.paymentUploaded = True
           app_data.save()
           return redirect("/")
        return render(request,'payment/paynow.html',data)
    else:
    	print posted.get("key")," - ", posted.get("txnid")," - ",posted.get("productinfo")," - ",posted.get("firstname")," - ",posted.get("email")
        return render(request,'payment/paynow.html',data1)
    #return render(request,'payment/current_datetime.html',data)
   
@csrf_protect
@csrf_exempt
@login_required(login_url='/register')
def success(request):
    c = {}
    #c.update(csrf(request))
    app = Appdata.objects.get(user=request.user)
    status=request.POST["status"]
    firstname=request.user.first_name
    amount=request.POST["amount"]
    txnid=request.POST["txnid"]
    posted_hash=request.POST["hash"]
    key=request.POST["key"]
    productinfo=request.POST["productinfo"]
    email=request.user.email
    print firstname,"--",amount,"--",posted_hash,"--",email 
    salt=""
    response = {}
    profile = UserProfile.objects.get(user=request.user)
    pay_data = PaymentDetails.objects.get(appID=profile.applicationID)
    
    response['paydata'] = pay_data
    if request.method == 'POST' :
        pay_data.bankName = ''
        pay_data.accountNum = ''
        pay_data.transID = txnid
        pay_data.payDate = str(datetime.datetime.now())
        # pay_data.payType = 'payType'
        # if pay_data.payType == 'SC/ST/PWD':
        #     pay_data.amount = 'Rs.500'
        # elif pay_data.payType == 'GEN/OBC':
        #     pay_data.amount = 'Rs.1000'
        # elif pay_data.payType == 'abroad':
        #     pay_data.amount = '$25'
        
        pay_data.save()
        app_data = Appdata.objects.get(user=request.user)
        app_data.paymentUploaded = True
        app_data.save()
        
        #return redirect('/')

    try:
        additionalCharges=request.POST["additionalCharges"]
        retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    except Exception:
        retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
    hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
    if(hashh !=posted_hash):
        print "Invalid Transaction. Please try again"
    else:
        print "Thank You. Your order status is ", status
        #print "User Is ",request.User
        print "Your Transaction ID for this transaction is ",txnid
        print "We have received a payment of Rs. ", amount ,". Your order will soon be shipped."
    return render(request,'payment/success.html',{"UserId":app.app_id,"txnid":txnid,"status":status,"amount":amount})


@csrf_protect
@csrf_exempt
def failure(request):
    c = {}
    #c.update(csrf(request))
    return render(request,"payment/Failure.html",c)

    

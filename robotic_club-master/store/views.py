from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from store.forms import ItemForm,CartForm
from basic_app.models import UserProfile
from .models import Item_discription,Request_item,Cart
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings
# Create your views here.
@login_required
def add_item(request):

	if request.method=="POST":
		form = ItemForm(request.POST,request.FILES)
		mentor = UserProfile.objects.filter(user=request.user).values("is_mentor")
		mentor = mentor[0]['is_mentor']
		if mentor:
			if form.is_valid():
				user_ = form.save(commit=False)
				user_.user = request.user
				form.save()
            
			return HttpResponse("cool your stuff is uploaded ")
		else:
			return HttpResponse("please contect kanishk for your aproval as mentor")
	else:
		 form = ItemForm()

		 return render(request,'add_item.html',{'form':form})

 

def item_view(request):

	items = Item_discription.objects.all()
	return render(request,'item_view.html',{'items':items})

# def item_detail(request,pk):
#     if request.method == 'POST':
    	
    	
#     	item = Item_discription.objects.get(pk=pk)
#     	item.requested()
#     	item1 = Item_discription.objects.filter(pk=pk).values('user')

#     	item2 = Item_discription.objects.filter(pk=pk).values('text')
#     	u=item1[0]['user']
#     	t=item2[0]['text']
#     	item1 = User.objects.get(pk=u)


#     	Request_item.objects.create(user=item1,text=t,requesting_user=request.user.username,first=request.user.first_name,last=request.user.last_name)
#     	mail=str(item1.email)
#     	lsi=[]
#     	lsi.append(mail)
#     	name = request.user.first_name+" "+request.user.last_name
#     	email(lsi,t,name,request.user.username)
#     	return HttpResponse("request made")

#     else:


	
# 	    item = Item_discription.objects.get(pk=pk)
# 	    return render(request,"item_detail.html",{'item':item})


def email(lis,text,text1,username):
    subject = 'hey mentor someone want your help'
    message = subject+"\n"+text+"\nrequested by "+text1+"\n"+username+"\n\n RoboticsClub\n\nplease contact kanishk CSE 3rd yr for any inconvenience\nkanishksinghal2@gmail.com"
    print(message)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = lis
    send_mail( subject, message, email_from, recipient_list )

@login_required
def item_detail(request,pk):
    print("got request")


    if request.method == 'POST' and int(request.POST['amount'])>0:
        
        form = CartForm(request.POST)
        if form.is_valid():
            item = Item_discription.objects.get(pk=pk)
            print(request.POST['amount'])
            if item.amount >= int(request.POST['amount']):
                item1 = Item_discription.objects.filter(pk=pk).values('user')

                item2 = Item_discription.objects.filter(pk=pk).values('text')
                u=item1[0]['user']
                t=item2[0]['text']
                product_name = Item_discription.objects.filter(pk=pk).values('product_name')
                product_name=product_name[0]['product_name']
                photo = Item_discription.objects.filter(pk=pk).values('photo1')
                photo = photo[0]['photo1']
                item1 = User.objects.get(pk=u)
        

                Cart.objects.create(user=item1,text=t,requesting_user=request.user.username,
                    first=request.user.first_name,last=request.user.last_name, amount=request.POST['amount'],dis_id=pk,product_name=product_name,photo1=photo)
                data = {
                "request":True
                }
                return JsonResponse(data)
                
            else:
                data = {

                     "message":"amount not valid"
                     }
                return JsonResponse(data)
                
        data = {
                     
                "message":"form not valid"
                }
        return JsonResponse(data)
        

    else:


        
        item = Item_discription.objects.get(pk=pk)
        photo1=str(item.photo1)
        photo2=str(item.photo2)
        text=item.text
        amount=item.amount
        url = settings.MEDIA_URL+photo1
        print(url)
      
        data = {
            "working":True,
            
            "amount":amount,
            "text":text,
            "photo1":url,
            "photo2":photo2,
            "product_name":item.product_name

            }
        return JsonResponse(data)
        
    


@login_required
def delete_item(request,pk):

    item = Item_discription.objects.filter(pk=pk).values("text")
    
    cart = Cart.objects.filter(requesting_user=request.user)
    print(cart)

    cart = cart.filter(text=item[0]['text'])
    if cart:
        

        cart[0].delete()
        item = Item_discription.objects.get(pk=pk)
        item.add_
    
        return HttpResponseRedirect("/index/request_mentor/")
    return HttpResponse("item not present")



@login_required
def request_mentor(request):

    if request.method == "POST":
        items = Cart.objects.filter(requesting_user=request.user)
        inform=""
        recipients = {}

        if Cart.objects.filter(requesting_user=request.user).exists() == False:
            return HttpResponse("cart empty")

        listx={}
        for  item in items:
            amt_obj = Item_discription.objects.get(pk=item.dis_id)
            if amt_obj.requested(item.amount):

                Request_item.objects.create(user=item.user,text=item.text,requesting_user=item.requesting_user,
                        first=item.first,last=item.last, amount=item.amount,dis_id=item.dis_id,product_name=item.product_name)
                if item.user in recipients:
                    # recipients[item.user] = (recipients[item.user] +" "+item.text+" "+str(item.amount)
                    recipients[item.user] = ("%s \n%d. %s  %d" %(recipients[item.user],listx[item.user],item.text,item.amount))
                    listx[item.user] +=1

                else:
                    recipients[item.user] = ("1. %s %d " %(item.text,item.amount))
                    listx[item.user] = 2
                



            else:
                inform = inform +"<br>" +item.text +" request cant be made"
            item.delete()
        print(recipients)

#         request_mail(recipients,request.user)


        return render(request, "successful.html",{})
        return HttpResponse("working"+inform)

    else:
        items = Cart.objects.filter(requesting_user=request.user)
        if not items:
            empty = 1;
        else:
            empty = 0;
        return render(request,"request_mentor.html",{'items':items, 'empty':empty})



def request_mail(dict,request_by):
   
    

    for user_obj in dict:
        recipient=str(user_obj.email)
        recipients_list=[]
        recipients_list.append(recipient)


        text = dict[user_obj]
        text1 = request_by.first_name + " " + request_by.last_name
        email(recipients_list,text,text1,str(request_by.username))
    

    

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,CreateView
from .models import Toko
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, get_object_or_404
from .forms import CreateBatchForm
from django.http import HttpResponse 
import numpy as np
from django.contrib import messages
import json
from django.template.response import TemplateResponse

@method_decorator([login_required], name='dispatch') 
class CreateBatch(SuccessMessageMixin, TemplateView):
    model = Toko
    template_name = 'toko/create_batch.html'
    fields ='__all__'
    # success_message = 'Added Successfully!'
    # error_message = "Failed Login"
    success_url = reverse_lazy('create_batch')
    form_class = CreateBatchForm
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)        
        form = CreateBatchForm()        
        context["form"] = form
        return context
    
    # def form_valid(self, form):
    #     form = CreateBatchForm(self.request.POST, (self.request.FILES))
    #     messages.success(self.request, f"{self.request.user.first_name} {self.request.user.last_name} , Create Batch")
    #     print("waduhhhhhh")
    #     return HttpResponseRedirect(self.request.path_info)
    
    def post(self, request, **kwargs):
        action = self.request.POST['action']
        cabang = self.request.POST['cabang']
        passtoko = self.request.POST['passtoko']
        kdtk = self.request.POST['kdtk']
        query = self.request.POST['query']
        nama_file = self.request.POST['nama_file']
                
        if request.method == 'POST':
            kdtks = Toko.objects.all()
            count = kdtks.count()
            array = kdtks.values_list('kdtk','ip')
            form = CreateBatchForm(request.POST, request.FILES)
            # mess = messages.success(request, f"{request.user.first_name} {request.user.last_name} , Create Batch")
            if cabang == 'g117':
                array = kdtks.values_list('kdtk','ip').filter(cabang_id='1')      
                numpy_array = np.array(list(array))      
                list_bat =[]
                for kdtkk,ipp in numpy_array:
                    bat = f"Mysql -uroot -p{passtoko}  -h{ipp} -Dpos -B -e \"{query}\"     |sed.exe s/\\t/\"|\"/g;s/^/\"/;s/$/\"/;s/\\n//g  > batch_{kdtkk[0:1]}.{kdtkk[1:4]}";
                    list_bat.append(f'{bat}\n')

                response = HttpResponse(content_type='text/plain')
                response['Content-Disposition'] = f'attachment; filename=tembak.txt'
                response.writelines(list_bat)
                response.close()
                
                response1 = HttpResponse(content_type='text/plain')
                response1['Content-Disposition'] = f'attachment; filename=tembak2.txt'
                response1['Content-Disposition'] = f'attachment; filename=tembak1.txt'
                response1.writelines(list_bat)
                response1.close()
                
                # response = HttpResponse(content_type='text/plain')
                # response['Content-Disposition'] = f'attachment; filename=tembak1.txt'
                # response.writelines(list_bat)
                # response.close()
                # self.status_code = int(status)
      

             
                    
                # print(response)
               
                  
                
            elif cabang == 'g113':
                array = kdtks.values_list('kdtk','ip').filter(cabang_id='2')      
                numpy_array = np.array(list(array))      
                list_bat =[]
                for kdtkk,ipp in numpy_array:
                    bat = f"Mysql -uroot -p{passtoko}  -h{ipp} -Dpos -B -e \"{query}\"     |sed.exe s/\\t/\"|\"/g;s/^/\"/;s/$/\"/;s/\\n//g  > batch_{kdtkk[0:1]}.{kdtkk[1:4]}";
                    list_bat.append(f'{bat}\n')
                response = HttpResponse(content_type='text/plain')
                response['Content-Disposition'] = f'attachment; filename=tembak1.txt'
                response.writelines(list_bat)
                response.close()
                
                response1 = HttpResponse(content_type='text/plain')
                response1['Content-Disposition'] = f'attachment; filename=tembak2.txt'
                response1.writelines(list_bat)
                response1.close()
                  
            else:
                print("G113 invalid")              
        # return response
        # return render(request, self.template_name, {'form': form})
        # return render_to_response()
        # return render(request, self.template_name, {'response': response},
        #                     content_type="text/plain")
        return response
        

    
           

class AddToko(SuccessMessageMixin, CreateView):
    model = Toko
    template_name = 'toko/add_toko.html'
    fields ='__all__'
    success_message = 'Added Successfully!'
    success_url = reverse_lazy('add_toko')
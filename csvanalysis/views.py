from django.shortcuts import render, redirect
from .forms import *
from .models import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


def upload_file(request):
    if request.method == 'POST':  
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
             form.save()
             return redirect('fileupload:process_file', file_id=upload_file.id)
    else:
        form = UploadFileForm()
    
    return render(request, 'upload.html', {'form': form})



def process_file(request, file_id):
    file = get_object_or_404(YourModel, id=file_id)
    file_path = uploaded_file.file.path


     # Read the CSV file
    df = pd.read_csv(file_path)

    # Perform csv files
    data_head = df.head().to_html()
    data_description = df.describe().to_html()
    missing_values = df.isnull().sum().to_html()
    

    # Generate visualizations
    plots = []
    os.makedirs(os.path.join('media', 'plots'), exist_ok=True)
    for column in df.select_dtypes(include=['number']).columns:
        plt.figure()
        sns.histplot(df[column], kde=True)
        plot_path = os.path.join('media', 'plots', f'{column}_hist.png')
        plt.savefig(plot_path)
        plt.close()
        plots.append(plot_path)

    context = {
        'data_head': data_head,
        'data_description': data_description,
        'missing_values': missing_values,
        'plots': plots,
    }
    return render(request, 'fileupload/results.html', context)
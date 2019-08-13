from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from . import models


# Create your views here.
def index(request):
    storageinfo = models.Asset.objects.all()
    return render(request, 'StorageInfo/index.html', locals())

def dashboard(request):
    total = models.Asset.objects.count()
    upline = models.Asset.objects.filter(status=0).count()
    offline = models.Asset.objects.filter(status=1).count()
    unknown = models.Asset.objects.filter(status=2).count()
    breakdown = models.Asset.objects.filter(status=3).count()
    backup = models.Asset.objects.filter(status=4).count()
    up_rate = round(upline/total*100)
    o_rate = round(offline/total*100)
    un_rate = round(unknown/total*100)
    bd_rate = round(breakdown/total*100)
    bu_rate = round(backup/total*100)
    storagedevice_number = models.StorageDevice.objects.count()
    sanswitch_number = models.SanSwitch.objects.count()
    return render(request, 'StorageInfo/dashboard.html', locals())

def detail(request, asset_id):
    asset = get_object_or_404(models.Asset, id=asset_id)
    return render(request, 'StorageInfo/detail.html', locals())

def storagedetail(request, asset_id):
    asset = get_object_or_404(models.Asset, id=asset_id)
    return render(request, 'StorageInfo/storagedetail.html', locals())

def sanswitchdetail(request, asset_id):
    asset = get_object_or_404(models.Asset, id=asset_id)
    return render(request, 'StorageInfo/sanswitchdetail.html', locals())

def maintenance(request):
    storageinfo = models.Asset.objects.all()
    return render(request, 'StorageInfo/maintenance.html', locals())

def asset_coding(request):
    storageinfo = models.Asset.objects.all()
    return render(request, 'StorageInfo/asset_coding.html', locals())
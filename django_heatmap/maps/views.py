from django.shortcuts import render

# Create your views here.

#make Heatmap
import sys
import folium
from folium.plugins import HeatMap
import csv
import pandas as pd


from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt


def index(request):

    return render(request, 'index.html')


def calc(request):

    val1 = int(request.POST['val1'])
#    val2 = int(request.POST['val2'])
#    answer = val1 + val2
#    context = {
#        'answer': answer,
#    }

    print('answer=' + str(val1))

    csvfile = 'data/org_PV_20200508.csv'
    map_data = pd.read_csv(csvfile, header=0)

    # プロットするデータのリスト
    lon_data = map_data.iloc[:,0]
    lat_data = map_data.iloc[:,1]
    PV_data = map_data.iloc[:,2]

    map_data_index = 0

    ############
    # 7 colors
    ############
    map_data549 = []#350~549
    map_data550 = []#550~699
    map_data700 = []#700~849
    map_data850 = []#850~1000
    map_data1000 = []#1000~1150
    map_data1150 = []#1150~1300
    map_data1300 = []#1300~1500

    for w in PV_data:

	    if w < 550:
		    PV_temp = (w - 350) / 200
		    map_data549.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= 550 and w < 700:
		    PV_temp = (w - 550) / 150
		    map_data550.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= 700 and w < 850:
		    PV_temp = (w - 700) / 150
		    map_data700.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= 850 and w < 1000:
		    PV_temp = (w - 850) / 150
		    map_data850.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= 1000 and w < 1150:
		    PV_temp = (w - 1000) / 150
		    map_data1000.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= 1150 and w < 1300:
		    PV_temp = (w - 1150) / 150
		    map_data1150.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])
    	
	    elif w >= 1300:
		    PV_temp = (w - 1300) / 200
		    map_data1300.append([lon_data[map_data_index],lat_data[map_data_index], PV_temp ])

	    else:
		    print ('???')

	    map_data_index = map_data_index + 1


    #緯度・経度
    # 地図の中心をセット
    #world_map = folium.Map(location=[36, 140],zoom_start=1)
    world_map = folium.Map(location=[0, 0],zoom_start=1)
    #world_map = folium.Map([48, 5], tiles='stamentoner', zoom_start=6)

    # データをヒートマップとしてプロット
    Radius_temp = 7
    Blur_temp = 20

    HeatMap(map_data549, name = '549PVポテンシャル_20200508',gradient={1:'gray'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data550, name = '550PVポテンシャル_20200508',gradient={1:'blue'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data700, name = '700PVポテンシャル_20200508',gradient={1:'yellowgreen'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data850, name = '850PVポテンシャル_20200508',gradient={1:'green'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data1000, name = '1000PVポテンシャル_20200508',gradient={1:'yellow'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data1150, name = '1150PVポテンシャル_20200508',gradient={1:'orange'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)
    HeatMap(map_data1300, name = '1300PVポテンシャル_20200508',gradient={1:'red'},radius=Radius_temp, blur=Blur_temp,max_val=1, max_zoom=18).add_to(world_map)

    # HTMLを出力
    #world_map.save('PV_heatmap.html')

    #return render(request, 'index.html', context)
    return render(request, 'index.html')

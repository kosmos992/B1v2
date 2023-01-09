import math
import requests
import json
import time

from json import loads

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from mapapp.models import Cctv

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, 'mapapp/index.html')

    cctvs = Cctv.objects.all()


    cctv_list = []  # 모든 CCTV 정보

    open_list = []  # 시작 노드로부터 가장 가까운 5개 CCTV의 정보
    closed_list = []  # 필요없는 CCTV id - open_list 검사용

    cctv_passing = []  # 반환값. 최단 거리 CCTV 정보

    cctv_count = 0
    walk_distance = 0

    test_coords = []
    if (request.method == 'POST'):
        data = json.loads(request.body)
        start_lat = data['s_lat']
        start_long = data['s_lon']
        end_lat = data['e_lat']
        end_long = data['e_lon']
        test_coords.append(start_lat)
        test_coords.append(start_long)
        test_coords.append(end_lat)
        test_coords.append(end_long)

        print(test_coords)

        ######################무한반복문 말고 10번만 해보기 (호출 개수 초과) ###########################################
        #시작노드에서부터 가장 가까운 5개의 CCTV 까지의 거리를 open_list에 저장
        for i in range(0, 10):
            for cctv in cctvs:
                cctv_list.append([cctv.id, math.sqrt(math.pow(float(cctv.latitude) - start_lat, 2) + math.pow(float(cctv.longtitude) - start_long, 2)), cctv.longtitude, cctv.latitude, cctv.address])

            cctv_list.sort(key=lambda x: x[1])


            open_list = []
            #open_list에 closed_list에 있는 CCTV를 제외한 cctv 추가
            for cctv in cctv_list:
                if cctv_count == 5:
                    break
                elif cctv[0] in closed_list:
                    continue
                else:
                    open_list.append(cctv)
                    cctv_count += 1

            cctv_count=0
            #############################################################################


            # open_list의 cctv를 하나씩 검사해서, 최단거리 cctv 정보를 cctv_passing에 저장하고, 해당 cctv id를 closed_list에 저장
            #   1. 각 노드에서 목적지까지의 직선 거리 구하기
            temp_list = []
            for cctv in open_list:
                line_distance = math.sqrt(
                    math.pow(float(cctv[3]) - float(start_lat), 2) + math.pow(float(cctv[2]) - float(start_long),2))

                walk_distance = int(requestAPI(cctv[2], cctv[3], end_long, end_lat))

                total_distance = line_distance + walk_distance
                temp_list.append([cctv[0], float(cctv[2]), float(cctv[3]), total_distance, walk_distance])

                time.sleep(0.25)

            temp_list.sort(key=lambda x: x[3])
            cctv_passing.append(temp_list[0])
            closed_list.append(temp_list[0][0])

            start_long = float(temp_list[0][1])
            start_lat = float(temp_list[0][2])

            cctv_list = []
            if cctv_passing[-1][-2] < 100:
                break;
        print(cctv_passing)

        return JsonResponse(cctv_passing, safe=False)

def requestAPI(start_long, start_lat, end_long, end_lat):
    url = "https://apis.openapi.sk.com/tmap/routes/pedestrian?version=1&format=json&callback=result"

    start_name = "출발지"

    end_name = "도착지"

    data = {
        "appKey": "l7xx799fb381535144889be4ad26a3c1a910",
        "startX": start_long,
        "startY": start_lat,
        "endX": end_long,
        "endY": end_lat,
        "startName": "출발지",
        "endName": "도착지"
    }

    res = requests.post(url, data=data)

    jsonObj = json.loads(res.text)

    totalDistance = str(jsonObj.get("features")[0].get("properties").get("totalDistance"))

    return totalDistance
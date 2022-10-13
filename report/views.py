# from django.shortcuts import render, redirect
# # from .forms import *
# # from .models import *

# # Create your views here.

# from django.http import Http404
# from django.core.paginator import Paginator
# import pymysql
# import pandas as pd



# def board_list(request):
#     userform = request.session.get('user')

#     conn = pymysql.connect(
#                     user='root',
#                     passwd='pass',
#                     host='15.165.221.104',
#                     port=53601,
#                     db='sgcamweb'
#                 )
    
#     curs = conn.cursor()
#     sql = "select * from web_info where username = " + "'"+userform+"'"+";"
#     # id 정보를 추가로 넘겨줘야 함

#     curs.execute(sql)
#     row = curs.fetchall()

#     auth_bridge = row[0][4]
#     if auth_bridge:
#         auth_list = auth_bridge.split(',')
        
#     bridge_list = []     

# #     boards = Board.objects.all().order_by('-id')

#     if (auth_list[0] == 'admin'):
#         curs1 = conn.cursor()
#         sql1 = "select * from bridge_info;"
#         # id 정보를 추가로 넘겨줘야 함

#         curs1.execute(sql1)
#         bridge_list = curs1.fetchall()
#     else:
#         for brid in auth_list:   
#             curs1 = conn.cursor()
#             sql1 = "select * from bridge_info where name = " + "'"+brid+"'"+";"
#             # id 정보를 추가로 넘겨줘야 함

#             curs1.execute(sql1)
#             row1 = curs1.fetchall()
#             if row1:
#                 print(row1[0])
#                 bridge_list.append(row1[0])
    

#     return render(request, 'main.html', {'bridge_list': bridge_list})


# # def board_detail(request, pk):
# #     # 사용 안 함
# #     try:
# #         board = Board.objects.get(pk=pk)
# #     except Board.DoesNotExist:
# #         raise Http404('게시글을 찾을 수 없습니다')

# #     return render(request, 'detail.html', {'board': board})


# # def board_map(request, latitude, longitude):

# #     if request.session.get('user'):

# #         userform = request.session.get('user')

# #         conn = pymysql.connect(
# #                     user='root',
# #                     passwd='pass',
# #                     host='15.165.221.104',
# #                     port=53601,
# #                     db='sgcamweb'
# #                 )
# #         curs = conn.cursor()
# #         sql = "select * from web_info where username = " + "'"+userform+"'"+";"
# #         # id 정보를 추가로 넘겨줘야 함

# #         curs.execute(sql)
# #         row = curs.fetchall()

# #         auth_bridge = row[0][4]
# #         auth_list = auth_bridge.split(',')
        
# #         curs1 = conn.cursor()
# #                 # select * from bridge_info where latitude = 111               and longitude = 111;
# #         sql1 = "select * from bridge_info where latitude = "+str(latitude)+ " and longitude = "+str(longitude)+ ";"
# #         # id 정보를 추가로 넘겨줘야 함

# #         curs1.execute(sql1)
# #         row1 = curs1.fetchall()
        
# #         name = row1[0][2]
        
        

# #         for bridge in auth_list:
# #             if bridge == name or bridge == 'admin':
# #                 return render(request, 'map.html', {'latitude': latitude, 'longitude': longitude})

# #         raise Http404('권한이 없습니다!')

# #     return redirect('/breezyuser/login/')
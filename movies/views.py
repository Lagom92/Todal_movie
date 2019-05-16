from django.shortcuts import render
import requests
import os
from .models import Movie
from .forms import SearchForm,MovieForm,CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

# 영화 데이터 수집용 페이지 - 사용자는 알 필요없음
def moviePickUp(request):
     # the movie db key
    TMD_KEY = "24df7a2f9bd1e573801cee80414af820"
    
    # 영화 list url
    LIST_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMD_KEY}&language=ko-kr"
    listData = requests.get(LIST_URL)
    resDatas = listData.json().get('results')
    
    for resData in resDatas:
        # 영화의 TMD id
        tmd_id = resData.get('id')
        # 영화 detail url
        DETAIL_URL = f"https://api.themoviedb.org/3/movie/{tmd_id}?api_key={TMD_KEY}&language=ko-kr"
        # json 파일 가져옴
        detailData = requests.get(DETAIL_URL)
        # 영화 회사정보
        resDetailData = detailData.json()['production_companies']
        if resDetailData:
            company = resDetailData[0]['name']
        else:
            # 영화 회사 정보가 없는 경우
            company = ""
   
        Movie.objects.get_or_create(
            title = resData.get('title'),
            poster_path = "https://image.tmdb.org/t/p/w500"+ resData.get('poster_path'),
            homepage = detailData.json()['homepage'],
            overview = detailData.json()['overview'],
            release_date = detailData.json()['release_date'],
            genre = detailData.json().get('genres')[0].get('name'),
            production_company = company,
            tmd_id = tmd_id,
            )
    return render(request, 'movies/moviePickUp.html')


def main(request):
    movies = Movie.objects.all()
    
    # search기능 ############################################
    movie = Movie.objects.all()
    # GET request의 인자중에 searchword값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if request.method=="GET":
        searchword = request.GET.get('searchword','')
        resultMovie = []
        
        if searchword: #searchword가 있다면
            searchMovie = movie.filter(title__contains=searchword) #제목에 searchword가 포함된 레코드만 필터링
            if searchMovie:
                # 영화 여러개 저장위해 데이터의 개수 
                movie_count = searchMovie.count()
                for c in range(movie_count):
                    # 데이터들 resultMovie리스트에 저장
                    resultMovie.append({searchMovie[c].title:searchMovie[c].id})
                    # 디테일 페이지 이동위해 id값도 넘겨준다
                return render(request,'movies/searchresult.html',{'movie':movie,'searchMovie':searchMovie,'resultMovie':resultMovie})
            else:
                #아무것도 입력하지 않는다면,
                return render(request,'movies/searchresult.html',{'resultMovie':resultMovie})

        return render(request, 'movies/main.html', {'movies':movies})
    #mainpage에서는 
    #<검색기능>작품의 제목,배우,감독을 검색해 해당 영화의 디테일 페이지로 연결하는 역할을 한다.
    # 일단 작품의 제목으로 검색하는 것을 구현 
    #<로그인버튼>
    #############################################################################3
    
    

def detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movies/detail.html', {'movie':movie})


def search(request):
    movie = Movie.objects.all()
    # GET request의 인자중에 searchword값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if request.method=="GET":
        searchword = request.GET.get('searchword','')
        resultMovie = []
        
        if searchword: #searchword가 있다면
            searchMovie = movie.filter(title__contains=searchword) #제목에 searchword가 포함된 레코드만 필터링
            if searchMovie:
                # 영화 여러개 저장위해 데이터의 개수 
                movie_count = searchMovie.count()
                for c in range(movie_count):
                    # 데이터들 resultMovie리스트에 저장
                    resultMovie.append({searchMovie[c].title:searchMovie[c].id})
                    # 디테일 페이지 이동위해 id값도 넘겨준다
                return render(request,'movies/searchresult.html',{'movie':movie,'searchMovie':searchMovie,'resultMovie':resultMovie})
            else:
                #아무것도 입력하지 않는다면,
                return render(request,'movies/searchresult.html',{'resultMovie':resultMovie})

        return render(request,'movies/search.html')
    #mainpage에서는 
    #<검색기능>작품의 제목,배우,감독을 검색해 해당 영화의 디테일 페이지로 연결하는 역할을 한다.
    # 일단 작품의 제목으로 검색하는 것을 구현 
    #<로그인버튼>

@login_required
def commentCreate(request,id):
#   # 댓글 작성 폼을 list에서 보여줌.
    pass
    
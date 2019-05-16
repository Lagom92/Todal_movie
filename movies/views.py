from django.shortcuts import render,redirect, get_object_or_404
import requests
import os
from .models import Movie,Comment,Score
from .forms import SearchForm,MovieForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# 영화 데이터 수집용 페이지 - 사용자는 알 필요없음
def moviePickUp(request):
    # the movie db key
    TMD_KEY = os.getenv('TMD_KEY')
    
    # 영화 리스트를 여러 페이지 가져오기
    for n in range(1, 6):
        num = str(n)
        # 영화 목록 url
        LIST_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMD_KEY}&language=ko-KR&page={num}"
        listData = requests.get(LIST_URL)
        resDatas = listData.json().get('results')
    
        for resData in resDatas:
            # 영화의 TMD id
            tmd_id = resData.get('id')
            # 영화 detail url
            DETAIL_URL = f"https://api.themoviedb.org/3/movie/{tmd_id}?api_key={TMD_KEY}&language=ko-KR"
            detailData = requests.get(DETAIL_URL)
            # 영화 감독 //
            CREDITS_URL = f"https://api.themoviedb.org/3/movie/{tmd_id}/credits?api_key={TMD_KEY}"
            creditsData = requests.get(CREDITS_URL)
            resdirectors = creditsData.json().get('crew')
            
            for n in range(5):
                # job이 Director인 사람의 이름 찾기
                if resdirectors[n].get('job') =='Director':
                    director = resdirectors[n].get('name')
                    break
                else:
                    director = ""
            # // 영화 감독
            
            # 영화 회사정보
            resDetailData = detailData.json().get('production_companies')
            if resDetailData:
                company = resDetailData[0].get('name')
            else:
                # 영화 회사 정보가 없는 경우
                company = ""

            # 홈페이지가 있는경우와 없는 경우 구분
            # print(detailData.json().get('homepage'))
            if detailData.json().get('homepage') != None :
                homepage =  detailData.json().get('homepage')
                # print(homepage)
            else:
                homepage = ""
                
            # 장르가 있는지 없는지
            if detailData.json().get('genres'):
                genre = detailData.json().get('genres')[0].get('name')
            else:
                genre = ""
            
            Movie.objects.get_or_create(
                title = resData.get('title'),
                backdrop_path = "https://image.tmdb.org/t/p/original" + resData.get('backdrop_path'),
                poster_path = "https://image.tmdb.org/t/p/original"+ resData.get('poster_path'),
                overview = detailData.json().get('overview'),
                release_date = detailData.json().get('release_date'),
                genre = detailData.json().get('genres')[0].get('name'),
                production_company = company,
                tmd_id = tmd_id,
                director = director,
                homepage = homepage,
                )
    return render(request, 'movies/moviePickUp.html')


def main(request):
    # pagination //
    movie_list = Movie.objects.all()
    paginator = Paginator(movie_list, 20) # Show 20 contacts per page
    page = request.GET.get('page')
    try:
        movies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        movies = paginator.page(paginator.num_pages)
    # // pagination
    
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
                    # 원본 주석처리
                    # resultMovie.append({searchMovie[c].title:searchMovie[c].id})
                    resultMovie.append({'title':searchMovie[c].title, 'id':searchMovie[c].id})
                    # 디테일 페이지 이동위해 id값도 넘겨준다
                # print(resultMovie)
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
    # # 댓글 폼
    comment_form = CommentForm()
    ratings = 0
    # 평점
    for score in movie.score_set.all():
        ratings += score.rating
    if ratings == 0:
        ratingAvg = 0
    else:
        ratingAvg = ratings/movie.score_set.all().count()
    ratingAvg = round(ratingAvg,2)
    
    
    # 추천 영화 보여주기 //
    TMD_KEY = os.getenv('TMD_KEY')    
    RECOMMEND_URL = f"https://api.themoviedb.org/3/movie/{movie.tmd_id}/recommendations?api_key={TMD_KEY}&language=ko-KR"
    recommendData = requests.get(RECOMMEND_URL)
    resRecommends = recommendData.json().get('results')

    # 영화 추천 //
    # 추천 영화가 5개보다 작을때와 클때로 구분
    res = []
    if (len(resRecommends) > 5):
        for i in range(5):
            ig = "https://image.tmdb.org/t/p/w500" + resRecommends[i].get('poster_path')
            url = resRecommends[i].get('id')
            if Movie.objects.filter(tmd_id=url):
                # 추천 영화가 db에 있다면
                recommend = Movie.objects.get(tmd_id=url)
                ul = recommend.id
            else:
                # 없으면 현재 페이지 영화 id 사용
                ul = id
            res.append({'ig':ig, 'ul':ul})
    else:
        for j in range(len(resRecommends)):
            ig = "https://image.tmdb.org/t/p/w500" + resRecommends[j].get('poster_path')
            url = resRecommends[j].get('id')
            if Movie.objects.filter(tmd_id=url):
                # 추천 영화가 db에 있다면
                recommend = Movie.objects.get(tmd_id=url)
                ul = recommend.id
            else:
                # 없으면 현재 페이지 영화 id 사용
                ul = id
            res.append({'ig':ig, 'ul':ul})
    # // 영화 추천
    return render(request, 'movies/detail.html', {'movie':movie,'comment_form':comment_form, 'res':res, "ratingAvg":ratingAvg})


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
                    # 원본 주석처리
                    # resultMovie.append({searchMovie[c].title:searchMovie[c].id})
                    resultMovie.append({'title':searchMovie[c].title, 'id':searchMovie[c].id})
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

# 댓글 생성하기
@login_required
def commentCreate(request,id):
#   # 댓글 작성 폼을 list에서 보여줌.
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 유저정보, 몇번 글 넣어야 하는지 전달할거니까 기다려
        movie = Movie.objects.get(id=id)
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.movie = movie
        comment.save()
        
    return redirect('movies:detail',id)

# 댓글 삭제하기
@login_required
def commentDelete(request,id,comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this Comment")
    else:
        comment.delete()
    return redirect('movies:detail',id)
    
# 평점 등록하기
@login_required
def scoreCreate(request,id):
    rating = request.POST.get('rating')
    user = request.user
    movie = Movie.objects.get(id=id)
    score_list = Score.objects.filter(user=user,movie=movie)
    
    if score_list:
        score = score_list.update(rating=rating)
    else:
        score = Score.objects.create(user=user, movie=movie, rating=rating)

    return redirect('movies:detail',id)
  
# 오늘의 인물들을 보여주는 페이지
@login_required
def person(request):
    TMD_KEY = os.getenv('TMD_KEY')
    PERSON_URL = f"https://api.themoviedb.org/3/person/popular?api_key={TMD_KEY}&language=ko-KR"
    
    personData = requests.get(PERSON_URL)
    resPerson = personData.json().get('results')
    
    datas = []
    if len(resPerson) > 4:
        for n in range(4):
            # 배우 이름
            name = resPerson[n].get('name')
            # 배우 사진
            profile = "https://image.tmdb.org/t/p/w500" + resPerson[n].get('profile_path')
            # 배우 출연작
            known_for = resPerson[n].get('known_for')
            poster = "https://image.tmdb.org/t/p/w500" + known_for[0].get('poster_path')
            postId = known_for[0].get('id')
            # 영화가 나의 DB에 있는지 체크
            if Movie.objects.filter(tmd_id=postId):
                movie = Movie.objects.get(tmd_id=postId)
                poster_id = movie.id
            else:
                poster_id = ""
            num = str(n)
            datas.append({'name':name, 'poster':poster, 'profile':profile, 'poster_id':poster_id, 'num':num})
    else:
        for m in len(resPerson):
            name = resPerson[m].get('name')
            profile = "https://image.tmdb.org/t/p/w500" + resPerson[n].get('profile_path')
            known_for = resPerson[m].get('known_for')
            poster = "https://image.tmdb.org/t/p/w500" + known_for.get('poster_path')
            datas.append({'name':name, 'poster':poster, 'profile':profile})
            
    return render(request, 'movies/person.html', {'datas':datas})
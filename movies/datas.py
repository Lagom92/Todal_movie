# api 사용해서 정보 가져오는 내용 - 임시로 옮겨놨음
# 영진위 api//
    KURL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"
    key = os.getenv('KEY')
    itemPerPage = '5'  # 영화 개수
    MovieData = f"{KURL}?key={key}&itemPerPage={itemPerPage}"
    # f string 이 않되면 바꿔야함
    # MovieData = KURL + "?key=" + key + "&itemPerPage=" + itemPerPage
    res = requests.get(MovieData).json()['movieListResult']
    Movies = res.get("movieList")
    # //영진위 api
    
    # naver api//
    aver_url = "https://openapi.naver.com/v1/search/movie.json?query="
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
    # //naver api
    
    NURL = 'https://openapi.naver.com/v1/search/movie.json'
    query = '?query='
    

    
    # https://openapi.naver.com/v1/search/movie.xml?query=%EC%A3%BC%EC%8B%9D&display=10
    
    movienames=[]    # 영화이름들을 저장        
    movie_images = []    # 영화 이미지들을 저장
    for Movie in Movies:
        movienames.append(Movie['movieNm'])
        
        word = Movie['movieNm']
        # Movie.objects.create() model에 넣기 - 수정 필
        naver_url = NURL + query + word
        naver_movies = requests.get(naver_url, headers=headers).json()    # 검색 결과(json형태)
        if (naver_movies['items']):
            movie_image = naver_movies['items'][0]['image']
            movie_images.append(movie_image)
    datas = {
        'movienames':movienames, 
        'movie_images':movie_images
    }
## 프로젝트  기술 보고서  

# Todal Movie

영화 추천, 평가 사이트



| 팀명     | Todal           |
| -------- | --------------- |
| 구성원   | 윤은솔 , 양시영 |
| 보고일자 | 2019.05.16      |



------

## 목차



1. 팀원 정보 및 업무 분담 내역
2. 목표 서비스 구현 및 실제 구현 정도
3. 데이터 베이스 모델링
4. 핵심기능
5. 배포 서버 URL
6. 기타 (느낀점)
7. 출처 및 참고 사이트

------

### 1.팀원 정보 및 업무 분담 내역



|                         담당업무(정)                         |                         담당업무(부)                         |                         사용언어/툴                          | 담당자 |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----: |
| Project management<br />Database construction<br />Recommendation algorithm<br />Website construction | API management<br />Database management<br />UX/UI design<br />Website Distribution | Python<br />JavaScript<br />HTML/CSSS<br />Bootstrap<br />Django<br />SQLite<br />c9 | 윤은솔 |
| API management<br />Database management<br />UX/UI design<br /> Website Distribution | Project management<br />Database construction<br />Recommendation algorithm | Python<br />JavaScript<br />HTML/CSSS<br />Bootstrap<br />Django<br />SQLite<br />c9 | 양시영 |



------

### 2.목표 서비스 구현 및 실제 구현 정도



| 목표                                                         | 실제 구현                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Account                                                      |                                                              |
| 관리자의  영화 등록 및 삭제 기능<br />관리자의  유저 관리 기능<br />유저 회원가입 기능<br />유저 로그인 기능<br />유저 로그아웃 기능<br />회원정보 수정 | 관리자의  영화 등록 및 삭제 기능<br />관리자의  유저 관리 기능<br />유저 회원가입 기능<br />유저 로그인 기능<br />유저 로그아웃 기능<br /> |
| Movie Data Crolling                                          |                                                              |
| 영화진흥위원회 데이터 크롤링 <br /> 네이버 영화 검색 API 크롤링<br /> 데이터 수집 및 모델링<br />추천영화 데이터 수정 및 기능 구현 | The Movie Database API 크롤링<br /> 데이터 수집 및 모델링<br />추천영화 데이터 수정 및 기능 구현 |
| Website construction                                         |                                                              |
| 영화 제목을 통한 검색 기능 구현<br /> 댓글 생성 및 삭제 기능 구현<br /> 로그인 상태인 유저의 평점 등록/ 수정/삭제 기능 <br /> 오늘의 영화인  소개 및 관련 영화 정보 제공 기능 구현<br />영화 상세페이지를 통해 상세 정보 제공 기능 구현<br />pagination 기능 구현 | Website construction<br /> 영화 제목을 통한 검색 기능 구현<br /> 댓글 생성 및 삭제 기능 구현<br /> 로그인 상태인 유저의 평점 등록/ 수정/삭제 기능 <br /> 오늘의 영화인  소개 및 관련 영화 정보 제공 기능 구현<br />영화 상세페이지에서 상세 정보 제공 기능 구현<br />pagination 기능 구현 |

------

### 3.데이터 베이스 모델링



##### 서비스 아키텍쳐 - 이미지 링크 참고

https://zzu.li/todalDBMODEL





------

### 4.핵심 기능



##### 영화 검색 기능

단어를 검색하여 그 단어가 영화 제목에 들어가는 영화들을 검색 결과로 보여줌



##### 영화 추천 기능

영화 상세페이지에 들어가면 해당 영화와 관련있는 영화를 추천



##### 오늘의 유명인 추천 기능

하루에 1번씩 변경되는 영화 배우들의 이미지를 보여주고 해당 배우의 출연작을 통해 그 영화에 대한 상세 페이지로 이동



------

### 5.배포 서버 URL



##### URL 주소

```md
http://todal-dev.ap-northeast-2.elasticbeanstalk.com
```





------

### 6.기타(느낀점)



일을 함에 있어서 어디부터 어디까지는 누가하는지 일을 분배함에 있어서 어려움



협업의 어려움  ....



사이트에 적용하고 싶은 기능은 많았지만 시간과 능력에 한계를 느껴서 처음 원하던데로 만들지는 못함



개발 도중에 오류가 발생했을때 오류를 찾는데 어려움



프로젝트를 시작하는 초반에 일 먼저 앞으로 어떠한 방향으로 프로젝트를 만들어 나갈지 완전히 정해 놓고 시작하지 않아서 개발 중간에 방향이 달라지게 됨



개발을 막 하고 싶은 욕심과 현재 나의 실력과 제한된 시간 사이에서 조절을 하여 완성된 결과물을 만드는데 어려움이 느껴졌음



c9을 이용한 협업은 너무 힘듦

배운 내용을 통해 검색기능을 구현해보면서  내가 무엇을 놓치고 있는지. 할 수 있는지 알수 있었음 

------

### 7.출처 및 참고사이트

1. The movie DB

   <https://www.themoviedb.org/>

2. watcha

   <https://watcha.com/ko-KR>

3. fontawesome

   <https://fontawesome.com/>

4. googlefont

   <https://fonts.google.com/>


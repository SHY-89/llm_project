# LLM PROJECT
## 프로젝트 개요
    이 프로젝트는 Django를 기반으로 한 인터넷 쇼핑몰 개발과 OpenAI 연동을 목표로 합니다. 애자일 방법론을 적용하여 개발을 진행합니다.

## 프로세스
    애자일 방법론으로 제작

## 주요 기능
    - 회원 관리
        - 로그인 및 로그아웃
        - 회원 가입
        - 회원 탈퇴
        - 회원 정보 수정
        - 비밀번호 변경
    - 제품 관리
        - 제품 조회, 등록, 수정, 삭제
        - 찜하기 기능
        - 장바구니 담기
        - 제품 검색
    
    - 장바구니
        - 장바구니 조회
        - 장바구니 내 상품 삭제
        - 장바구니 내 상품 수량 수정
    

## 와이어프레임
![와이어프레임](/docs/image/LLM_PJ.png)

## ERD
![ERD](/docs/image/LLMProject.drawio.png)


## 개발 환경
    windows 10
    VScode
    sqlite3
    Python 3.10.14
    Django 4.2
    django-extensions 3.2.3
    django-mathfilters 1.0.0
    pillow 10.4.0


## API
    | **API 이름**     | **설명**                | **HTTP 메서드** | **엔드포인트**         |
    |------------------|-------------------------|-----------------|------------------------|
    | 로그인           | 사용자 로그인 처리      | POST            | /api/login             |
    | 회원 가입        | 새로운 사용자 등록      | POST            | /api/register          |
    | 제품 조회        | 모든 제품 목록 반환     | GET             | /api/products          |
    | 장바구니 추가    | 장바구니에 제품 추가    | POST            | /api/cart/add          |
    | 장바구니 조회    | 장바구니 내 제품 목록   | GET             | /api/cart              |
    | 회원 정보 수정   | 사용자 정보 업데이트    | PUT             | /api/user/update       |
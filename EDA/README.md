# Chatbot dataset(songys) EDA

---
## Question / Answer 토큰 빈도 분석
* 사용 예정인 사전학습 임베딩인 KoBERT와 KoGPT2의 토큰 빈도를 비교 및 분석한다.
* 모두 HuggingFace 패키지를 사용한다.
* Chatbot dataset은 Question과 Answer로 구성되어 있으므로 구분하여 분석한다.
---
### Question 단순 글자 수 빈도
![download](https://user-images.githubusercontent.com/75473005/147901005-e2421ef7-5fe7-45db-9f77-e819f648a12a.png)
### Answer 단순 글자 수 빈도
![download](https://user-images.githubusercontent.com/75473005/147901084-302904d2-2ba9-4b84-9257-e13f8347b6df.png)

* Answer의 최대 글자수 길이 범위가 Question보다 더 넓은 것을 알 수 있다.
* Question, Answer 모두 대부분 10~20 길이의 문장으로 이루어져 있다.
---
### Question KoGPT2 토큰 수 빈도
![download](https://user-images.githubusercontent.com/75473005/147901829-c32998b3-03e8-4a2b-91e3-2c5f46895246.png)
### Answer KoGPT2 토큰 수 빈도
![download](https://user-images.githubusercontent.com/75473005/147901848-d58ac75f-9c71-4624-afa5-497e85a37152.png)

* Question, Answer 모두 대부분 5~10개의 토큰으로 이루어져 있으나 Answer의 범위가 더 넓다.
---
### Question KoBERT 토큰 수 빈도
![download](https://user-images.githubusercontent.com/75473005/147901976-bc14d3dc-90ee-4247-bbc2-6c9ffc1bf8a0.png)
### Answer KoBERT 토큰 수 빈도
![download](https://user-images.githubusercontent.com/75473005/147901991-dbb1d7ab-9074-45ec-8335-3bdf5c41559a.png)

* KoBERT tokenizer 사용 결과 Question의 토큰 수 분포에서는 적은 쪽의 비중이 크다.
* Answer 보다는 Question의 분포가 좀 더 다양하다.
* 모든 분포의 skewness가 positive한 모습을 보인다.
---
## Question / Answer 명사 빈도 분석
* POS tagging을 위해 konlpy의 Mecab을 사용했다.
* Question과 Answer의 명사 빈도는 상위 40개의 명사를 가지고 시각화한다.
* 한글자 명사의 경우 명사인지 불분명한 것이 많기 때문에 제외한 결과도 포함한다.
---
### Question 명사 빈도
![download](https://user-images.githubusercontent.com/75473005/147902330-869495b1-e41c-4b4c-aa0b-b99998ccf6cc.png)
### Answer 명사 빈도
![download](https://user-images.githubusercontent.com/75473005/147902340-bd76f7b6-7ab6-420d-8f5b-601051d3f9d8.png)
* 사랑, 실연과 관련된 내용이 주를 이루는 데이터셋답게 사람을 지칭하거나 사람 간의 관계를 나타내는 명사가 많이 쓰였다.
* Question의 경우 "사람", "친구", "여자", "남자", "이별" 등 고민의 주체가 되는 대상에 대한 내용이 주를 이룬다.
* Answer의 경우 "필요", "지금", "걱정" 등 직접적인 고민에 대한 파생 단어가 주를 이룬다.
---
### Question 명사 빈도(2글자 이상)
![download](https://user-images.githubusercontent.com/75473005/147902847-29ba7072-dff8-45f1-9bb3-7f1ffc619665.png)
### Answer 명사 빈도(2글자 이상)
![download](https://user-images.githubusercontent.com/75473005/147902863-8990412b-5fbd-4b88-a6fb-37350ff5758e.png)
* 불분명한 한글자 명사를 제외한 후 의미 파악이 명확해지는 것을 알 수 있다.
* Question의 경우 마찬가지로 고민의 주체가 되는 사람을 지칭하는 명사와 "고백", "고민" 등의 명사가 주를 이룬다.
* Answer의 경우 "기억", "축하", "이해"와 같이 고민 해결 보다는 질문자에게 공감하는 듯한 명사가 추가되었다.
---
## Question / Answer 형태소 빈도
* 형태소 분석도 마찬가지로 konlpy의 Mecab으로 진행했다.
---
### Question 형태소 빈도
![download](https://user-images.githubusercontent.com/75473005/147903724-f3d85f75-27b3-4f4d-8538-1f1a98c456a3.png)
### Answer 형태소 빈도
![download](https://user-images.githubusercontent.com/75473005/147903755-9d9daf1a-ed19-4f51-811b-9584d146323c.png)

* Question, Answer 모두 NNG(명사)의 수가 가장 많았다.
* Question은 이후 EC(연결 어미), VV(동사), MAG(일반 부사), SF(마침표, 물음표, 느낌표), VA(형용사), JKS(주격 조사) 순으로 나타났다.
* Answer는 SF(마침표, 물음표, 느낌표), VV(동사), EC(연결 어미), EF(종결 어미), MAG(일반 부사), VA(형용사) 순으로 나타났다.
* 관련 자료: https://docs.google.com/spreadsheets/d/1-9blXKjtjeKZqsf4NzHeYJCrr49-nXeRF6D80udfcwY/edit#gid=589544265
---
## Question / Answer N-gram 통계
* 주변 단어가 없을 경우 한글자 명사가 불분명하듯, 동음이의어가 많은 한국어의 경우 함께 쓰이는 단어에 따라 중요도가 달라진다.
* N-gram 통계의 경우 자주 쓰이는 chunk의 동향을 살펴볼 수 있다.
* Mecab의 형태소 분석 결과에 대한 N-gram 분석은 scikit-learn의 CountVectorizer 패키지를 사용했다.
---
### Question 2-gram 통계(형태소)
![download](https://user-images.githubusercontent.com/75473005/147904658-2956b225-70a6-4bc5-b876-7b6f10bb30fa.png)
### Answer 2-gram 통계(형태소)
![download](https://user-images.githubusercontent.com/75473005/147904686-b8f04aa5-3dc8-4e8d-92c4-8ca06571929a.png)
* Question은 전형적인 연애 상담 주제와 관련된 chunk가 많이 보인다.
* Answer에서는 chunk로 봤을 때 고민에 대한 해결 방안을 제시하는 어조가 많이 보인다.
* Question과 Answer set이 약 12000개 남짓인 것을 생각해봤을 때, Answer에서 "생각 세요" or "생각 해요"가 약 200개를 차지하고 있는 것은 고민에 대해 bot이 어떻게 생각하는지, 또는 고민에 대해 다른 방식으로 생각해보라는 뉘앙스로 받아들일 수 있다.
### Question 3-gram 통계(형태소)
![download](https://user-images.githubusercontent.com/75473005/147904783-598edc2e-79a5-4345-991e-63e735d719a6.png)
### Answer 3-gram 통계(형태소)
![download](https://user-images.githubusercontent.com/75473005/147904806-70ff4910-caf6-48b2-833f-7a3e9a4f7b10.png)
* 3-gram 분석 결과, Question과 Answer의 차이가 2-gram보다 확연히 차이나는 것을 알 수 있다.
---
## Question / Answer 개체명 분석
* ETRI에서 제공하는 API를 이용해 개체명을 분석했다.
* 개체명 분석: https://aiopen.etri.re.kr/guide_wiseNLU.php#group01
* 1회 최대 1만 자, 1일 5000회 제한
* 문장 당 평균 10~20 글자, 넉넉히 50글자로 잡고 200개를 한 묶음으로 간주
* 묶음은 "\n"으로 join 된 결과
* 전체 데이터 수 = 11823*2 = 23646개
* Question / Answer 따로 한다면 200*60*2=12000*2 -> 60*2회
---
### Question 개체명 분포
![download](https://user-images.githubusercontent.com/75473005/147906637-eeb76f58-0d30-4097-9637-436711b98368.png)
### Answer 개체명 분포
![download](https://user-images.githubusercontent.com/75473005/147906660-f6666082-08b1-4a42-b79d-8c5f80a7a40b.png)
* 두 데이터셋 모두 "친구" 개체명이 가장 많은 빈도를 보이지만 이는 남자친구, 여자친구라는 단어에서 비롯한 것으로 보인다.
* Question에서는 토큰 분석과 마찬가지로 사람과 관련된 개체명이 많이 보인다.
* Answer에서는 전반적인 인간관계에서 비롯할 수 있는 개체명들이 많이 보인다.
### Question 개체명 태그 분포
![download](https://user-images.githubusercontent.com/75473005/147906888-eae5d08c-42f1-4581-9cc8-8ca4a119b68d.png)
### Answer 개체명 태그 분포
![download](https://user-images.githubusercontent.com/75473005/147906897-89648184-634d-4525-80ef-6cae13148612.png)
* Question, Answer 모두 CV_RELATION 개체명이 가장 많은 것을 알 수 있다.
### Question CV_RELATION 개체명 분포
![download](https://user-images.githubusercontent.com/75473005/147907171-4d34018d-2b62-498d-b13f-40a07ce9e928.png)
### Answer CV_RELATION 개체명 분포
![download](https://user-images.githubusercontent.com/75473005/147907179-dc9c7aa3-cfe7-4557-ab70-a175581e0f4f.png)
* CV_RELATION 개체명을 구성하는 개체명들이 Question에서 Answer 데이터셋보다 훨씬 다양한 것을 알 수 있다.
* 가족이나 다른 관계보다는 주로 연인과의 연애, 사랑 등에 관련된 데이터가 많음을 알 수 있다.

---

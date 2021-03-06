# 토큰화하기
# 샘플 텍스트로 작동 원리 알아보기

text <- tibble(value = "대한민국은 민주공화국이다. 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.")
text
# # A tibble: 1 x 1
# value
# <chr>
#   1 대한민국은 민주공화국이다. 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.~
  -----------------------------------------------------------------
install.packages("tidytext")
library("tidytext")

# 문장 기준
text %>%
  unnest_tokens(input = value, output = word, token = "sentences")
# # A tibble: 2 x 1
# word
# <chr>
#   1 대한민국은 민주공화국이다.
# 2 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.

# 띄어쓰기 기준
text %>%
  unnest_tokens(input = value, output = word, token = "words")
# # A tibble: 10 x 1
# word
# <chr>
#   1 대한민국은
# 2 민주공화국이다
# 3 대한민국의
# 4 주권은
# 5 국민에게
# 6 있고
# 7 모든
# 8 권력은
# 9 국민으로부터
# 10 나온다

# 문자 기준
text %>%
  unnest_tokens(input = value, output = word, token = "characters")
# # A tibble: 40 x 1
# word
# <chr>
#   1 대
# 2 한
# 3 민
# 4 국
# 5 은
# 6 민
# 7 주
# 8 공
# 9 화
# 10 국
# # ... with 30 more rows

word_space <- moon %>%
  unnest_tokens(input = value, output = word, token = "words")
word_space
# # A tibble: 2,025 x 1
# word
# <chr>
#   1 정권교체
# 2 하겠습니다
# 3 정치교체
# 4 하겠습니다
# 5 시대교체
# 6 하겠습니다
# 7 불비불명
# 8 이라는
# 9 고사가
# 10 있습니다
# # ... with 2,015 more rows
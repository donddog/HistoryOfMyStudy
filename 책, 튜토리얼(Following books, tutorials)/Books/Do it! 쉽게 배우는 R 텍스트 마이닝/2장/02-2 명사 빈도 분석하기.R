# 단어 빈도 구하기
word_noun <- word_noun %>%
  count(word, sort = T) %>%
  filter(str_count(word) > 1)

word_noun
# # A tibble: 704 x 2
# word       n
# <chr>  <int>
#   1 국민      21
# 2 일자리    21
# 3 나라      19
# 4 우리      17
# 5 경제      15
# 6 사회      14
# 7 성장      13
# 8 대통령    12
# 9 정치      12
# 10 하게      12
# # ... with 694 more rows
------------------------------------
# 막대 그래프 만들기
  
top20 <- word_noun %>%
  head(20)

library(ggplot2)
ggplot(top20, aes(x = reorder(word, n), y = n)) +
  geom_col() +
  coord_flip() +
  geom_text(aes(label = n), hjust = -0.3) +
  labs(x = NULL) +
  theme(text = element_text(family = "nanumgothic"))
------------------------------------
# 워드 클라우드 만들기  
  
library(showtext)
font_add_google(name = "Black Han Sans", family = "blackhansans")
showtext_auto()

library(ggwordcloud)
ggplot(word_noun, aes(label = word, size = n, col = n)) +
  geom_text_wordcloud(seed = 1234, family = "blackhansans") +
  scale_radius(limits = c(3, NA), range = c(3, 15)) + scale_color_gradient(low = "#66aaf2", high = "#004EA1") +
  theme_minimal()
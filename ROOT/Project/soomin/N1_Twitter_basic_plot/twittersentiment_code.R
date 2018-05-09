#junho
library(twitteR)
library(RColorBrewer)
library(dplyr)
library(Rserve)
Sys.setenv(LANG="en_US.UTF-8")

setwd("/home/soomin/Desktop/group_study/Statistics/R_language")
#SOUTH_KOREA = '35.549684,127.094529,300km'
NEWYORK='40.758896,-73.985130,200km'; #BOSTON='42.362701, -71.055044,200km'; 
SANF='37.774209,-122.426209,200km'; LA='34.121035,-118.323131,200km'


SAVE_FILE_PATH = "/home/soomin/Desktop/twitterR/LA_week7"

FROM='2018-05-04'
TO='2018-05-05'
KEY_WORD1='coke -filter:retweets'
KEY_WORD2='cola -filter:retweets'
KEY_WORD3='coffee -filter:retweets'
KEY_WORD4='tea -filter:retweets'

SAVE_FILE_NAME1 = "coke_0504Fri_LA.txt"
SAVE_FILE_NAME2 = "cola_0504Fri_LA.txt"
SAVE_FILE_NAME3 = "coffee_0504Fri_LA.txt"
SAVE_FILE_NAME4 = "tea_0504Fri_LA.txt"
#KEY_WORD5='"get water" -filter:retweets'
#KEY_WORD6='"got water" -filter:retweets'
NUMBER_OF_TWEETS=10000
city=LA



iphone_t = searchTwitter(KEY_WORD1, n=NUMBER_OF_TWEETS, lang="en", since=FROM ,
                         until=TO, geocode=city)
#head(iphone_t)
#iphone_t = searchTwitter(KEY_WORD, n=NUMBER_OF_TWEETS, lang="en", since=FROM ,
#                         until=TO, geocode=NEWYORK)

print(typeof(iphone_t))
head(iphone_t,15)
iphone_t=laply(iphone_t,function(t) t$getText())

iphone_t = gsub('[[:punct:]]','',iphone_t)
iphone_t = gsub("[[:cntrl:]]","",iphone_t)
iphone_t = gsub("http:[^ $]+","",iphone_t)

pos.word=scan("positive-words.txt", what = "character", comment.char = ";")
neg.word=scan("negative-words.txt", what = "character", comment.char = ";") 

setwd(SAVE_FILE_PATH)

head(iphone_t,5)
for (i in 1:length(iphone_t)){
  word.list = str_split(iphone_t[i],"\\s+")
  words = unlist(word.list)
  #print(words)
  total=length(words); print(total)
  pos.match = match(words, pos.word); pos.match = !is.na(pos.match); pos.score = sum(pos.match); print(pos.score)
  neg.match = match(words, neg.word); neg.match = !is.na(neg.match); neg.score = sum(neg.match); print(neg.score)
  
  soolist = c(total, pos.score, neg.score)
  if(i==1)
  {
    Msoolist = matrix(soolist, nrow=1,byrow = T)
  }  

  else{
    Fsoolist = matrix(soolist, nrow=1,byrow = T)
    Msoolist <- rbind(Msoolist, Fsoolist)
  }   
  
  print(Msoolist)

#  print(total,pos.score,neg.score)  
}
head(iphone_t,15)  
write.table(Msoolist, SAVE_FILE_NAME1 , row.names = F,quote = F )

########################################################

setwd("/home/soomin/Desktop/group_study/Statistics/R_language")
#SOUTH_KOREA = '35.549684,127.094529,300km'
NEWYORK='40.758896,-73.985130,200km'; #BOSTON='42.362701, -71.055044,200km'; 
SANF='37.774209,-122.426209,200km'; LA='34.121035,-118.323131,200km'


iphone_t = searchTwitter(KEY_WORD2, n=NUMBER_OF_TWEETS, lang="en", since=FROM ,
                         until=TO, geocode=city)
#head(iphone_t)
#iphone_t = searchTwitter(KEY_WORD, n=NUMBER_OF_TWEETS, lang="en", since=FROM ,
#                         until=TO, geocode=NEWYORK)

print(typeof(iphone_t))
head(iphone_t,15)
iphone_t=laply(iphone_t,function(t) t$getText())

iphone_t = gsub('[[:punct:]]','',iphone_t)
iphone_t = gsub("[[:cntrl:]]","",iphone_t)
iphone_t = gsub("http:[^ $]+","",iphone_t)

pos.word=scan("positive-words.txt", what = "character", comment.char = ";")
neg.word=scan("negative-words.txt", what = "character", comment.char = ";") 

setwd(SAVE_FILE_PATH)

head(iphone_t,5)
for (i in 1:length(iphone_t)){
  word.list = str_split(iphone_t[i],"\\s+")
  words = unlist(word.list)
  #print(words)
  total=length(words); print(total)
  pos.match = match(words, pos.word); pos.match = !is.na(pos.match); pos.score = sum(pos.match); print(pos.score)
  neg.match = match(words, neg.word); neg.match = !is.na(neg.match); neg.score = sum(neg.match); print(neg.score)
  
  soolist = c(total, pos.score, neg.score)
  if(i==1)
  {
    Msoolist = matrix(soolist, nrow=1,byrow = T)
  }  
  
  else{
    Fsoolist = matrix(soolist, nrow=1,byrow = T)
    Msoolist <- rbind(Msoolist, Fsoolist)
  }   
  
  print(Msoolist)
  
  #  print(total,pos.score,neg.score)  
}
head(iphone_t,15)  
write.table(Msoolist, SAVE_FILE_NAME2 , row.names = F,quote = F )


####################################################

setwd("/home/soomin/Desktop/group_study/Statistics/R_language")
#SOUTH_KOREA = '35.549684,127.094529,300km'
NEWYORK='40.758896,-73.985130,200km'; #BOSTON='42.362701, -71.055044,200km'; 
SANF='37.774209,-122.426209,200km'; LA='34.121035,-118.323131,200km'



iphone_t = searchTwitter(KEY_WORD3, n=NUMBER_OF_TWEETS, lang="en", since=FROM ,
                         until=TO, geocode=city)
#head(iphone_t)
#iphone_t = searchTwitter(KEY_WORD, n=NUMBER_OF_TWEETS, lang="en", since=FROM ,
#                         until=TO, geocode=NEWYORK)

print(typeof(iphone_t))
head(iphone_t,15)
iphone_t=laply(iphone_t,function(t) t$getText())

iphone_t = gsub('[[:punct:]]','',iphone_t)
iphone_t = gsub("[[:cntrl:]]","",iphone_t)
iphone_t = gsub("http:[^ $]+","",iphone_t)

pos.word=scan("positive-words.txt", what = "character", comment.char = ";")
neg.word=scan("negative-words.txt", what = "character", comment.char = ";") 

setwd(SAVE_FILE_PATH)

head(iphone_t,5)
for (i in 1:length(iphone_t)){
  word.list = str_split(iphone_t[i],"\\s+")
  words = unlist(word.list)
  #print(words)
  total=length(words); print(total)
  pos.match = match(words, pos.word); pos.match = !is.na(pos.match); pos.score = sum(pos.match); print(pos.score)
  neg.match = match(words, neg.word); neg.match = !is.na(neg.match); neg.score = sum(neg.match); print(neg.score)
  
  soolist = c(total, pos.score, neg.score)
  if(i==1)
  {
    Msoolist = matrix(soolist, nrow=1,byrow = T)
  }  
  
  else{
    Fsoolist = matrix(soolist, nrow=1,byrow = T)
    Msoolist <- rbind(Msoolist, Fsoolist)
  }   
  
  print(Msoolist)
  
  #  print(total,pos.score,neg.score)  
}
head(iphone_t,15)  
write.table(Msoolist, SAVE_FILE_NAME3 , row.names = F,quote = F )

########################################################
setwd("/home/soomin/Desktop/group_study/Statistics/R_language")
#SOUTH_KOREA = '35.549684,127.094529,300km'
NEWYORK='40.758896,-73.985130,200km'; #BOSTON='42.362701, -71.055044,200km'; 
SANF='37.774209,-122.426209,200km'; LA='34.121035,-118.323131,200km'


iphone_t = searchTwitter(KEY_WORD4, n=NUMBER_OF_TWEETS, lang="en", since=FROM ,
                         until=TO, geocode=city)
#head(iphone_t)
#iphone_t = searchTwitter(KEY_WORD, n=NUMBER_OF_TWEETS, lang="en", since=FROM ,
#                         until=TO, geocode=NEWYORK)

print(typeof(iphone_t))
head(iphone_t,15)
iphone_t=laply(iphone_t,function(t) t$getText())

iphone_t = gsub('[[:punct:]]','',iphone_t)
iphone_t = gsub("[[:cntrl:]]","",iphone_t)
iphone_t = gsub("http:[^ $]+","",iphone_t)

pos.word=scan("positive-words.txt", what = "character", comment.char = ";")
neg.word=scan("negative-words.txt", what = "character", comment.char = ";") 

setwd(SAVE_FILE_PATH)

head(iphone_t,5)
for (i in 1:length(iphone_t)){
  word.list = str_split(iphone_t[i],"\\s+")
  words = unlist(word.list)
  #print(words)
  total=length(words); print(total)
  pos.match = match(words, pos.word); pos.match = !is.na(pos.match); pos.score = sum(pos.match); print(pos.score)
  neg.match = match(words, neg.word); neg.match = !is.na(neg.match); neg.score = sum(neg.match); print(neg.score)
  
  soolist = c(total, pos.score, neg.score)
  if(i==1)
  {
    Msoolist = matrix(soolist, nrow=1,byrow = T)
  }  
  
  else{
    Fsoolist = matrix(soolist, nrow=1,byrow = T)
    Msoolist <- rbind(Msoolist, Fsoolist)
  }   
  
  print(Msoolist)
  
  #  print(total,pos.score,neg.score)  
}
head(iphone_t,15)  
write.table(Msoolist, SAVE_FILE_NAME4 , row.names = F,quote = F )


Import <- function(){
  setwd(file.path("D:/Program/R"))
  # 更改檔案目錄至R
  Data <- read.csv("Mobile Price Classification.csv", fileEncoding = 'UTF-8-BOM')
  print("讀取成功")
  return (Data)
}

Statistics <- function(data){
  print(summary(data)) # 查看 data summary
  library(Hmisc) #使用 Hmisc library
  print(describe(data)) #使用 Hmisc 的內建函數來查看 data summar
}

Plot <- function(data){
  name <- colnames(data)
  par(mfrow = c(2,2))
  for(count in 2:20){
    boxplot(data[count], xlab = name[count]) # 盒鬚圖
    
    qqnorm(data[,count]); # 常態機率圖
    qqline(data[,count],col="red") # 最佳斜線
  }
}

Analysis <- function(data){
  cor_ <- cor(data, method = 'pearson')
  View(cor_) # 查看相關係數
}

data <- Import()
Statistics(data)
Plot(data)
Analysis(data)


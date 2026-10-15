改模型接口：
改 config.json 里的模型名 为你接口支持的模型
"judge" : { "model" : "deepseek-chat" , "min_score" : 0.5 } , "usecases" : { "per_day" : 5 , "model" : "deepseek-chat" , ... }

运行本项目：
python3 -m radar daily
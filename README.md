# ai_learning

我的 Python + AI 学习记录。

## 项目背景



目标是成为 AI 应用开发工程师。
这个仓库记录我每天的学习代码，从 Python 基础到调用大模型 API。

## 文件说明

- `chat.py`          最简单的命令行对话练习
- `chat_test.py`     循环输入 + 判断名字的练习
- `chat_list.py`     命令行通讯录，支持添加、查看、删除，数据存 JSON
- `contact_book.py`  通讯录重写版
- `ai_chat.py`       调用 DeepSeek API 的流式聊天脚本，支持多轮对话

## 技术栈

- Python 3.12
- requests（HTTP 请求）
- json（数据持久化）
- DeepSeek API（大模型对话）
- Git / GitHub

## 安全说明

API Key 通过环境变量 `DEEPSEEK_API_KEY` 读取，不写入代码。
`data/` 目录是本地数据，已加入 `.gitignore`，不会上传。

测试更新
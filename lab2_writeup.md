## 存储改为 MongoDB

1. **依赖修改**
   在 [requirements.txt](https://super-waffle-x5qgjwq746q53vrgp.github.dev/) 中添加了 `pymongo` 和 `python-dotenv`，用于连接 MongoDB 和加载环境变量。
2. **模型层修改**
   在 [note_mongo.py](https://super-waffle-x5qgjwq746q53vrgp.github.dev/) 中，使用 `pymongo` 替换原有的 SQLAlchemy，定义了 `Note` 类和相关的 MongoDB 操作。通过 `MongoClient` 连接远程 MongoDB Atlas 实例，所有笔记数据存储在 `notes` 集合中。
3. **环境变量配置**
   在 [token.env](https://super-waffle-x5qgjwq746q53vrgp.github.dev/) 文件中添加了 `MONGO_URI`，用于存储 MongoDB 的连接字符串。代码通过 [load_dotenv](https://super-waffle-x5qgjwq746q53vrgp.github.dev/) 加载该变量，保证连接安全性和灵活性。

------

## 部署到 Vercel

1. **Vercel 配置**
   新增 [vercel.json](https://super-waffle-x5qgjwq746q53vrgp.github.dev/) 文件，指定 Python 入口为 [main.py](https://super-waffle-x5qgjwq746q53vrgp.github.dev/)，并配置路由。
2. **依赖管理**
   确保 [requirements.txt](https://super-waffle-x5qgjwq746q53vrgp.github.dev/) 包含所有依赖，Vercel 部署时会自动安装。
3. **环境变量设置**
   在 Vercel 项目设置中，添加 `MONGO_URI` 和 `SECRET_KEY` 环境变量，保证云端部署时能正确连接数据库。
4. **部署流程**
   - 将项目推送到 GitHub。
   - 在 Vercel 平台导入 GitHub 仓库，自动触发部署。
   - 部署完成后，应用可通过 Vercel 提供的域名访问。
## Storage Changed to MongoDB

1. **Dependency Modifications** Added pymongo and python-dotenv to [requirements.txt](https://super-waffle-x5qgjwq746q53vrgp.github.dev/), for connecting to MongoDB and loading environment variables.
2. **Model Layer Modifications** In [note_mongo.py](https://super-waffle-x5qgjwq746q53vrgp.github.dev/), replaced the original SQLAlchemy with pymongo, defined the Note class and related MongoDB operations. Connected to a remote MongoDB Atlas instance via MongoClient, with all note data stored in the notes collection.
3. **Environment Variable Configuration** Added MONGO_URI to the [token.env](https://super-waffle-x5qgjwq746q53vrgp.github.dev/) file to store the MongoDB connection string. The code loads this variable via [load_dotenv](https://super-waffle-x5qgjwq746q53vrgp.github.dev/), ensuring connection security and flexibility.

------

## Deployment to Vercel

1. **Vercel Configuration** Added a new [vercel.json](https://super-waffle-x5qgjwq746q53vrgp.github.dev/) file, specifying the Python entry point as [main.py](https://super-waffle-x5qgjwq746q53vrgp.github.dev/) and configuring routes.
2. **Dependency Management** Ensured [requirements.txt](https://super-waffle-x5qgjwq746q53vrgp.github.dev/) includes all dependencies, which Vercel will automatically install during deployment.
3. **Environment Variable Settings** In the Vercel project settings, added MONGO_URI and SECRET_KEY environment variables to ensure proper database connection during cloud deployment.
4. **Deployment Process**
   - Push the project to GitHub.
   - Import the GitHub repository on the Vercel platform, automatically triggering deployment.
   - After deployment is complete, the application can be accessed via the domain provided by Vercel.
